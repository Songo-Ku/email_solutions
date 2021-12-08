from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, PackageLoader
import os
from gmail_adapter import GmailAdapter  # importuje class z stworzonego modulu

from dotenv import dotenv_values


def get_data():
    data = []
    data.append(
        {
         "movies": [
             {
                 "title": 'Terminator',
                 "description": 'One soldier is sent back to protect her from the killing machine. He must find Sarah before the Terminator can carry out its mission.'
             },
             {
                 "title": 'Seven Years in Tibet',
                 "description": 'Seven Years in Tibet is a 1997 American biographical war drama film based on the 1952 book of the same name written by Austrian mountaineer Heinrich Harrer on his experiences in Tibet.'
             },
             {
                 "title": 'The Lion King',
                 "description": 'A young lion prince is born in Africa, thus making his uncle Scar the second in line to the throne. Scar plots with the hyenas to kill King Mufasa and Prince Simba, thus making himself King. The King is killed and Simba is led to believe by Scar that it was his fault, and so flees the kingdom in shame.'
             }
         ]
         })
    return data


def send_mail(bodyContent):
    config = dotenv_values(".env")
    to_email = 'bartosz.badlewski@gmail.com'
    from_email = config.get('USERNAME')
    password = config.get('PASSWORD')
    subject = 'This is a email from Python with a movies list!'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email

    message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msgBody)
    server.quit()


def send_movie_list(env, context_file_html):
    json_data = get_data()
    template = env.get_template(context_file_html)
    output = template.render(data=json_data[0])
    send_mail(output)
    return "Mail sent successfully."


# template_loader = FileSystemLoader(searchpath="./templates")
# template_env = Environment(loader=template_loader)  # to jest jako env
# template_file = 'welcome.html'
# template = template_env.get_template(template_file)
# output = template.render(data=json_data[0])

template_loader = FileSystemLoader(searchpath="./templates")
template_env = Environment(loader=template_loader)  # to jest jako env
send_movie_list(template_env, 'child.html')


