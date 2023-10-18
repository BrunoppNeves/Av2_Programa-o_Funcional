# Fiz a implementação da questão 2
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__, template_folder='templates_folder')
users = lambda: {line.strip().split(":")[0]: line.strip().split(":")[1] for line in open("users.txt", "r")}
register_user = lambda: (
    open("users.txt", "a").write(f"{request.form['username']}:{request.form['password']}\n")
    if request.method == 'POST'
    else render_template('index.html')
) and redirect(url_for('index'))

welcome = lambda : f'WELCOME {request.form["username"]}!!'
wrong = lambda : 'WRONG PASSWORD!!!!'
invalid = lambda : 'User does not exist!'
password_matches = lambda dic: dic.get(request.form["username"]) == request.form["password"]
check_password = lambda : welcome () if password_matches (users ()) else wrong ()
check_if_user_exists = lambda : check_password () if f'{request.form["username"]}' in users () else invalid ()
reqresp = lambda : check_if_user_exists () if request.method == 'POST' else render_template('index.html')
app.add_url_rule('/index/', 'index', reqresp, methods=['GET', 'POST'])
app.add_url_rule('/register/', 'register', register_user, methods=['GET','POST'])
app.run(host='0.0.0.0', port=8080)