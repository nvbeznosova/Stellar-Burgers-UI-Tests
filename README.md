markdown
# Stellar Burgers — Selenium Test Automation

Automated UI tests for [Stellar Burgers](https://stellarburgers.nomoreparties.site/), 
a space-themed fast-food web application where users can build and order custom burgers.

## Project Description

This project contains end-to-end UI tests built with **Selenium WebDriver** and **pytest**. 
The tests verify critical user flows including registration, login, account management, 
and burger constructor navigation.

## Test Coverage

### Registration
- Successful registration with valid data
- Error message for invalid password (less than 6 characters)

### Login
- Via "Sign In" button on the main page
- Via "Personal Account" button
- Via registration form
- Via password recovery form

### Personal Account
- Navigate to personal account
- Navigate back to Constructor via "Constructor" button
- Navigate back via logo click
- Logout from account

### Constructor
- Tab switching between sections:
  - Buns
  - Sauces
  - Fillings

## Project Structure

```
Stellar-Burgers-UI-Tests/
    ├── README.md
    ├── conftest.py
    ├── requirements.txt
    ├── utils.py
    ├── locators/
    │   ├── __init__.py
    │   ├── constructor_page_locators.py
    │   ├── login_page_locators.py
    │   ├── personal_account_locators.py
    │   └── registration_page_locators.py
    ├── pages/
    │   ├── login_page.py
    │   ├── main_page.py
    │   └── register_page.py
    └── tests/
        ├── test_constructor.py
        ├── test_login.py
        ├── test_personal_account.py
        └── test_registration.py

```

## Setup & Installation

### Requirements
- Python 3.13+
- Google Chrome (latest version)
- Selenium
- Webdriver Manager
- pytest

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nvbeznosova/Stellar-Burgers-UI-Tests.git
   cd Stellar-Burgers-UI-Tests
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   # .venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running tests

1. **Run all tests**:
    ```bash
   pytest tests/
   ```

2. **Run a specific test file**:
    ```bash
   pytest tests/test_registration.py
   ```

3. **Run with verbose output**: 
   ```bash
   pytest -v tests/
   ```


All tests are independent: each test opens its own browser instance, executes checks, and closes the browser using driver.quit().

## Generating Test Data
```python
from utils import generate_email, generate_password

email = generate_email()
password = generate_password()
```