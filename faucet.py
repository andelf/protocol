import requests



URL = 'https://www.trongrid.io/api/get-shasta-trx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'origin': 'https://www.trongrid.io',
    'referer': 'https://www.trongrid.io/faucet',

}

addr = 'TQHAvs2ZFTbsd93ycTfw1Wuf1e4WsPZWCp'


addrs = """
TCLBgkbfVkJroVBJVqBEsxtPNQEQMTQCLQ
TBvJUBXorwBPzqvV38vjDgegj5Eh6g2Tsq
TJRabPrwbZy45sbavfcjinPJC18kjpRTv8
TLfuw4tRywtxCusvTudbjf7PbcXjfe7qrw
TWa5cxQFesyCQUm17usvHrVkKce6rMCV4H
TVwvLcXD1WTK2gegh7tZ5Fxocfo8GttHgL
TRsbuxREXKJKonexpejWhacE4sYHt1BSHV
TJzXt1sZautjqXnpjQT4xSCBHNSYgBkDr3
TBCtDueBN3LeyrJA8bKWetb5s3JfePK19X
TP5gxuZj6Pj5ciM6B8fMJwytZwWAJ66sat
TNTU3x2BLuJg3MQCnk6hne43NpgphMK2NJ
TXBUwpDrRYfSH3MNha5amQ1SkprDBgRhpd
TRJworXfT4HwMx9W9mE26KTzKdMrJTDwHy
TGQgfK497YXmjdgvun9Bg5Zu3xE15v17cu
"""

for addr in filter(None, addrs.split()):
    print(addr)
    payload = {
        'address': addr,
        'search': '',
    }
    resp = requests.post(URL, json=payload, headers=headers)

    print(resp.json())

# {'status': 401, 'message': 'Your IP reached its daily limit, please try tomorrow in UTC time.'}