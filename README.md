# Pull the docker image

        docker pull savvythru/contrail-provisioning-tool

# Run container & map the exposed conatiner port to host port
        
        docker run -p 10001:10001 -itd savvythru/contrail-provisioning-tool
