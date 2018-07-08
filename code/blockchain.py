# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 19:09:31 2018

@author: Aman Ali Pogaku
"""

# Blockchain using Python
# Install Flask version 0.12.2 by using pip install Flask==0.12.2
# Install Postman HTTP client: https://www.getpostman.com/ 

#Importing libraries
import datetime #since each block will have its own time
import hashlib #to hash the block
import json #encode the blocks before hashing
#Flask is used to create an object which will be the web-app 
#jsonify is used to return the response of the requests
from flask import Flask, jsonify 

# Part 1-building the blockchain class

class Blockchain:
    
    def __init__(self): # Constructor method
        self.chain = [] #empty list. supposed to contain the list of blocks
        self.create_block(proof = 1, previous_hash ='0')
        #proof of work is initialised to 1(a number) and previous hash is initialised to 0.
        #As hash is encoded we initialised it with single quotes.
        
        
