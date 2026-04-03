# 🔐 Password Generator with Username Save

A simple Python script that generates a strong random password and saves it to a plain text file along with the username.

## ✨ Features

* Generates secure random passwords
* Includes lowercase, uppercase, digits, and special characters
* User-defined password length
* Saves username + password to `passwords.txt`
* Appends multiple entries (does not overwrite)

## 📦 Requirements

* Python 3.x
* No external libraries needed (uses built-in modules)

## 🚀 How to Run

```bash
python pass_gen.py
```

## 🧑‍💻 Usage

1. Enter the username
2. Enter desired password length
3. Password is generated
4. Credentials saved to `passwords.txt`

Example:

```
Enter username: sanket
Enter the desired password length: 10
Generated Password: A@7kLp!2Qa
Saved to passwords.txt successfully.
```

## 📄 Output File

The script creates/updates:

```
passwords.txt
```

Example content:

```
Username: sanket | Password: A@7kLp!2Qa
Username: admin  | Password: 9#Lm2P!xQa
```

## 📁 Project Structure

```
password-generator/
│
├── pass_gen.py
└── passwords.txt
```

## 🔒 Password Rules

* Minimum length: 4
* Contains at least:

  * 1 lowercase letter
  * 1 uppercase letter
  * 1 digit
  * 1 special character

## 🛠 Built With

* Python
* random
* string

## 📌 Notes

* Passwords are stored in plain text (not encrypted)
* Do not use for production systems
* For learning/demo purposes only

## 👨‍💻 Author

Sanket Bhuite
