from datetime import datetime
import hashlib as h

class Block :

    def __init__(self, index, timestamp, prev_hash, data) :
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.hash = self.hash_block()

    def hash_block(self) :
        block_encrypt = h.sha256()
        encrypt_update = (str(self.index) + str(self.timestamp) + str(self.prev_hash) + str(self.data)).encode()
        block_encrypt.update(encrypt_update)
        return block_encrypt.hexdigest()

    @staticmethod
    def start_block() :
        index = 0
        timestamp = datetime.now()
        prev_hash = 'first block transaction'
        data = 'data' + str(index)
        return Block(index, timestamp, prev_hash, data)

    @staticmethod
    def new_block(last_block) :
        index = last_block.index + 1
        timestamp = datetime.now()
        prev_hash = last_block.hash
        data = 'data' + str(index)
        return Block(index, timestamp, prev_hash, data)

block_zero = Block.start_block()

block_chain = [block_zero]

for i in range(5) :
    add_block = Block.new_block(block_chain[i])
    block_chain.append(add_block)

for i in range(len(block_chain)) :
    current_block = block_chain[i]
    print ('Index: ', current_block.index)
    print ('Timestamp: ', current_block.timestamp)
    print ('Previous hash: ', current_block.prev_hash)
    print ('Data: ', current_block.data)
    print ('Hash: ', current_block.hash)
    print ('\n===\n')
