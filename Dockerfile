# Partindo da imagem Ubuntu
FROM ubuntu:latest

# RUN serve para rodar um comando shell script na criação da imagem Docker
RUN apt-get update && apt-get install python3-pip -y \ 
    && apt-get install nano -y

RUN mkdir /nova-pasta

# Ao iniciar o container, o mesmo apresenta o console 
ENTRYPOINT ["/bin/bash"]

# docker build -t <name> . 
#
# Usando "volumes"
# docker run --name <name_container> -it -v volume:/meu-volume <Docker Image>
#
# ${PWD}/<Pasta do Host>:<Pasta dentro do Container> 