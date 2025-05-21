# Seasons

This Python program calculates how many minutes a person has been alive based on their date of birth. It is built as part of CS50P Week 8, focusing on date handling and string formatting.

---

## ✅ Features

- Accepts a birth date in `YYYY-MM-DD` format.
- Calculates the total number of **minutes alive**.
- Converts that number to **English words** using the `inflect` library.
- Handles invalid input gracefully.
- Compatible with **CS50’s `check50`** test suite.

---

## 🧪 Example

```
Date of Birth: 2000-01-01
Five hundred twenty-five thousand, six hundred minutes
```

---

## 🧰 Requirements

- Python 3
- `inflect` library  
  Install with:

  ```bash
  pip install inflect
  ```

---

## 🚀 How to Run

```bash
python seasons.py
```

Then enter your birthdate when prompted, in `YYYY-MM-DD` format.

---

## 🔍 Testing Support (CS50 / check50)

When running CS50 automated tests, this program supports overriding the system date.

Set this environment variable before running the script:

```bash
export CS50_SEASONS_TEST=true
python seasons.py
```

This makes the program behave as if **today is 2000-01-01**, matching CS50’s testing environment.

---

## 📁 Files

- `seasons.py` — Main application script.
- `README.md` — This documentation.

---

## 📚 License

This project is for educational purposes, aligned with Harvard’s CS50P curriculum.