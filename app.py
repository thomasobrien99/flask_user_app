from flask import Flask, render_template, url_for, redirect, flash
from forms import NewUserForm
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'shhhh'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_user_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CsrfProtect(app)

#########################
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, nullable = False)
	password = db.Column(db.Text, nullable = False)

	def __init__(self, username, password):
		self.username = username;
		self.password = password;

##########################

@app.route('/')
@app.route('/users')
def index_user():
	users = User.query.all()
	return render_template('index.html', users=users)

@app.route('/', methods=["POST"])
def create_user():
	form = NewUserForm()
	if (form.validate_on_submit()):
		user = User(form.username.data, form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("You created a new user!")
	return redirect(url_for('index_user'))
@app.route('/users/new')
def new_user():
	form = NewUserForm()
	return render_template('new.html', form=form)


if(__name__ == '__main__'):
	app.run(debug=True, port=3001)