import os
import webapp2
import jinja2
from rot13 import Rot13



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),  autoescape = True)
rot13_tool = Rot13()

class Handler(webapp2.RequestHandler):

    '''
    Handler class for performing
    basic operations
    '''

    #Outputs to the browser
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    #Looks for template and add params
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    #Renders the template
    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPage(Handler):

    '''
    Home Page
    '''

    def get(self):
        items = self.request.get_all("food")
        self.render("shopping-list.html", items = items)

class FizzBuzzPage(Handler):

    '''
    FizzBuzz Page
    '''

    def get(self):

        number_of_iterations = self.request.get("n")
        print(number_of_iterations)

        if number_of_iterations and number_of_iterations.isdigit():
            number_of_iterations = int(number_of_iterations)

        self.render("fizzbuzz.html", n=number_of_iterations)

class Rot13Page(Handler):

    '''
    Rot13 Page
    '''

    def get(self):
        rot_value = self.request.params
        print(rot_value)
        self.render("rot13.html")

    def post(self):
        rot_value = self.request.get("text")
        rot_value = rot13_tool.process_value(rot_value)
        self.render("rot13.html", text=rot_value)

app = webapp2.WSGIApplication(
    [
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzzPage),
    ('/rot13', Rot13Page)
    ],
    debug = True)