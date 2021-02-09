#!/bin/bash -xe
# set container name
CONTAINER="${USER}_admingrasshopper_vm"
# using shell
START_SHELL="sh"

# define image name
IMAGE_NAME=${USER}_admingrasshopper_image
# set docker image(from local)
IMAGE=${IMAGE_NAME}:latest

IMAGE_CHECK=`docker image ls -q $IMAGE_NAME`

if ! [ -n "$IMAGE_CHECK" ];then
    echo "no image existing, building the image ${IMAGE_NAME}"
    # build docker with dockerfile
    docker build -t $IMAGE_NAME .
else
    echo "image ${IMAGE_NAME} found!"
fi

# test if the container is running, if running, HASH is true
HASH=`docker ps -q -f name=$CONTAINER`
# test if the container is stopped, if stopped, HASH_STOPPED is true
HASH_STOPPED=`docker ps -qa -f name=$CONTAINER`


if [ -n "$HASH" ];then
    echo "founding existing running container $CONTAINER, proceeed to exec another shell"
    # restart the docker compose and execute it in shell
    # docker-compose restart
    docker exec -it $HASH $START_SHELL
elif [ -n "$HASH_STOPPED" ];then
    echo "founding existing stopped container $CONTAINER, proceeed to start"
    # docker-compose restart--entrypoint
    docker start --attach -i $HASH_STOPPED
    docker exec -it $HASH_STOPPED $START_SHELL
else
    echo "existing container not found, createing a new one, named $CONTAINER"
    # login to aws
    # aws ecr get-login --registry-ids 774915305292 --region=us-west-2 --no-include-email | sudo -E bash
    # pull with compose yaml file
    # docker-compose pull
    # run on these ports
    docker run --rm -it -p 8080:8080 -p 9229:9229 -p 9000:9000 --name=$CONTAINER $IMAGE
fi
echo "see you, use 'docker rm ${CONTAINER}' to kill the vm if you want a fresh env next time"
echo "see you, use 'docker-compose down' to kill the mongodb/mysql if you want a fresh env next time"
