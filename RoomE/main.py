import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SignupHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('templates/sign_up.html')
     self.response.out.write(template.render())


class LoginHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('templates/login.html')
     self.response.out.write(template.render())


#creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
    ('/signup', SignupHandler),('/login', LoginHandler)
], debug=True)
