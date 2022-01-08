from datetime import datetime, date
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
    username = db.Column(db.String(120), unique=True,
                         nullable=False, primary_key=True)
    password = db.Column(db.String(74), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class Prescription_info(db.Model):
    prescription_id = db.Column(
        db.String(50), nullable=False, primary_key=True)
    appointment_id = db.Column(db.String(15), db.ForeignKey(
        'appointment_info.appointment_id'), unique=True, nullable=False)
    prescription = db.Column(db.String(50), unique=True, nullable=False)
    start_treatment = db.Column(db.Date(), nullable=False)
    end_treatment = db.Column(db.Date(), nullable=False)
    diagnosis = db.Column(db.String(15), nullable=False)
    notes = db.Column(db.String(30), nullable=False)

    def __init__(self, prescription, prescription_id, start_treatment, end_treatment, diagnosis, notes, appointment_id):
        self.prescription = prescription
        self.prescription_id = prescription_id
        self.start_treatment = start_treatment
        self.end_treatment = end_treatment
        self.diagnosis = diagnosis
        self.notes = notes
        self.appointment_id = appointment_id


class Appointment_info(db.Model):
    appointment_id = db.Column(
        db.String(50), unique=True, nullable=False, primary_key=True)
    case_id = db.Column(db.String(50), db.ForeignKey(
        'case_info.case_id'), unique=True, nullable=False)
    appointment_date = db.Column(db.Date(), nullable=False)
    appointment_time = db.Column(db.DateTime(), nullable=False)

    def __init__(self, appointment_id, case_id, appointment_date, appointment_time):
        self.appointment_time = appointment_time
        self.appointment_id = appointment_id
        self.appointment_date = appointment_date
        self.case_id = case_id


class Case_info(db.Model):
    case_id = db.Column(db.String(15), primary_key=True)
    patient_id = db.Column(db.String(15), nullable=False)
    doctor_id = db.Column(db.String(15), nullable=False)

    def __init__(self, case_id, patient_id, doctor_id):
        self.case_id = case_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id


class User_info(db.Model):
    username = db.Column(db.String(120), unique=True,
                         nullable=False, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    dob = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    bloodgroup = db.Column(db.String(50))
    contactno = db.Column(db.String(50))
    city = db.Column(db.String(50))

    def __init__(self, username, role, firstname, lastname, dob, sex, bloodgroup, contactno, city):
        self.username = username
        self.role = role
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.sex = sex
        self.bloodgroup = bloodgroup
        self.contactno = contactno
        self.city = city
# @app.before_request
# def require_login():
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
    role = "Doctor"  # request.form.get('role')
    user = User.query.filter_by(username=username, role=role).first()
    if user is None:
        flash('Please Check your username', 'danger')
        return render_template('index.html')
    if bcrypt.checkpw(password.encode('UTF-8'), user.password.encode('UTF-8')):
        session['username'] = username
        session['role'] = role
        if role == 'Doctor':
            data = DocDash()
            return render_template('DocDash.html', data=data)
        elif role == 'Pharmacist':
            return render_template('PrescriptionPage.html')
        elif role == 'Reception':
            return render_template('AppointmentCase.html')

    else:
        flash('Username/Password is incorrect', 'danger')
        return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password').encode('UTF-8')
    role = "Doctor"  # request.form.get('role')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    dob = request.form.get('dob')
    sex = request.form.get('sex')
    bloodgroup = request.form.get('bloodgroup')
    contactno = request.form.get('contactno')
    city = request.form.get('city')
    user = User.query.filter_by(username=username, role=role).first()
    if user is not None:
        flash('User with same Username exists', 'danger')
        return redirect('/')
    hashed_password = bcrypt.hashpw(
        password, bcrypt.gensalt(14)).decode('UTF-8')
    user_info = User_info(username, role, firstname,
                          lastname, dob, sex, bloodgroup, contactno, city)
    user = User(username, hashed_password, role)
    print(user_info)
    db.session.add(user)
    db.session.add(user_info)
    try:
        db.session.commit()
        flash('Registered Successfully', 'success')
        return render_template('index.html', status='success')
    except IntegrityError:
        flash('Error in registration', 'danger')
    return render_template('index.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')


@app.route('/appointment')
def appointment():
    return render_template('AppointmentCase.html')


@app.route('/prescription', methods=['POST', 'GET'])
def prescription():
    if request.method == 'POST':
        patient_id = request.form.get('patient_id')


@app.route('/DocPage', methods=['POST', 'GET'])
def DocPage():
    if request.method == 'GET' and session['role'] == 'Doctor':
        appointment_id = request.args.get('appointment_id')
        case_id = request.args.get('case_id')
        session['appointment_id'] = appointment_id
        session['case_id'] = case_id
        return render_template('DocPage.html')
    elif request.method == 'POST' and session['role'] == 'Doctor':
        appointment_id = session['appointment_id']
        case_id = session['case_id']
        prescription_id = prescription_generator(appointment_id, case_id)
        notes = request.form.get('notes')
        prescription = request.form.get('prescription')
        start_treatment = request.form.get('startoftreatment')
        end_treatment = request.form.get('endoftreatment')
        diagnosis = ' '.join(map(str, request.form.getlist('diagnosis')))
        print(diagnosis)
        prescription_data = Prescription_info(
            prescription, prescription_id, start_treatment, end_treatment, diagnosis, notes, appointment_id)
        db.session.add(prescription_data)
        db.session.commit()
        return render_template('DocDash.html')
    else:
        return redirect('/')


def DocDash():
    doc_id = session['username']
    current_date = date.today()
    cases = db.session.execute(" SELECT * from appointment_info join (SELECT * from case_info join user_info on case_info.patient_id=user_info.username) AS A on appointment_info.case_id = A.case_id where appointment_date = '" +
                               str(current_date)+"' and doctor_id= '" + doc_id + "' order by appointment_time;")
    return cases


def appointment_generator(case_id, appointment_date, appointment_time):
    appointment_id = "V_"+case_id+str(appointment_date)+str(appointment_time)
    return appointment_id


def prescription_generator(appointment_id, case_id):
    prescription_id = "P_"+case_id+appointment_id
    return prescription_id


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
