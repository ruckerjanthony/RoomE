class MainHandler(webapp2.RequestHandler):
    def get(self):
        #this is how to print something out
        self.response.write('Hello webapp2 world!')

#creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True) 
