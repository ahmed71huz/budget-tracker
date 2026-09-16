# 💰 Budget Tracker

A simple full-stack web app to track personal income and expenses, built with Python and Flask.

## Features

- Add, edit, and delete income/expense transactions
- Dashboard with total income, total expense, balance, and spending by category
- Export all transactions to a formatted Excel report (.xlsx)

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Reporting:** openpyxl (Excel export)
- **Frontend:** HTML + Jinja2 templates

## How to Run

1. Clone the repository:
```bash
   git clone https://github.com/ahmed71huz/budget-tracker.git
   cd budget-tracker
```
2. Create a virtual environment and activate it:
```bash
   python3 -m venv venv
   venv\Scripts\Activate.ps1   # Windows
```
3. Install dependencies:
```bash
   pip install flask openpyxl
```
4. Run the app:
```bash
   python3 app.py
```
5. Open `http://127.0.0.1:5000` in your browser.
