import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    message_template = read_template('template.html')
    MY_ADDRESS = 'your_email@gmail.com'
    PASSWORD = 'your_app_password' 
    successful_emails = 0
    failed_emails = []

    print("Connecting to email server...")
    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        print("Connected successfully!\n")
    except Exception as e:
        print(f"CRITICAL ERROR - Failed to connect to server: {e}")
        return 

    with open("dataset.csv", "r", encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        
        for row in csv_reader:
            if not row[1]:
                print(f"Skipped {row[0]}: No email address provided.")
                continue
                
            msg = MIMEMultipart()
            html_content = message_template.substitute(
                NAME=row[0], 
                TICKET_TYPE=row[2], 
                WORKSHOP=row[3], 
                DATE=row[4]
            )
            
            msg['From'] = MY_ADDRESS
            msg['To'] = row[1] 
            msg['Subject'] = f"Action Required: Your {row[2]} Registration Details"
            
            msg.attach(MIMEText(html_content, 'html')) 
            
            try:
                s.send_message(msg)
                print(f"Success: Sent ticket to {row[0]}")
                successful_emails += 1
                time.sleep(1.5) 
                
            except Exception as e:
                print(f"Error sending to {row[1]}: {e}")
                failed_emails.append(row[1])
            
            del msg
            
    s.quit()
    print("\n--- Automation Complete ---")
    print(f"Successfully sent: {successful_emails}")
    if failed_emails:
        print(f"Failed to send to: {len(failed_emails)} contacts.")

if __name__ == '__main__':
    main()
