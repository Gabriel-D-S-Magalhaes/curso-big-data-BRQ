#!/bin/bash

echo "***   Construindo Docker Images   ***"
echo "Dockerfile-consumer..."
docker build -t kafka_consumer --file Dockerfile-consumer .

echo "Dockerfile-producer..."
docker build -t kafka_producer --file Dockerfile-producer .