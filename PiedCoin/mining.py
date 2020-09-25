from blocks import BlockChain

blockchain = BlockChain()

person = input('send piedcoin to person: ')

print("***Mining piedcoin initialising")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0", 
    recipient=person,  
    quantity=
    1,  
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Mining piedcoin has been successful***")
print(blockchain.chain)


