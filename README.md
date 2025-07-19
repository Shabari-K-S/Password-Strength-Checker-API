# 🔐 Password Strength Checker API

[![FastAPI](https://img.shields.io/badge/FastAPI-🚀-brightgreen)](https://fastapi.tiangolo.com/)
A powerful and lightweight API that analyzes the strength of a password and provides smart feedback to help users create secure, robust passwords.

👉 **Live on GitHub:** [Password-Strength-Checker-API](https://github.com/Shabari-K-S/Password-Strength-Checker-API)

---

## 🚀 Features

* ✅ Password strength scoring (Very Weak → Very Strong)
* 📊 Entropy calculation (bits of randomness)
* 🧠 Intelligent suggestions for improvement
* 🔍 Optional breach detection using [Have I Been Pwned](https://haveibeenpwned.com/API)
* ⚡ FastAPI-based, async, and super lightweight

---

## 📦 Installation

```bash
git clone https://github.com/Shabari-K-S/Password-Strength-Checker-API.git
cd Password-Strength-Checker-API
pip install -r requirements.txt
uvicorn main:app --reload
```

> Access the interactive API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📮 Endpoint: `/check-password`

### Method: `POST`

### Request

```json
{
  "password": "YourSecurePassword123!"
}
```

### Response

```json
{
  "strength": "Strong",
  "score": 75,
  "entropy": 84.56,
  "suggestions": [
    "Add more special characters",
    "Avoid repeated patterns"
  ],
  "breached": false
}
```

### Response Fields

| Field         | Type      | Description                                              |
| ------------- | --------- | -------------------------------------------------------- |
| `strength`    | string    | Password strength label (Very Weak → Very Strong)        |
| `score`       | integer   | Score between 0–100                                      |
| `entropy`     | float     | Estimated randomness of the password                     |
| `suggestions` | string\[] | Helpful tips to improve the password                     |
| `breached`    | boolean   | True if found in a known breach (via HaveIBeenPwned API) |

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **zxcvbn-python**
* **httpx**
* **Uvicorn**

---

## 📄 License

This project is licensed under the MIT License.
Feel free to use, fork, and contribute!

---

## 🙌 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes
4. Push to the branch (`git push origin feature-xyz`)
5. Open a Pull Request

---

## ✨ Author

Built with ❤️ by [Shabari K S](https://github.com/Shabari-K-S)

