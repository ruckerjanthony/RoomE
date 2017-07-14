import webapp2
import jinja2
import os
from google.appengine.ext import ndb
import logging



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"))

class User (ndb.Model):
    Full_Name= ndb.StringProperty()
    Username = ndb.StringProperty()
    Gender= ndb.StringProperty()

class SignupHandler(webapp2.RequestHandler):
    def get(self):

     logging.info(self.request.get("Username"))
     user= User()
     user.Full_Name= self.request.get("name")
     user.Username= self.request.get("Username")
     user.Gender= self.request.get("gender")

     user.put()

     self.response.set_cookie('get_username', user.Username, max_age=360,
     path='/')

     template = jinja_environment.get_template('sign_up.html')
     self.response.write(template.render())

     logging.info(user.Username)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('RoomE.html')
     self.response.out.write(template.render())


class Preferences(ndb.Model):

     username=ndb.StringProperty()
     smoke=ndb.BooleanProperty()
     late_riser=ndb.BooleanProperty()
     snore=ndb.BooleanProperty()
     activity_level=ndb.StringProperty()
     sexuality=ndb.StringProperty()
     religion=ndb.StringProperty()
     religion_imp=ndb.StringProperty()
     origin=ndb.StringProperty()
     working=ndb.BooleanProperty()
     major=ndb.StringProperty()
     organization=ndb.StringProperty()
     social_level=ndb.StringProperty()
     hobbies=ndb.StringProperty()


class LoginHandler(webapp2.RequestHandler):
    def get(self):
     template = jinja_environment.get_template('login.html')
     self.response.out.write(template.render())

    def post(self):

        username= self.request.get("username")

        query= User.query(User.Username==username)
        user= query.get()
        username_value= self.request.cookies.get('get_username')

        if user:

            self.response.set_cookie('get_username', user.Username, max_age=360,
            path='/')

            # self.response.write("You're Logged In!")
            #
            self.redirect("/profile")

        else:

            self.response.write("Unrecognized Username")



class PrefHandler2(webapp2.RequestHandler):
    def post(self):
        User_Preferences= Preferences()

        fields= ["smoke", "late_riser", "snore", ]


        for field in fields:

            valid= self.request.get(field)=="yes"
            setattr(User_Preferences, field, valid)



        #for trait in traits:

            Traits=[ "Extrovert", "Introvert", "Agreeable", "Sarcastic""Confident",
            "Colorful", "Curteous", "Disciplined", "Honest", "Humble", "Neat", "Genuine",
            "Playful", "Peaceful", "Precise", "Rational", "Resourceful", "Prepared",
            "Logistical", "Systematic", "Stoic", "Trusting", "Realistic", "Sophisticated",
            "Practical", "Loyal", "Independent", "Decisive"]

            #Ask Josh about fixing this so that this data can actually be read
            #setattr(User_Preferences, trait, valid)

        User_Preferences.username=self.request.cookies.get('get_username')  #not working
        #User_Preferences.username=self.request.get("username")
        User_Preferences.activity_level=self.request.get("activity_level")
        User_Preferences.sexuality=self.request.get("sexuality")
        User_Preferences.religion= self.request.get("religion")            #not working
        User_Preferences.religion_imp= self.request.get("religion_imp")    #not working
        #User_Preferences.working= self.request.get("working") #returns an error in the code(says "NONE in the database")
        User_Preferences.major= self.request.get("major")
        User_Preferences.put()
        logging.info(User_Preferences)



        template = jinja_environment.get_template('/start_2.html')
        self.response.out.write(template.render())


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
        tpl_dict={"username": self.request.get("Username")}
        template = jinja_environment.get_template('start.html')
        self.response.out.write(template.render(tpl_dict))
        user= User()
        user.Full_Name= self.request.get("name")
        user.Username= self.request.get("Username")
        user.Gender= self.request.get("gender")

        self.response.set_cookie('get_username', user.Username, max_age=360,
         path='/')
        user.put()
class PrefHandler3(webapp2.RequestHandler):
        def post(self):

            User_Preferences= Preferences()
            User_Preferences.origin= self.request.get("origin")
            User_Preferences.organization= self.request.get("organization")
            User_Preferences.social_level= self.request.get("social_level")
            User_Preferences.hobbies=self.request.get("hobbies")
            User_Preferences.put()


            self.response.write("orgin")
            self.response.write("organization")
            self.response.write("social_level")
            self.response.write("hobbies")

            template = jinja_environment.get_template('/start_2.html')
            self.response.out.write(template.render())



class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        username_value= self.request.cookies.get('get_username')
        template = jinja_environment.get_template('profile.html')
        user_preferences= Preferences.query(Preferences.username==username_value)
        display_user_preferences= user_preferences.get()
        ## self.response.write(display_user_preferences)

        self.response.out.write(template.render({"Profile": username_value, "Profile_Info":display_user_preferences}))






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
    ('/profile', ProfileHandler)

], debug=True)
