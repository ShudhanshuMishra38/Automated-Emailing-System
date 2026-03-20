# Advanced Email Automation Pipeline

A robust Python automation script engineered to parse realistic event data and dispatch personalized, HTML-formatted confirmation emails in bulk.

## Core Features & Technical Upgrades
* **Fault Tolerance:** Implemented `try/except` blocks to handle SMTP server timeouts and prevent script crashes due to malformed dataset rows.
* **Anti-Spam Rate Limiting:** Utilized Python's `time` module to throttle API calls, ensuring compliance with standard email provider spam limits.
* **Rich HTML Templates:** Replaced plain text with dynamic, inline-CSS HTML templates using `MIMEText` for professional-grade formatting.
* **Data Validation:** Includes logic to skip null or missing data entries during iteration.
* **Terminal Analytics:** Generates a post-execution report detailing successful deliveries versus failures.

## Usage Scenario
Designed for a mock "Tech Conference," this script ingests a 15-row dataset (`dataset.csv`) containing Name, Email, Ticket Tier, and Workshop assignments, and dynamically injects them into a branded HTML confirmation email.
