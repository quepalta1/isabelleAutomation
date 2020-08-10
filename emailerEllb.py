import os
import smtplib



with smtplib.SMTP('mail.ellb.com.pe', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('ikervaire@ellb.com.pe', 'Peru2019')

    # subject = 'Grab dinner this weekend'
    # body = 'How about dinner at 6 pm.'

    msg =  """From: Isabelle Kervaire <ikervaire@ellb.com.pe>
    To: Walter Pramer <wspramer@gmail.com>
    Subject: Testtt
    
    Hola que tal 
    """

    smtp.sendmail('ikervaire@ellb.com.pe', 'wspramer@gmail.com', msg)
