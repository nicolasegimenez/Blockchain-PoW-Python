#Part 2 Mining our Blockchain

#Creating a Web App
app = Flask(__name__)


#Creating a Blockchain      
blockchain = Blockchain()

#Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block ['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash)
        response = {'message': 'Felicitaciones has minado tu bloque!',
                    'index': block['index'],
                    'timestamp': block ['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}
        return jsonify(response), 200


#Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'lenght': len(blockchain.chain)}
    return jsonify(response), 200
app.run(host = '0.0.0.0', port= 5000)  