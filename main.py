from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    my_list=[{
    "name":"Alex",
    "age":"42"
    },
    {"name":"Serg",
    "age":"39"
    }]
    return render_template('index.html', name=name, my_list=my_list)
