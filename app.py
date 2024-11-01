from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
import json_logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telegram_nicks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Настройка логирования
logger = logging.getLogger()
logHandler = logging.FileHandler('.venv/logs.json')
formatter = json_logging.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

class TelegramNick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    nicks = TelegramNick.query.all()
    logger.info('Home page accessed')
    return render_template('index.html', nicks=nicks)

@app.route('/add', methods=['POST'])
def add_nick():
    nick = request.form['nick']
    new_nick = TelegramNick(nick=nick)
    db.session.add(new_nick)
    db.session.commit()
    logger.info(f'New Telegram nick added: {nick}')
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)