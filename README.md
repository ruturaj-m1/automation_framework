# 🧪 SauceDemo + ReqRes Automation Framework

Hybrid test automation framework using **Python**, **Selenium**, **Pytest**, and **Requests** that automates:

🔹 UI checkout flow on [SauceDemo](https://www.saucedemo.com/)  
🔹 Full CRUD API testing on [ReqRes](https://reqres.in/)

---

## 📂 Tech Stack

| Layer      | Tech / Tool                         |
|------------|-------------------------------------|
| Language   | Python 3.8+                         |
| UI Test    | Selenium WebDriver                  |
| Framework  | Pytest + Page Object Model (POM)    |
| API Test   | Requests (with Headers)             |
| Reports    | Pytest HTML                         |
| Extras     | YAML config                         |

---

## 📁 Project Structure

```
automation_framework/
├── apis/                # ReqRes API wrappers
├── config/              # YAML config (URLs, creds)
├── pages/               # POM classes for SauceDemo
├── tests/               # Pytest test cases
├── conftest.py          # Pytest fixtures (browser, config)
├── requirements.txt     # Dependencies
└── README.md            # This file
```

---

## ✅ Features

### 🧪 UI Tests — SauceDemo

- Login with standard user  
- Add products to cart  
- Checkout and fill customer info  
- Complete the order  
- Assert success message  

### 🌐 API Tests — ReqRes.in

- **POST** → Create user  
- **GET** → Read user  
- **PUT** → Update user  
- **DELETE** → Remove user  
- Status code + response validations  

---

## ⚙️ Installation & Run

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧪 Run UI Tests

```bash
pytest tests/test_sauce_ui.py --html=report_ui.html
```

### 🌐 Run API Tests

```bash
pytest tests/test_reqres_api.py --html=report_api.html
```

---

## 📊 Sample Report Preview

After test run, open:

- `report_ui.html` → UI Test Results  
- `report_api.html` → API Test Results  

---

## 📌 Notes

- `reqres.in` is a mock API: data isn't persisted after `POST`  
- Only users with ID **1–12** return data for `GET`  
- `x-api-key` is required in headers for ReqRes now  

---

## 📬 Author

**Ruturaj Mohapatra**  
*Python | Selenium | Automation Engineer*  
🔗 [LinkedIn](https://www.linkedin.com/in/ruturajm1/)
