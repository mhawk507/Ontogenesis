from flask import Flask, render_template, request, jsonify, send_from_directory, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from sqlalchemy.exc import IntegrityError
import enum
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xzhopgnzfqvvjm:07134b270fcbb63d1a6806b4827f546413ab403707ddb703130542f59260f6b8@ec2-34-232-191-133.compute-1.amazonaws.com:5432/dce6b26bnbtlp6'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(74), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


#@app.before_request
#def require_login():
#    allowed_route = ['login', 'register', 'static', '']
#    if request.endpoint not in allowed_route and 'email' not in session:
#        return redirect('/')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    user = User.query.filter_by(username=username, role=role).first()
    if user is None:
        flash('Please Check your username', 'danger')
        return render_template('index.html')
    if bcrypt.checkpw(password, user.password.encode('UTF-8')):
        session['username'] = username
        print("USER LOGGED IN")
        #return render_template('home.html')
    else:
        flash('Username/Password is incorrect', 'danger')
        return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    user = User.query.filter_by(username=username, role=role).first()
    if user is not None:
        flash('User with same Username exists', 'danger')
        return redirect('/signup')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(14)).decode('UTF-8')
    user = User(username, hashed_password)
    db.session.add(user)
    try:
        db.session.commit()
        flash('Registered Successfully', 'success')
        return render_template('home.html', status='success')
    except IntegrityError:
        flash('Error in registration', 'danger')
    return render_template('register_user.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
