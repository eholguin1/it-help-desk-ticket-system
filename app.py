#Imports the Flask class from the Flask library
#Able for python to act as a web server/application
#request --> lets Python access information that a user submits through a form
from flask import Flask, render_template, request

#render_template allows Flask to load an HTML file

#Creates the Flask application
app = Flask(__name__) #storing variable named app
#__name__ --> tells Flask which Python module is running the application

#When someone visits the URL, run the function below
@app.route("/", methods=["GET","POST"]) #"/" is the home page 
                        #@app.route --> connects a URL to a python function
                        #GET --> the browser is requesting to view the page
                        #POST --> the browser is sending data to the server (submitted ticket)
def home():
    #return render_template("index.html") #what the home function sends back to the browser
    if request.method == "POST": #opens the website page, the condition is false, if they submit the form is true
        #request.method --> tells us which HTTP method was used
        #POST --> the method used when submitting the form
        name = request.form.get("name")
        email = request.form.get("email")
        issue = request.form.get("issue")
        category = request.form.get("category")
        priority = request.form.get("priority")

        return f"""
        <h1>Ticket Recieved!<h1>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Issue: {issue}</p>
        <p>Category: {category}</p>
        <p>Priority: {priority}</p>
        <a href="/">Submit another ticket</a>
        """
            #creates the HTML response that the browser displays after submission
        
    return render_template("index.html") #if the request method is not POST, show the form
#Only run the following code if this file is being run directly
if __name__ == "__main__":
    app.run(debug=True) #Starts the application and turns on debug mode
