import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv('.env')

def send_email(name: str):
    email_body = f"""
    <h1>Olá {name}!<h1>
    <p> Seja muito bem vindo ao nosso Aplicativo de Simulados!<p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Boas Vindas ao APPSimux'
    msg['From'] = 'jailsoncardoz123@gmail.com'
    msg['To'] = 'jailson.zarur@ufpi.edu.br'
    password = os.getenv('PASSWORD')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
