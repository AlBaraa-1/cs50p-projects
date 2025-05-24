# CS50P Solutions Repository

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/CS50P-Harvard-red" alt="CS50P">
</p>

---

Welcome to my **CS50P** (Introduction to Programming with Python) solutions repository! This repo contains my solutions to each week's problem sets, with a focus on clean code, testing, and best practices.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Week 1](#week-1)
- [Week 2](#week-2)
- [Week 3](#week-3)
- [Week 4](#week-4)
- [Week 5](#week-5)
- [Week 6](#week-6)
- [Week 7](#week-7)
- [Week 8](#week-8)

---

## 🚀 Getting Started

Clone this repository:

```bash
git clone https://github.com/yourusername/cs50p-projects.git
cd cs50p-projects
```

Install any required dependencies for specific problems (see each folder's README or requirements):

```bash
pip install -r requirements.txt
```

Run any script with:

```bash
python <filename>.py
```

---

## Week 1

### Problem Set: Hello

* **File:** `bank.py`
  Prompts for a greeting and responds with different dollar amounts based on whether the greeting starts with "hello", "h", or otherwise.

### Problem Set: Life, the Universe, and Everything

* **File:** `deep.py`
  Asks for the Answer to the Great Question of Life, the Universe, and Everything; accepts "42", "forty two", or "forty-two" as valid.

### Problem Set: File Extensions

* **File:** `extensions.py`
  Reads a filename from the user and prints its MIME type based on the file extension (e.g., `.jpg`, `.pdf`).

### Problem Set: Calculator Interpreter

* **File:** `interpreter.py`
  Interprets simple arithmetic expressions (e.g., `3 + 4`) and prints the result rounded to one decimal place.

### Problem Set: Meal Time

* **File:** `meal.py`
  Prompts for a time in `HH:MM` format and prints whether it’s Breakfast, Lunch, or Dinner time.

---

## Week 2

### Problem Set: CamelCase

* **File:** `camel.py`
  Converts a camelCase string to snake\_case by inserting underscores before uppercase letters and converting all characters to lowercase.

### Problem Set: Coke

* **File:** `coke.py`
  Simulates a soda machine that accepts coins (25, 10, 5, 50) until a cost of 50 cents is reached, then computes and dispenses change.

### Problem Set: Nutrition

* **File:** `nutrition.py`
  Looks up and prints the calorie count for a given fruit from a predefined dictionary of nutrition values.

### Problem Set: Plates

* **File:** `plates.py`
  Validates vanity license plates according to rules on length, letters, digits, leading zeros, and ordering of letters and numbers.

### Problem Set: Twttr

* **File:** `twttr.py`
  Removes all vowels from user input and prints the remaining characters separated by commas.

## Week 3

### Problem Set: Fuel

* **File:** `fuel.py`
  Converts a fraction (X/Y) into a percentage string (e.g., “50%”), with “F” for ≥99% and “E” for ≤1%.

### Problem Set: Grocery

* **File:** `grocery.py`
  Reads grocery items from input until EOF, counts occurrences case-insensitively, and prints a sorted tally of each item.

### Problem Set: Outdated

* **File:** `outdated.py`
  Parses dates in either `M/D/Y` or `Month D, Y` formats and prints them as ISO `YYYY-MM-DD`.

### Problem Set: Taqueria

* **File:** `taqueria.py`
  Simulates a taqueria menu: prompts for menu items until EOF and prints a running total price formatted to two decimal places.

## Week 4

### Problem Set: Adieu

* **File:** `adieu.py`
  Prompts for names until EOF and prints a farewell using `inflect`’s `join`.

### Problem Set: Bitcoin

* **File:** `bitcoin.py`
  Fetches Bitcoin price via CoinCap API, multiplies by user-provided bitcoin amount, and prints total in USD.

### Problem Set: Emojize

* **File:** `emojize.py`
  Converts text containing emoji aliases (e.g., `:smile:`) into actual emojis using the `emoji` library.

### Problem Set: Figlet

* **File:** `figlet.py`
  Renders ASCII art with `pyfiglet`; accepts a font flag (`-f`/`--font`) or picks a random font.

### Problem Set: Game

* **File:** `game.py`
  Number-guessing game that prompts for difficulty and gives feedback until the correct guess.

### Problem Set: Professor

* **File:** `professor.py`
  Generates 10 math problems based on difficulty level, tracks score, and provides feedback on incorrect attempts.

## Week 5

### Problem Set: Back to the Bank

* **Folder:** `w5/back_to_the_bank/`

  * **Files:** `bank.py`, `bank_bugged.py`, `test_bank.py`
    Prompts for a greeting and responds with a dollar amount; includes bugged and fixed versions with tests.

### Problem Set: Refueling

* **Folder:** `w5/refueling/`

  * **Files:** `fuel.py`, `test_fuel.py`
    Converts a fuel fraction into a percentage string with `F`/`E` edge cases, tested for correct input and errors.

### Problem Set: Rerequesting a Vanity Plate

* **Folder:** `w5/rerequesting_a_vanity_plate/`

  * **Files:** `plates.py`, `plates_bugged.py`, `test_plates.py`
    Validates vanity plates by length, letter restrictions, and number formatting, with bugged version and accompanying tests.

### Problem Set: Testing My Twttr

* **Folder:** `w5/testing_my_twttr/`

  * **Files:** `twttr.py`, `twttr_bugged.py`, `test_twttr.py`
    Removes vowels from input, tests include handling of uppercase vowels and edge cases.

## Week 6

### Problem Set: Lines

* **File:** `lines.py`
  Counts the number of lines of actual code in a Python file, excluding comments and blank lines.

### Problem Set: Pizza

* **File:** `pizza.py`
  Reads a CSV file of pizza menu items and prints it as a formatted table using the `tabulate` library.

### Problem Set: Scourgify

* **File:** `scourgify.py`
  Reads a CSV file of names in "last, first" format and converts it to a CSV with "first, last, house" columns.

### Problem Set: Shirtificate

* **File:** `shirt.py`
  Overlays a transparent shirt image on top of a user-provided input image and saves the result, ensuring correct format, dimensions, and transparency handling.

## Week 7

### Problem Set: NUMB3RS

* **Folder:** `w7/numb3rs/`

  * **Files:** `numb3rs.py`, `numb3rs_bug1.py`, `numb3rs_bug2.py`, `test_numb3rs.py`
    Validates IPv4 addresses using regular expressions. Includes full and partial buggy versions and a test suite covering valid and invalid IP formats.

### Problem Set: Um

* **Folder:** `w7/um/`

  * **Files:** `um.py`, `um_bugged.py`, `um_bugged2.py`, `test_um.py`
    Counts how many times "um" appears as a standalone word in a sentence using regex. Includes tests for multiple occurrences and edge cases.

### Problem Set: Watch on YouTube

* **File:** `watch.py`
  Extracts YouTube video ID from an iframe HTML embed and converts it to a youtu.be URL using regex.

### Problem Set: Working Hours

* **Folder:** `w7/working/`

  * **Files:** `working.py`, `working_buged.py`, `import pytest.py`
    Converts 12-hour time ranges (e.g., 9 AM to 5 PM) to 24-hour format. Handles edge cases, invalid formats, and includes test suite.

### Problem Set: Response

* **File:** `response.py`
  Uses `validator-collection` to validate whether user input is a properly formatted email address.

---

## Week 8

### Problem Set: Cookie Jar

* **Folder:** `w8/Cookie Jar/`

  * **Files:** `jar.py`, `test_jar.py`
    Implements a cookie jar class with deposit/withdraw methods, capacity checks, and a test suite for correct and error cases.

### Problem Set: Seasons of Love

* **Folder:** `w8/Seasons of Love/`

  * **Files:** `seasons.py`, `test_seasons.py`, `README.md`
    Calculates the number of minutes a person has been alive from their date of birth, outputs the result in English words, and includes tests for date parsing and error handling.

### Problem Set: CS50 Shirtificate

* **Folder:** `w8/CS50 Shirtificate/`

  * **Files:** `shirtificate.py`, `shirtificate.png`
    Generates a PDF certificate with the user's name overlaid on a shirt image using the FPDF library.


---

<p align="center">
  <sub>CS50P provided by Harvard University. This repository is for educational and personal learning purposes only.</sub>
</p>
