import webapp2
import jinja2
import os
from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"))

class Users (ndb.Model):
    Full_Name= ndb.StringProperty()
    Email = ndb.StringProperty()
    Gender= ndb.StringProperty()


class SignupHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('sign_up.html')
     self.response.out.write(template.render())
     user= Users()
     user.Full_Name= self.request.get("name")
     user.Email= self.request.get("email")
     user.Gender= self.request.get("gender")
     user.put()

class HomeHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('RoomE.html')
     self.response.out.write(template.render())




class LoginHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('login.html')
     self.response.out.write(template.render())

    def post(self):

        username= self.request.get("username")
        query= Users.query(Users.Email==username)
        user= query.get()
        username_value= self.request.cookies.get('get_username')


        self.response.set_cookie('get_username', user.Email, max_age=360, path='/')




        self.response.write("You're Logged In!")

class PrefHandler2(webapp2.RequestHandler):
    def post(self):
        template = jinja_environment.get_template('start_2.html')
        self.response.out.write(template.render())
        User_Preferences= Users()
        User_Preferences.Full_Name= self.request.get("name")
        User_Preferences.Email= self.request.get("email")
        User_Preferences.Gender= self.request.get("gender")
        user.put()


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:

            self.redirect("/home2")
        else:
            greeting = ('<a href="%s">Sign in or Sign Up</a>.' %
            users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)


class PrefHandler(webapp2.RequestHandler):
    def post(self):
        template = jinja_environment.get_template('start.html')
        self.response.out.write(template.render())
        user= Users()
        user.Full_Name= self.request.get("name")
        user.Email= self.request.get("email")
        user.Gender= self.request.get("gender")
        user.put()







#class Home2Handler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write("You're logged in!")
#creates a WSGIApplication and assigns it to the variable app.

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/', HomeHandler),
    ('/home', MainPage),
    ("/pref", PrefHandler),
    ('/pref2', PrefHandler2),
    ("/data", Users),

], debug=True)
