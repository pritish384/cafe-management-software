from flask import Flask, render_template, request, redirect, url_for, Response
from db.database_config import *

app = Flask(__name__)

app.template_folder = 'pages'
app.static_folder = 'static'



@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('templates/index.html' , active_orders=active_orders)

@app.route('/orders')
def orders():
    return render_template('templates/orders.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/error.html' , error="404 Page not found" ,solution="Avoid visiting this page, as it does not exist.")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('templates/error.html' , error="500 Internal Server Error" , solution="You did something wrong and the server is not able to handle it or the server is down")

@app.errorhandler(403)
def forbidden(e):
    return render_template('templates/error.html' , error="403 Forbidden" , solution="You are not allowed to access this page")

@app.errorhandler(400)
def bad_request(e):
    return render_template('templates/error.html' , error="400 Bad Request" , solution="You did something wrong and the server is not able to handle it")

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('templates/error.html' , error="405 Method Not Allowed" , solution="You did something wrong and the server is not able to handle it")


if __name__ == '__main__':
    app.run(debug=True , host="0.0.0.0" , port=80)