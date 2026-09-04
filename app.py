#Imports the Flask class from the Flask library
#Able for python to act as a web server/application
from flask import Flask, render_template

#render_template allows Flask to load an HTML file

#Creates the Flask application
app = Flask(__name__) #storing variable named app
#__name__ --> tells Flask which Python module is running the application

#When someone visits the URL, run the function below
@app.route("/") #"/" is the home page 
def home():
    return render_template("index.html") #what the home function sends back to the browser

#Only run the following code if this file is being run directly
if __name__ == "__main__":
    app.run(debug=True) #Starts the application and turns on debug mode
