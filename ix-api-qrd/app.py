from flask import Flask, request

import binascii
import crc16
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/qr',methods=['POST'])
def generate_qr():
    data = request.get_json()
    string = read_string(data)
    checksum= crc(read_string(data).encode('utf-8'))
    qr_string = string + checksum
    response = {
      "qr_string":qr_string,
      "crc": checksum
    
    }
    return response,201
@app.route('/checksum',methods=['POST'])
def generate_crc():
    data = request.get_json()["string"]
    checksum= crc(str(data).encode('utf-8'))
    response = {
      
      "crc": checksum
    
    }
    return response,201

def read_string(data):

  collector = data['collector']
  transaction_amount=data['transaction_amount']
  description=data['description']
  city=data['city']
  country=data['country']
  external_reference=data['external_reference']
  tittle=data['title']
  external_id=data['external_id']


  ID00= '000201'
  ID01='010212'
  ID43 = '43' + str(12 + 16 + 1+ len(str(collector)))
  ID4300='0016com.mercadolibre'
  ID4302='02011'
  ID4303='03' +zero_left(len(str(collector)))+ str(collector)
  ID52='52045206'
  ID53='5303032'
  ID54='54'+zero_left(len(str(transaction_amount)))+str(transaction_amount)
  ID58='5802'+country
  ID59='59'+ zero_left(len(tittle)) +tittle
  ID60='60'+zero_left(len(city))+city
  ID62='62'+str(len(external_reference) + len(external_id) + len(description) +12)
  ID6205='05'+zero_left(len(external_reference))+external_reference
  ID6207='07'+zero_left(len(external_id))+external_id
  ID6208='08'+zero_left(len(description))+description
  ID63='6304'
  return ID00+ID01+ID43+ID4300+ID4302+ID4303+ID52+ID53+ID54+ID58+ID59+ID60+ID62+ID6205+ID6207+ID6208+ID63

def zero_left(number):
  if number <10:
    return ('0'+str(number))
  else:
    return (str(number))

def crc(string):
    hex_qr= string.hex()
    byte_seq = binascii.unhexlify(hex_qr)
    crc = crc16.crc16xmodem(byte_seq, 0xffff)
    return '{:04X}'.format(crc & 0xffff)

if __name__ == '__main__':
    app.run()
