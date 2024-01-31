FROM ubuntu:latest
LABEL authors="gabis"

ENTRYPOINT ["top", "-b"]