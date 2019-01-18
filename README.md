# Purpose
Students just learning to code often struggle identifying and debugging errors. It can be hard to decipher the relevant parts of an error message or parse through the stack trace. They might not know how to articulate a question around the issue because they don't have the technical vocabulary yet. This app is designed to be used actively in the classroom to encourage students to identify the crucial portion of the error message, determine what part of code is responsible for the error, and then collaborate with others to resolve the issue.

## Getting Started

This project is built with Django and MySQL. The script for the database and tables creation, as well as some boiler plate data, is available in setup.sql.

### Prerequisites

Dependencies are listed in requirements.txt. To install all the dependencies for this project, create a virtual environment with Python 3.6 and run the following command to install dependencies:
```
pip install -r requirements.txt
```

### Running the Application

To run the application (localhost:8000):
```
python manage.py runserver
```

## To Do
- gamification
- consider any modifications needed to integrate other languages?
- leaderboard functionality
- other gamified components to increase adoption/participation
- utilize a front-end framework
- potentially convert to NoSQL db
- notifications for unread solutions
- filter functionality?

### Previous Iteration & Lessons Learned
Stack Overflow clone: [https://github.com/tehtertot/DojoQATest]
(Built with C# and Angular)
- difficult to articulate their question into coherent words; words alone are not useful/practical
- when running into an error, students struggle with finding the relevant error message
- how to make the tool useful enough that students turn to it consistently as a helpful resource, without just giving away answers to assignments?