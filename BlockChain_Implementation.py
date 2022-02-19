'''
Created on 19-Feb-2022

@author: Karuna
'''
import hashlib


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self, AccountHolderName, hash, prev_hash):
        self.AccountHolderName = AccountHolderName
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:

    def __init__(self):
        hashLast = hashGenerator('The hash of the last Block')
        hashStart = hashGenerator('The hash of the current Block')
        genesis = Block('The First Block of the Blockchain',
                        hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, AccountHolderName):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(AccountHolderName+prev_hash)
        block = Block(AccountHolderName , hash, prev_hash)
        self.chain.append(block)

print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● Block Chain Implementation ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')

bc = Blockchain()
bc.add_block('1. Karuna Kadam')

bc.add_block('2. Sumit Jadhav')

bc.add_block('3. Riya Pardhe')

bc.add_block('4. Piyush Patil')

bc.add_block('5. Aniket Mane')


for blocks in bc.chain:
    print('===========●==========●==========●==========●===========●==========●==============●============●==========●============●============●=========●===========●========●===========●=============●=============●===========●==========●===========●==========●=========')
    print("The list of the Blocks Information", blocks.__dict__)
    
   
    print('===========●==========●==========●==========●===========●==========●==============●============●==========●============●============●=========●===========●========●===========●=============●=============●===========●==========●===========●==========●=========')
    print("                                                                                              |")
    print("                                                                                              |")
    print("                                                                                              |")
    print("                                                                                            🔻🔻🔻")
print('●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●')






