# SauceDemo Automation Framework

## Project Overview

This project is an end-to-end Selenium Automation Framework developed using Python and Pytest following the Page Object Model (POM) design pattern.

The framework automates the SauceDemo web application by validating login, cart, checkout, sorting, and reset functionalities.

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- OpenPyXL
- Pytest HTML Report
- Allure Report
- WebDriver Manager

---

## Project Structure

```
SauceDemo_Automation_Framework/
│
├── pages/
├── tests/
├── utilities/
├── test_data/
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

- Page Object Model
- Explicit Waits
- Data Driven Testing using Excel
- Pytest Parameterization
- Pytest Markers
- Logging
- Automatic Screenshot on Failure
- HTML Reports
- Allure Reports
- Random Product Selection
- Reusable Utility Classes

---

## Test Cases Automated

- Login
- Invalid Login
- Logout
- Cart Verification
- Random Product Selection
- Add Products to Cart
- Cart Validation
- Checkout
- Product Sorting
- Reset App State

---

## Installation

Clone the repository

```bash
git clone <repository_url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

Run complete suite

```bash
pytest
```

Run specific marker

```bash
pytest -m login
```

Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Generate Allure Results

```bash
pytest --alluredir=allure-results
```

Generate Allure Report

```bash
allure serve allure-results
```

---

## Reports

- HTML Report
- Allure Report

---

## Design Pattern

- Page Object Model (POM)

---

## Author

**Dhanusriya Sugananth**