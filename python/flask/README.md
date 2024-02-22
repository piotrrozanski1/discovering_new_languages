# Flask
Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.

### WSGI
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development. WSGI is the specification of a common interface between web servers and web applications.

### Werkzeug
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions. This enables a web frame to be built on it. The Flask framework uses Werkzeg as one of its bases.

### jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a specific data source to render a dynamic web page.

### Microframework
Flask is often referred to as a microframework. It is designed to keep the core of the application simple and scalable.

Instead of an abstraction layer for database support, Flask supports extensions to add such capabilities to the application.

[source](hhttps://pythonbasics.org/what-is-flask-python/)

### Virtual env additional libraries
#### Pipenv
Pipenv is a Python virtual env management tool \
https://pipenv.pypa.io/en/latest/ \
Command: `pip install pipenv`

Configure pipenv into Intellij: https://www.jetbrains.com/help/idea/pipenv.html#install-pipenv

### Useful flask command
- **flask db init** - create database schema
- **flask db migrate -m "Initial migration."** - create database schema
- **flask db upgrade** - the command is used to upgrade the database schema to the latest version. This is done by comparing the current schema to the latest schema and applying any changes that are necessary.
- **flask db downgrade** - the command will automatically detect the latest version of the schema and apply any changes that are necessary to downgrade the schema to the specified version. If there are no changes to be made, the command will simply return a message saying that the database is already at the specified version.

### Links:
- https://flask.palletsprojects.com/ - Flask project website


