from datetime import datetime
import hashlib as h
import numpy as np


def proof_of_workx(old_param = np.random.randint(0, 10), validator = '01') :
	new_param = 0
	valid_params = False
	while valid_params is False :
		guess = (str(old_param) + str(new_param)).encode()
		hexdigest = h.sha256(guess).hexdigest()
		print (hexdigest)
		if hexdigest[:2] == validator :
			valid_params = True
		new_param += 1
	return old_param, new_param

#a, b = proof_of_work()

#print (a, b)

"""mini self-contained blockchain demonstrating blockchain mechanics"""

"""mini self-contained blockchain demonstrating blockchain mechanics"""

class Block :

    """Class for creating blocks"""

    def __init__(self, index, timestamp, nonce, prev_hash, data) :
        self.index = index # Index of block in blockchain
        self.timestamp = timestamp # Timestamp of block creation
        self.nonce = nonce # Nonce value for validation
        self.prev_hash = prev_hash # Hash of previous block in blockchain
        self.data = data # Data contained in block
        self.hash = self.hash_block() # Hash of new block

    def hash_block(self) :
        block_encrypt = h.sha256() # Create hasher
        encrypt_update = (str(self.index) + str(self.nonce) + str(self.timestamp) + str(self.prev_hash) + str(self.data)).encode() # Create content to be hashed
        block_encrypt.update(encrypt_update) # Update hasher
        return block_encrypt.hexdigest() # Return hash string

    def proof_of_work(last_block) :
        prev_nonce = last_block.nonce # Get last nonce to validate question
        new_nonce = 0 # Arbitrary start value for new nonce
        validator = '01' # Arbitrary string for validating question
        valid_params = False # Initiate question with False
        while valid_params is False :
            guess = (str(prev_nonce) + str(new_nonce)).encode()
            hex_guess = h.sha256(guess).hexdigest()
            if hex_guess[:len(validator)] == validator :
                valid_params = True
            new_nonce += 1
        return new_nonce

    def start_block() :
        index = 0 # First block index at 0
        nonce = 0 # Arbitrary value for first block
        timestamp = datetime.now()
        prev_hash = 'first block transaction' # First block does not have prev_hash
        data = 'data' + str(index)
        return Block(index, timestamp, nonce, prev_hash, data) # Return first block

    def new_block(last_block) :
        # Extract data from last block
        prev_data = last_block.data
        prev_index = last_block.index
        prev_hash = last_block.hash
        
        # Conduct proof of work
        new_nonce = Block.proof_of_work(last_block) # New nonce value for block hash
        
        #Set new block values
        index = prev_index # New block index is old block index + 1
        timestamp = datetime.now()
        prev_hash = prev_hash # New block stores previous block's hash
        data = prev_data + str(index) # Arbitrary data to store in new block
        return Block(index, timestamp, new_nonce, prev_hash, data) # Return new block
        
# Create blockchain as list for holding blocks
block_chain = list()

# Create and add first block
block_zero = Block.start_block()

print (block_zero.data)

new_block = Block.new_block(block_zero)

print (new_block.index)
print (new_block.timestamp)
print (new_block.nonce)
print (new_block.prev_hash)
print (new_block.data)
print (new_block.hash)
