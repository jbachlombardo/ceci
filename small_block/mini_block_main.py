"""mini self-contained blockchain demonstrating blockchain mechanics"""

from datetime import datetime
import hashlib as h
import numpy as np

class Block :

    """Class for creating blocks"""

    def __init__(self, index, timestamp, prev_hash, data) :
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

    def start_block() :
        index = 0 # First block index at 0
        nonce = 0 # Arbitrary value for first block
        timestamp = datetime.now()
        prev_hash = 'first block transaction' # First block does not have prev_hash
        data = 'data' + str(index)
        return Block(index, timestamp, prev_hash, data) # Return first block

    def new_block(last_block) :
        
        # Extract relevant parts of last_block
        prev_index = last_block.index
        prev_hash = last_block.hash
        
        # Proof of work -- create hash that ends in z
        while hash_value_lower = False :
            start_nonce = 0
            
        
        #Set new block values
        index = prev_index # New block index is old block index + 1
        timestamp = datetime.now()
        nonce = np.random.randint(0,100) # For simplicity max 100
        prev_hash = prev_hash # New block stores previous block's hash
        data = 'data' + str(index) # Arbitrary data to store in new block
        return Block(index, timestamp, prev_hash, data) # Return new block

# Create blockchain as list for holding blocks
block_chain = list()

# Create and add first block
block_zero = Block.start_block()

block_chain.append(block_zero)

# Create n subsequent blocks

n_blocks = 5

for i in range(n_blocks) :
    add_block = Block.new_block(block_chain[i])
    block_chain.append(add_block)

for i in range(len(block_chain)) :
    current_block = block_chain[i]
    print ('Index: ', current_block.index)
    print ('Timestamp: ', current_block.timestamp)
    print ('Previous hash: ', current_block.prev_hash)
    if i > 0 : # If not first block, check that hashes match up
        print ('Hashes match:', hash_to_check == current_block.prev_hash)
    print ('Data: ', current_block.data)
    print ('Hash: ', current_block.hash)
    hash_to_check = current_block.hash # Store block hash to compare to next block prev_hash
    print ('\n===\n')
