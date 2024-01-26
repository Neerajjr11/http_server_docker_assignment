## To build
`docker buildx build --platform linux/amd64,linux/arm64 -t httpserver .`
## To run
`docker run -p 8080:8080 --memory 1500m --cpus 2.0 httpserver`
## Screenshots

![Alt text](image-1.png)

![Alt text](image.png)