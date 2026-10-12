#Imports the Flask class from the Flask library
#Able for python to act as a web server/application
#request --> lets Python access information that a user submits through a form
from flask import Flask, redirect, render_template, request
        #render_template allows Flask to load an HTML file
import sqlite3 #built in python library that lets you work with SQLite databases    
        #stores data in a file on your computer, so you do not have to use a separate datebase server


#Creates the Flask application
app = Flask(__name__) #storing variable named app
#__name__ --> tells Flask which Python module is running the application

#Creates the database and tickets table if they dont exist
def init_db():
    connection = sqlite3.connect("tickets.db")
        #opens a connection an SQLIte database, if the file doesnt exist, it will be created
        #(communicate with the database)
    
    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            issue TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open'
        )
    """)

    #add the status column to an existing table if it missing
    columns = connection.execute("PRAGMA table_info(tickets)").fetchall()
    column_names = [column[1] for column in columns]
    if "status" not in column_names:
        connection.execute("ALTER TABLE tickets ADD COLUMN status TEXT NOT NULL DEFAULT 'Open'")

    connection.commit() #saves the changes made to through the database connection
    connection.close() #closes the connection to the database
    

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

        #connects to the database
        connection = sqlite3.connect("tickets.db")
        #inserts the ticket information into the table
        connection.execute("""
            INSERT INTO tickets(name, email, issue, category, priority) VALUES (?, ?, ?, ?, ?)
        """, (name, email, issue, category, priority))
            #? are placeholders for the values provided in the tuple (name, email, issue, category, priority)
        #saves the ticket to the database
        connection.commit()
        #closes the database connection
        connection.close()
        #shows a comfirmation page
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

#Displays all saved tickets
@app.route("/tickets")
def tickets():
    #connects to the database
    connection = sqlite3.connect("tickets.db")
    #retrieves all tickets from the database
    tickets = connection.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
                                                #ORDER BY id DESC --> shows the newsest ticket first
                                                #.fetchall() --> collects the results into a python list
    #closes the database connection
    connection.close()
    #sneds the tickets to the HTML page
    return render_template("tickets.html", tickets=tickets)

#Updates the status of a ticket
@app.route("/update_status/<int:ticket_id>", methods=["POST"])
    # /update_status/ -->> is the beginning of the UR:L
    # <int:ticket_id> --> the URL must contain a ticket ID represented as an integer
    # methods=["POST"] --> this route accpets POST requests, whic are commonly used when submitting a form to change data
    #ticket_id --> the ID of the ticket to update
def update_status(ticket_id):
    new_status = request.form.get("status") #selecting the status selected
    if new_status not in ["Open", "In Progress", "Closed"]:
        return "Invalid status",400 #400 is the HTTP status code meaning the request is invalid

    connection = sqlite3.connect("tickets.db") #opens a connection to the SQLite database
    connection.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))

    connection.commit() #saves the changes made to the database
    connection.close() #closes the connection to the database

    return redirect("/tickets") #redirects the user back to the tickets page after updating the status

#Only run the following code if this file is being run directly
if __name__ == "__main__":
    init_db()
    app.run(debug=True) #Starts the application and turns on debug mode
