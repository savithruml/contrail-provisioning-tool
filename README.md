## Pull the docker image

        docker pull savvythru/contrail-provisioning-tool

## Run & map the exposed container port to host port
        
        docker run -p 10001:10001 -itd --name contrail-provisioning-tool savvythru/contrail-provisioning-tool
