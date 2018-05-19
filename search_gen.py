import json
import hashlib
import time
from datetime import datetime

def calculate_hash(block):
    block_string = json.dumps(block).encode()
    return hashlib.sha256(block_string).hexdigest()

def mine(args):
    size = 4
    nonce = 0
    while True:
        block = {
            'timestamp':datetime.now().timestamp(),
            'host':args['host'],
            'data':args['data'],
            'previous_hash':args['previous_hash'],
            'nonce':nonce
            }

        hash_block = calculate_hash(block)

        if hash_block[:size] == "0"*size:
            break

        nonce += 1

    return hash_block

args = {
    'host': "http://localhost:114514",
    'data': "Ground Zero",
    'previous_hash': hashlib.sha256(bytes('0', 'utf8')).hexdigest()
    }

print(mine(args))
