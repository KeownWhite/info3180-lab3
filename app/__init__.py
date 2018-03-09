from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '6c606d3dafa2eb'
app.config['MAIL_PASSWORD'] = 'a23a2de709279a'

mail = Mail(app)
from app import views
