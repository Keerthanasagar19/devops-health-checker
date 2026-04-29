FROM ubuntu:latest

RUN apt update && apt install -y procps

COPY health.sh /health.sh

RUN chmod +x /health.sh

CMD ["/health.sh"]
