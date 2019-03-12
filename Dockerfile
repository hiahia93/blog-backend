FROM python:3.7-slim

WORKDIR /app
COPY . .
RUN mkdir -p /var/log/blogback && touch /var/log/blogback/server.log
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD [ "python", "./manage.py" ]
