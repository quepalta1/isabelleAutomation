import os
import smtplib



with smtplib.SMTP('mail.ellb.com.pe', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('ikervaire@ellb.com.pe', 'Peru2019')

    # subject = 'Grab dinner this weekend'
    # body = 'How about dinner at 6 pm.'

    msg = """From: Isabelle Kervaire <ikervaire@ellb.com.pe>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    smtp.sendmail('ikervaire@ellb.com.pe', 'wspramer@gmail.com', msg)
