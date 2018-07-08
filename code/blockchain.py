# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 19:09:31 2018

@author: Aman Ali Pogaku
"""

# Blockchain using Python
# Install Flask version 0.12.2 by using pip install Flask==0.12.2
# Install Postman HTTP client: https://www.getpostman.com/

# Importing libraries
import datetime  # since each block will have its own time
import hashlib  # to hash the block
import json  # encode the blocks before hashing
# Flask is used to create an object which will be the web-app
# jsonify is used to return the response of the requests
from flask import Flask, jsonify


# Part 1-building the blockchain class
class Blockchain:  # Helps to create blocks

    def __init__(self):  # Constructor method
        self.chain = []  # empty list. supposed to contain the list of blocks
        self.create_block(proof=1, previous_hash='0')
        # proof of work is initialised to 1 and previous hash is initialised to 0.
        # As hash is encoded we initialised it with single quotes
        # This is the genesis block

    def create_block(self, proof, previous_hash):  # this is used to create a block and append it to blockchain
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof, 'previous_hash': previous_hash}
        # 'index':chain+1 since we are creating a new block
        # 'timestamp': string because it will give no issues while using JSON.
        #  'proof': from proof of work function we pass proof as parameter
        # and that is what is equated to the key(proof)
        self.chain.append(block)  # add the blocks to the chain(list).
        return block  # return the parameters of the dictionary as it can be used to mine further blocks

    def get_previous_block(self):
        return self.chain[-1]
        # returns the last block in the chain.

    def proof_of_work(self, previous_proof):
        new_proof = 1

        # every nonce/proof of work must start with 1. It is then incremented to satisfy the target requirment
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            # we have '-' operation  because it is asymmetrical a-b!=b-a.
            # we are squaring it just to increase the difficulty
            # encode() is added so that sha256 accepts the encoded format. It adds 'b' to the result of a-b
            




