# zainstaluj python-dotenv jinja2

from gmail_adapter import GmailAdapter  # importuje class z stworzonego modulu
# from messages import WelcomeMessage dont know why but i cannot load it
# import zmiennych srodowiskowych
from dotenv import dotenv_values
from os import getenv, environ, path


# it works if we dont use welcomemessage but use destination

config = dotenv_values(".env")
print(config.get('USERNAME'))

mailer = GmailAdapter(
    host='smtp.gmail.com',
    port=465,
    username=config.get('USERNAME'),
    password=config.get('PASSWORD'),
)
mailer.login()
# welcome = WelcomeMessage()





# welcome = 'added from fingers because WelcomeMessage class cant be imported'
mailer.send_mail(
    recipient_email='bartosz.badlewski@gmail.com',
    subject='hello first email delivered from python3',
    content=' twoja stara i jest gitara dupa dupeczka')



# from jinja2 import Environment, FileSystemLoader, PackageLoader
# import jinja2
# template = env.get_template('child.html')
#
# template_loader = jinja2.FileSystemLoader(searchpath="./templates")
# template_env = jinja2.Environment(loader=template_loader)  # to jest jako env
# template_file = 'welcome.html'
# template = template_env.get_template(template_file)







# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     send_f()


