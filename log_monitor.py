# this script monitors a specified log file in real-time and sends an email notification if a specific error message appears

import time
import smtplib
from email.message import EmailMessage

def monitor_log_file(log_file, error_pattern, email_config):
    with open(log_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue

            if error_pattern in line:
                send_email_notification(line, email_config)

def send_email_notification(error_line, email_config):
    msg = EmailMessage()
    msg.set_content(f"An error occurred: {error_line}")
    msg["Subject"] = "Error Notification"
    msg["From"] = email_config["from_email"]
    msg["To"] = email_config["to_email"]

    with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
        server.login(email_config["username"], email_config["password"])
        server.send_message(msg)

email_config = {
    "from_email": "your-email@example.com",
    "to_email": "recipient@example.com",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "username": "your-username",
    "password": "your-password"
}

monitor_log_file("application.log", "ERROR", email_config)
