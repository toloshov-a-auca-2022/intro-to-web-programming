#hello world
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)


#Greeting
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {escape(name.capitalize())}!</h1>"

# 5. Template Rendering with Jinja2
#
# Why You Need It:
# 	•	Shows how to separate logic from presentation using templates.
# 	•	Introduces Jinja2 syntax for loops and variable substitution.

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ["Adilet", "Aziret", "Fara"]
    return render_template('index_lab1.html', names=names, title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)