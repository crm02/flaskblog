# necessary terminal commands to run  (USE BASH NOT POWERSHELL OR CMD)
 # export FLASK_APP = filename.py
  # flask --app filename run

# make it so your webpage debugs automatically
 # export FLASK_DEBUG = 1


from flask import Flask, render_template #Imports flask class 
app = Flask(__name__) # Making app an instance of Flask class, passing in __name__ (special var that means name of module)

posts = [  # represents the return value of a database query, we can past this into our template, by
    # passing an argument with our data. In the def home() function below, posts=posts
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2025'
    },
    {
        'author': 'Cody Miller',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2025'
    }
]


@app.route("/") # Routes are what we type into our broswers to go to different pages. (About pages, contact pages, both made using route decorators)
# this app.route decorator will handle the complex back end stuff and allow us to write a function to return the info that is shown on our website
# for this specific route. The / is for the root of our website



# necessary terminal commands to run 
 # set FLASK_APP = filename.py
  # flask --app filename run


@app.route("/home") # home page route
def home():
    return render_template('home.html',posts=posts) # render_template function looks in templates folder for html file
    # we can pass in variables to our html file by passing them as arguments to render_template
    # in this case we are passing in posts=posts, the first posts is the name

@app.route("/about") # about page route
def about():
    return render_template('about.html', title = 'About')






# Run app directly using python without use flask --app filename run

if __name__ == '__main__':
    app.run(debug=True)

