#!/usr/bin/python
# coding:utf-8

# Flask er et micro web framework til python. Det bliver brugt mange steder i
# produktion fordi det er let og minimalt. Mange bruger det med jinja2
# templates og SQLAlchemy. Det vil sige man stykker selv sine komponenter
# sammen.


# pip install flask

from flask import Flask
from jinja2 import Template

app = Flask(__name__)

@app.route('/hello/<name>') # denne her router requesten til den rigtige funktion
def hello_world(name):

    template = Template("""
                        <!DOCTYPE html>
                        <html lang="da">
                        <head>
                        <title>HELLO</title>
                        <meta charset="utf-8" />
                        </head>
                        <body>
                        <h1> HELLO {{name}} </h1>
                        </body>
                        """)
    return template.render(name=name)

# start serveren 
app.run(debug=True)

# prøv http://localhost:5000/hello/lars
# prøv http://localhost:5000/hello/ulrik

