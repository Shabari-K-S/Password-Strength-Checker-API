from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from zxcvbn import zxcvbn
import math
import httpx

app = FastAPI(title="Password Strength Checker API")

class PasswordRequest(BaseModel):
    password: str

class PasswordResponse(BaseModel):
    strength: str
    score: int
    entropy: float
    suggestions: list[str]
    breached: bool | None = None

def map_score_to_strength(score: int) -> str:
    return ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"][score]

def calculate_entropy(password: str) -> float:
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|" for c in password):
        charset_size += 32  # rough estimate of special chars
    if charset_size == 0:
        return 0
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

async def check_pwned(password: str) -> bool:
    import hashlib
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return suffix in response.text
    return None

@app.post("/check-password", response_model=PasswordResponse)
async def check_password(data: PasswordRequest):
    result = zxcvbn(data.password)
    score = result['score']
    strength = map_score_to_strength(score)
    suggestions = result['feedback']['suggestions']
    entropy = calculate_entropy(data.password)

    # Optional breach check (can be slow)
    breached = await check_pwned(data.password)

    return {
        "strength": strength,
        "score": score * 25,  # Convert to 0-100
        "entropy": entropy,
        "suggestions": suggestions if suggestions else ["No suggestions. Good password!"],
        "breached": breached
    }

@app.get("/ping")
def ping():
    return {"message": "pong"}