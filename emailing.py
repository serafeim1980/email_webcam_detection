from email.message import EmailMessage
import filetype
from dotenv import load_dotenv
import os
import smtplib


load_dotenv()
api_key = os.getenv("API_KEY")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")


    with open(image_path, "rb") as file:
        content = file.read()

    kind = filetype.guess(content)
    if kind is None:
        raise ValueError
    email_message.add_attachment(content, maintype="image", subtype=kind.extension)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, api_key)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email(image_path="images/19.png")