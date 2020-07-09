# API GRAPHQL FOR OPTICAL CHARACTER RECOGNITION

## Requirements
You need to have installed:
- Docker 
- docker-compose.

## Create docker images
First you need to create the docker images
```
docker-compose build
```

## Run the docker images
To run the images with docker use the following sentence.
```
docker-compose up -d
```

## Keep in mind
- The project will run in the port 80.
- The endpoint for graphql is: /graphql


## Execute an graphql query
- Enter to localhost/graphql
- Create the query you want to use.

## Query example
You can change the link of the image for another one in the internet.
```
{
  predict(link:"https://upload.wikimedia.org/wikipedia/commons/0/0c/600px-Pare_svg.png")
}
```
