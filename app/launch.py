from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import logging
 
application = Flask(__name__)


@application.route('/login', methods=['POST', 'GET'])
def login():
	
	usr_name = str(request.form['username'])
	usr_pass = str(request.form['password'])
	
	if usr_name == 'admin' and usr_pass == 'c0ntrail123':
		return render_template('provision.html')
	else:
		return render_template('loginfail.html')

@application.route('/')
def main():

        logging.basicConfig(level=logging.INFO, filename='status.log',
                                             format='%(asctime)s %(message)s')

        return render_template('login.html')
 
if __name__ == "__main__":
    application.run(debug=True,host='0.0.0.0', port=8090)
