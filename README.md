# STEPS

### Pull the docker image

        docker pull savvythru/contrail-provisioning-tool

### Run & map the exposed container port to host port
        
        docker run -p 10001:10001 -itd --name contrail-provisioning-tool savvythru/contrail-provisioning-tool

### Open Web-browser & navigate to localhost:10001 to open the application

        http://127.0.0.1:10001

# SCREENSHOTS

### Login<br /><br />![Login](https://github.com/savithruml/contrail-provisioning-tool/blob/master/screenshots/login.png "Login")

### Provision<br /><br />![Provision](https://github.com/savithruml/contrail-provisioning-tool/blob/master/screenshots/provision_empty.png "Provision")

### Provision Params<br /><br />![Provision Params](https://github.com/savithruml/contrail-provisioning-tool/blob/master/screenshots/provision_data.png "Provision Params")
