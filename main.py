import datetime
import requests
from bs4 import BeautifulSoup
import re
import time
import json
from flask import Flask, render_template, url_for, redirect, flash
from forms import RD2LForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4e895d495ab39301b88457d72968508'

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/rd2l', methods=['GET','POST'])
def scout():
    form = RD2LForm()
    if form.validate_on_submit():
        with open('teams.json','r', encoding='utf-8') as teams_file:
            team_json = json.load(teams_file)
            for team_data in team_json:
                if team_data['header'] == form.team_select.data:
                    return render_template('rd2l.html', form=form, players=team_data['players'], matches=team_data['matches'], header=team_data['header'], heroes=team_data['heroes'] )
    else:
        return render_template('rd2l.html', form=form)

@app.route('/me', methods=['GET', 'POST'])
def me():
	return render_template('me.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=False, ssl_context='adhoc')
