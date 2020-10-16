
[![python](https://img.shields.io/badge/python-v3.7.X-green.svg)](https://www.python.org/)
[![pip](https://img.shields.io/badge/pip-v10.0.X-yellow.svg)](https://pypi.org/project/pip/)
[![virtualenv](https://img.shields.io/badge/virtualenv-v15.1.X-red.svg)](https://virtualenv.pypa.io/en/stable/)

# qrd-api

Flask API for mercadopago's Dynamic EMVco QR Code Generation

## Installation
1. Open de folder
```
$cd ix-api-qrd
```
2.Activate the virtual environment:
```
$source env/bin/activate
```
3.Run the flask app:
```
$python3 app.py
```

# Methods

## Dynamic QR Code string generation

```
curl --location --request POST 'http://127.0.0.1:5000/qr' \
--header 'Content-Type: application/json' \
--data-raw '{
"collector":446566691,
"transaction_amount":5.0,
"description":"Bebida",
"city":"Buenos Aires",
"country":"AR",
"title":"TuNegocio",
"external_reference":"ticket-123",
"external_id":"CAJA001"
}'
```

## Checksum field CRC-16 HEX generator

```
curl --location --request POST 'http://127.0.0.1:5000/checksum' \
--header 'Content-Type: application/json' \
--data-raw '{
"string":"00020101021243380016com.mercadolibre02011030944656669152045206530303254035.05802AR5909TuNegocio6012Buenos Aires62350510ticket-1230707CAJA0010806Bebida6304"
}'
```

## Oficial documentation

https://www.mercadopago.com.ar/developers/es/guides/in-person-payments/qr-code/qr-dinamic/qr-dinamic-part-b/

## References

https://crccalc.com/
