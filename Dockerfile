# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV API_HOST=0.0.0.0 
ENV API_PORT=5000 
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python3", "-m", "api.v1.app"]