from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
application = Flask(__name__)

@application.route('/provision', methods=['POST', 'GET'])
def provision():

	target_node_ip = str(request.form['target-node-ip'])
        target_node_password = str(request.form['target-node-password'])
	base_image = str(request.form['image'])
	contrail_package_version = str(request.form['package'])
        contrail_package_build = str(request.form['build-number'])
	testbed_file = request.files['testbed-file'].read()

	print target_node_ip, target_node_password, base_image, contrail_package_version, contrail_package_build
        print "\n\n\n"
	
	localfile = open("testbed.py", "w")
	localfile.write(testbed_file)
	localfile.close()

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

        return render_template('login.html')
 
if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=9000)
