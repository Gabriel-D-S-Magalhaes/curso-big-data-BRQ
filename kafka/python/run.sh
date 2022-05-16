#!/bin/bash

echo "***   Executando Docker Containers   ***"
echo "Dockerfile-consumer..."
docker run --rm -d --name kafka_consumer --network single-node_default kafka_consumer

echo "Dockerfile-producer..."
docker run --rm -d --name kafka_producer --network single-node_default kafka_producer