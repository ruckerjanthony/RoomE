import webapp2
import jinja2
import os
from google.appengine.api import users


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('templates/RoomE.html')
     self.response.out.write(template.render())

class SignupHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('templates/sign_up.html')
     self.response.out.write(template.render())


class LoginHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('templates/login.html')
     self.response.out.write(template.render())

class PrefHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/start.html')
        self.response.out.write(template.render())


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:


            self.redirect("/home2")
        elif:
            greeting = ('<a href="%s">Sign in or Sign Up</a>.' %
            users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)

        else



#class Home2Handler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write("You're logged in!")
#creates a WSGIApplication and assigns it to the variable app.

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler),('/login', LoginHandler), ('/', HomeHandler),
    ('/home', MainPage), ('/home2', Home2Handler), ("/pref", PrefHandler)
], debug=True)
