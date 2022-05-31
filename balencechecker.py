from web3 import Web3
infurakey="https://mainnet.infura.io/v3/2070d76c84cd41a58ee6199743878e1c"
web3 = Web3(Web3.HTTPProvider(infurakey))

address=input("Insert Ethereum address to balence check here : ")
balence=web3.eth.getBalence(address)

