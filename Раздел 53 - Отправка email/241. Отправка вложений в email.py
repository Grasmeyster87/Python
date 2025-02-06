from email.message import EmailMessage
import smtplib

from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(
    Path("./Раздел 53 - Отправка email/templates/index.html").read_text())

html_content = html_template.substitute(
    {'name': 'Vitaliy', 'date': 'tomorrow'})

my_email['from'] = 'Vitaliy <bs@gmail.com>'
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Email with image"
my_email.set_content("Hey! How are you doing?")
my_email.set_content(html_content, 'html')

with open('./Раздел 53 - Отправка email/images/thumb-1920-1320168.jpeg', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image',
                            subtype='jpeg', filename='thumb-1920-1320168.jpeg')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()  # метод для установки соединения
    # smtp_server.starttls()  # метод для шифрования
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was sent!')
