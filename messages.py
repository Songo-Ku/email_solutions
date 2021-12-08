import jinja2


class Message:
    def __init__(self):
        self.template_loader = jinja2.FileSystemLoader(searchpath="./templates")
        self.template_env = jinja2.Environment(loader=self.template_loader)
        self.template_file = 'message.html'
        self.template = self.template_env.get_template(self.template_file)

    def render(self, **kwargs):
        return self.template.render(**kwargs)


class WelcomeMessage(Message):
    def __init__(self, template_file="welcome.html"):
        self.template_file = template_file
        super().__init__(self)




