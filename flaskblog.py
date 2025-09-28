# necessary terminal commands to run  (USE BASH NOT POWERSHELL OR CMD)
 # export FLASK_APP = filename.py
  # flask --app filename run

# make it so your webpage debugs automatically
 # export FLASK_DEBUG = 1


from flask import Flask #Imports flask class 
app = Flask(__name__) # Making app an instance of Flask class, passing in __name__ (special var that means name of module)

@app.route("/") # Routes are what we type into our broswers to go to different pages. (About pages, contact pages, both made using route decorators)
# this app.route decorator will handle the complex back end stuff and allow us to write a function to return the info that is shown on our website
# for this specific route. The / is for the root of our website

# necessary terminal commands to run 
 # set FLASK_APP = filename.py
  # flask --app filename run



def hello():
    return "<h1>Hello World!</h1>"

# Run app directly using python without use flask --app filename run

if __name__ == '__main__':
    app.run(debug=True)

