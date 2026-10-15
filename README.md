# IT Help Desk Ticket System

A web-based IT Help Desk Ticket System built with Python, Flask, SQLite, HTML, and CSS. This project simulates a basic IT support workflow by allowing users to submit support tickets and track their progress through a dashboard.

## Features

- **Ticket Submission:** Submit support requests with a name, email, issue description, category, and priority.
- **Ticket Dashboard:** View all submitted tickets in one place.
- **Ticket Details:** Open individual tickets to view their information.
- **Status Management:** Update tickets to Open, In Progress, or Closed.
- **Dashboard Summary:** View the number of tickets in each status.
- **Database Storage:** Store ticket information in a SQLite database.
- **Web Interface:** Use an HTML interface styled with CSS.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
it-help-desk-ticket-system/
├── app.py
├── templates/
│   ├── index.html
│   ├── tickets.html
│   └── ticket_detail.html
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/eholguin1/it-help-desk-ticket-system.git
cd it-help-desk-ticket-system
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

The application initializes its SQLite database locally when it starts.

## What I Learned

- Building a web application using Flask and Python
- Creating and querying a SQLite database
- Using SQL to retrieve, count, and update records
- Connecting HTML templates to Python using Flask and Jinja
- Handling form submissions and HTTP requests
- Tracking project changes with Git and GitHub

## Future Improvements

- Add ticket search and filtering
- Assign tickets to support technicians
- Record ticket creation timestamps
- Add input validation and error handling
- Improve the interface for mobile devices
