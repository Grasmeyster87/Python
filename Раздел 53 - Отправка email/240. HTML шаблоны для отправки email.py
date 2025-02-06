from email.message import EmailMessage
import smtplib

from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(
    Path("./Раздел 53 - Отправка email/templates/index.html").read_text())

html_content = html_template.substitute(
    {'name': 'Vitaliy', 'date': 'tomorrow'})

my_email['from'] = 'Vitaliy'
# my_email['to'] = 'test@gmail.com'
my_email['to'] = 'friend@gmail.com'
# my_email['subject'] = "Hello from Python"
my_email['subject'] = "Let's go out"
# my_email.set_content("Hey! How are you doing?")
# my_email.set_content(html_content, 'html')
my_email.set_content(html_content)

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()  # метод для установки соединения
    # smtp_server.starttls()  # метод для шифрования
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was sent!')
