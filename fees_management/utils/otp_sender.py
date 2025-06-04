# fees_management/utils/otp_sender.py

import smtplib
from email.mime.text import MIMEText

def send_otp(receiver_email, otp):
    try:
        sender_email = "dineshjangra0063@gmail.com"
        app_password = "wgpecndcfpayasgg"

        msg = MIMEText(f"Your OTP is: {otp}")
        msg['Subject'] = "OTP Verification"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("❌ OTP Error:", e)
        return False
