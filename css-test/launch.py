from flask import Flask, flash, redirect, render_template, request, session, abort, Response
import os, subprocess
from shelljob import proc


application = Flask(__name__)

@application.route('/provision', methods=['POST', 'GET'])
def provision():
	
	target_node_ip = str(request.form['target-ip'])
	target_node_password = str(request.form['target-password'])
	base_image = str(request.form['image'])
	contrail_package_version = str(request.form['package']).split('contrail-')[1]
	contrail_package_release = str(request.form['release'])
	contrail_package_build = str(request.form['build'])
	testbed_file = request.files['testbed-file'].read()

	localfile = open("testbed.py", "w")
	localfile.write(testbed_file)
	localfile.close()
	
	if request.form["commit"] == "Provision":
		def generate():
			for line in (subprocess.check_output("ssh root@{4} wget http://10.84.5.120/github-build/R{0}/{1}/{2}/{3}/artifacts/contrail-cloud-docker_4.0.0.0-{1}-{3}.tgz && \
		         ssh root@{4} wget http://10.84.5.120/github-build/R{0}/{1}/{2}/{3}/artifacts/contrail-server-manager-installer_4.0.0.0-{1}~{3}_all.deb && \
		         ssh root@{4} truncate -s 0 /etc/apt/sources.list && \
		         scp testbed.py root@{4}:~/ && \
		         ssh root@{4} dpkg -i contrail-server-manager*deb". \
		         format(contrail_package_version,contrail_package_build,base_image,contrail_package_release,target_node_ip), shell=True)).splitlines():
					 yield line + '\n'
					 
		os.remove("testbed.py")
		
		return Response( generate(), mimetype= 'text/html' )


@application.route('/login', methods=['POST', 'GET'])
def login():
	
	usr_name = str(request.form['username'])
	usr_pass = str(request.form['password'])
	
	if usr_name == 'admin' and usr_pass == 'c0ntrail123':
		return render_template('provision.html')
	else:
		return render_template('login-fail.html')


@application.route('/')
def main():

        return render_template('login.html')

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=9000)
