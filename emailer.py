
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
isa_user = 'ikervaire@ellb.com.pe'
isa_pass = 'Peru2019'

with smtplib.SMTP('mail.ellb.com.pe', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(isa_user, isa_pass)

    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6 pm.'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(isa_user, isa_user, msg)
