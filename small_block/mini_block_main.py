"""mini self-contained blockchain demonstrating blockchain mechanics"""

from datetime import datetime
import hashlib as h
import numpy as np

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
        """Block hash helper function"""
        block_encrypt = h.sha256() # Create hasher
        encrypt_update = (str(self.index) + str(self.nonce) + str(self.timestamp) + str(self.prev_hash) + str(self.data)).encode() # Create content to be hashed
        block_encrypt.update(encrypt_update) # Update hasher
        return block_encrypt.hexdigest() # Return hash string

    def proof_of_work(last_block) :
        """Proof of work helper function"""

        # Function values
        prev_nonce = last_block.nonce # Get last nonce to validate question
        new_nonce = 0 # Arbitrary start value for new nonce
        validator = '01' # Arbitrary string for validating question
        valid_params = False # Initiate question with False

        # Loop until problem solved
        while valid_params is False :
            guess = (str(prev_nonce) + str(new_nonce)).encode()
            hex_guess = h.sha256(guess).hexdigest()
            if hex_guess[:len(validator)] == validator :
                valid_params = True
            else :
                new_nonce += 1

        # Return proof of work
        return new_nonce

    def start_block() :
        """Create first block of chain"""

        index = 0 # First block index at 0
        nonce = 0 # Arbitrary value for first block
        timestamp = datetime.now()
        prev_hash = 'first block transaction' # First block does not have prev_hash
        data = 'data' + str(index)
        return Block(index, timestamp, nonce, prev_hash, data) # Return first block

    def new_block(last_block) :
        """Create a new block"""

        # Extract data from last block
        prev_data = last_block.data
        prev_index = last_block.index
        prev_hash = last_block.hash

        # Conduct proof of work
        new_nonce = Block.proof_of_work(last_block) # New nonce value for block hash

        #Set new block values
        index = prev_index + 1 # New block index is old block index + 1
        timestamp = datetime.now()
        prev_hash = prev_hash # New block stores previous block's hash
        data = prev_data + str(index) # Arbitrary data to store in new block
        return Block(index, timestamp, new_nonce, prev_hash, data) # Return new block

class Transaction : ### ONLY MAPPED OUT WITH COMMENT BLOCKS

    """Class for creating transactions"""

    def __init__(self, transaction_data, holder_data) :
        self.transaction_data = transaction_data # All historical transactions
        self.holder_data = holder_data # Current list of holders and amounts

    def create_transation(seller, buyer, amount, holder_data) :
        """Create a new transaction"""

        # Create a new transaction and return it in the form of a dictionary

        # Verify transaction can happen based on existing balances

        # If validated, return new transaction
        return new_transaction

    def append_transaction(new_transaction, transaction_data, holder_data) :
        """Add new transaction to complete list of transactions and update holding values"""

        # Add transaction to the full list

        # Update holder dictionary

        return transaction_data, holder_data

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
    print ('Nonce: ', current_block.nonce)
    print ('Data: ', current_block.data)
    print ('Hash: ', current_block.hash)
    hash_to_check = current_block.hash # Store block hash to compare to next block prev_hash
    print ('\n===\n')
