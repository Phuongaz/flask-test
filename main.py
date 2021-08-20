from flask import Flask, render_template, url_for, request, redirect
from query import status
import asyncio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'test' or request.form['password'] != 'test':
            error = 'Login attempt failed! Your username or password is incorrect!'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/home')
def home():
    result = None
    port = 19132
    if request.method == 'POST':
        ipaddress = request.form['host']
        port = int(request.form['port'])
        if ipaddress != "":
            result = asyncio.run(status(ipaddress, port))
            print(result)

    return render_template("home.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
