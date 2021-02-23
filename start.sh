#!/bin/bash

if [ ! -f config.yaml ]
then
    cp src/config.yaml ./
fi

docker-compose down && docker-compose up --build -d
