import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List

def send_email(
    smtp_server: str,
    smtp_port: int,
    sender_email: str,
    sender_password: str,
    recipients: List[str],
    subject: str,
    message: str,
    attachment_path: str = None,
) -> bool:
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        if attachment_path:
            try:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={attachment_path.split("/")[-1]}'
                )
                msg.attach(part)
            except FileNotFoundError:
                print(f"Error: The file {attachment_path} was not found.")
                return False
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())
        
        print("Email sent successfully!")
        return True
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



if __name__ == "__main__":
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "chaudharin19298@gmail.com"
    sender_password = "vsmg mxry unyk dffo"
    
    
    recipients = ["vp.sitrc@gmail.com", "sampada1999deshmukh@gmail.com"]
    subject = "Application for Python Developer role"
    message = """
Dear recruiter,
I've attached my resume for your consideration so you know which teams
most closely match my skills and interests. Looking forward to talking
to you.

Regards,
Nikhil Chaudhari
Email: chaudharin19298@gmail.com
Contact No: +919766394028
"""
    attachment_path = "/home/lbsnaa/Downloads/Nikhil_chaudhari_9766394028.pdf"
    
    success = send_email(
        smtp_server,
        smtp_port,
        sender_email,
        sender_password,
        recipients,
        subject,
        message,
        attachment_path,
    )
    
    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
