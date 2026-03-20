# Automated Email Sender

A Python automation script designed to send bulk, personalized emails by extracting contact details and custom data from a CSV file and mapping it to a text template.

## Features
* **Dynamic Content:** Uses Python's `string.Template` to inject personalized data into each email.
* **CSV Integration:** Reads recipient data dynamically from `details.csv`.
* **Secure SMTP:** Utilizes `smtplib` and TLS encryption to securely route emails via Gmail's servers.

## Files in this Repository
* `main.py`: The core automation script.
* `template.txt`: The structural blueprint for the email body.
* `details.csv`: The database containing recipient information and custom variables.

## Future Improvements
* Adding a graphical user interface (GUI) for non-technical users.
* Implementing attachment support for PDFs and images.
