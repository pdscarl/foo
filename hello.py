from flask import Flask, escape, request, render_template
from flask_pymongo import PyMongo

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    occupation = StringField('occupation', validators=[DataRequired()])
    language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

    
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dsjafkadkfjaknfknkabfjhbk78346592u3[])(*&^%$#ndf9hin983io'

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     #return f'Hello, {escape(name)}!'
#     return 'Hello, world!'


@app.route("/new")
def blah():
    pass


@app.route("/")
def home_page():
    #online_users = mongo.db.users.find({"online": True})
    online_users = mongo.db.users.find()
    #print ('online_users=', list(online_users))
    #online_users = mongo.db.users.find_one_or_404({"online": True})
    form = MyForm(request.form)
    
    return render_template(
        "index.html",
        online_users=online_users,
        form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
