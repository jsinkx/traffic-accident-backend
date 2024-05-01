# Create .env by args
FROM alpine AS env_by_args
ARG SERVER_HOST
ARG SERVER_PORT
ARG IS_PROD
WORKDIR /traffic-accident-backend-ml
RUN echo "SERVER_HOST=$SERVER_HOST" > .env
RUN echo "SERVER_PORT=$SERVER_PORT" >> .env
RUN echo "IS_PROD=$IS_PROD" >> .env

# Select .env from project or craeted by args
FROM alpine as env
WORKDIR /traffic-accident-backend-ml
COPY --from=env_by_args /traffic-accident-backend-ml/.env .
COPY *.env .env

# Build final backend ml app
FROM python:3.10-slim-buster as runner
WORKDIR /traffic-accident-backend-ml
COPY --from=env /traffic-accident-backend-ml/.env .env
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
