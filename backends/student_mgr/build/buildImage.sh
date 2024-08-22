#!/bin/bash
scriptDir=$(dirname $0)

IMAGE_NAME=jbcodeforce/student-mgr
#IMAGE_NAME=athenadecisionsystems/athena-owl-backend

if [[ $# -eq 2 ]]
then
  TAG=$1
  OS=$2
else
  TAG=latest
  OS=linux
fi

cd $scriptDir/..
if  [[ $OS -eq "linux" ]]
then
  docker build -f Dockerfile --platform linux/amd64 -t  ${IMAGE_NAME}:${TAG} src
else
  docker build -f Dockerfile  -t  ${IMAGE_NAME}:${TAG} src
fi

docker tag  ${IMAGE_NAME}:${TAG}   ${IMAGE_NAME}:latest
