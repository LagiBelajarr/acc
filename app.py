from flask import Flask, render_template, request, redirect, url_for, session
import secrets
import mysql.connector

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="user",
    password=""
)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/aksi_login', methods=["POST"])
def aksi_login():
    cursor = mydb.cursor()
    query = ("SELECT * FROM project x WHERE username = %s AND password = %s")
    data = (request.form['username'], request.form['password'])
    cursor.execute(query, data)
    value = cursor.fetchone()

    if value:
        session["user"] = request.form['username']
        return redirect(url_for('admin'))
    else:
        return "Salah !!!"
