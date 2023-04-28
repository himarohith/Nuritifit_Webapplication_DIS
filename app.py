from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'nutrifit'

db = SQLAlchemy(app)


class NutrifitUser (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/nutrition")
def nutrition():
    return render_template("nutrition.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

@app.route("/fitness")
def fitness():
    return render_template("fitness.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        repeat_password = request.form['psw-repeat']
        print(email,password,repeat_password)
        if password==repeat_password:
            users = NutrifitUser.query.all()
            for user1 in users:
                print(user1.email,user1.password)
            check_user = NutrifitUser.query.filter_by(email=email).first()
            if check_user is None:
                user = NutrifitUser(email=email, password=password)
                print(user.email)
                db.session.add(user)
                db.session.commit()
                print('User SignedUp Successfully!', 'success')
                return redirect(url_for('home'))
            else:
                error='User already signed up'
                return render_template('signup.html', error=error)
        else:
            error='Password Mismatch...Try Again'
            return render_template('signup.html', error=error)


    return render_template("signup.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)