import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.model import Email
from scripts.constants.email import email_object
from scripts.core.handlers.grocery_handler import Grocery_handler


class Email_handler:

    def send_email(self, Email: Email):
        sender_email = email_object.email_name
        sender_password = email_object.email_password
        receiver_email = Email.rec_email

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Total Price Of The Grocery List"

        bill_object = Grocery_handler()
        result = bill_object.find_total()


        body = str(result)
        message.attach(
            MIMEText(("THESE ARE THE ITEMS IN YOUR GROCERY :\n"  + "\n Total amount : " + body), "plain"))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            server.quit()
            return {"message": "Email sent successfully"}

        except Exception as e:
            return {"message": str(e)}
