# qrd-api

Flask API for mercadopago's Dynamic EMVco QR Code Generation

```
$cd ix-api-qrd
```

```
$source env/bin/activate
```

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
"tittle":"TuNegocio",
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
