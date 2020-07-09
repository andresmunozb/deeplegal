# API GRAPHQL FOR OPTICAL CHARACTER RECOGNITION
## Demo
See [Live demo](34.95.183.94).

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


## Execute an graphql query
- Enter to localhost
- Create the query you want to use.

## Query example
You can change the link of the image for another one in the internet.
```
{
  predict(link:"https://upload.wikimedia.org/wikipedia/commons/0/0c/600px-Pare_svg.png")
}
```
