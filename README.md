# Test Backend

<b>Chalange Luhn Algorithm.</b> For this chalange we want you build an API REST to checkout if a credicard number is valid. For this purpose, please note the following:

##### <li>The service must receive a string with creditcard number.</li>
##### <li>The creditcard number may contain spaces.</li>
##### <li>he service must return franchise name to creditcard belong</li>
##### <li>he service must be portable and easy to use in any SO. For this you must use Dockerd.</li>


## Simple API REST

Simple HTTP API for check credicard numbers.

## Files

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/card`


## Setup

```
$ pip3 install -r requirements.txt
```

## Run from concole

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Run from docker

```
$ docker-compose up
```

## Routes

- `GET /api/v1/card`: returns the card franchise name of the API

## Consult any number

- `/api/v1/card?card_number=xxx xxxx xxxx xxxx` Acept blank spaces or 
- `/api/v1/card?card_number=xxxxxxxxxxxxxxx` Not spaces