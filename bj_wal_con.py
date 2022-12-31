import web3

#check for CKBee NFT in player wallet

def check_wallet_for_nft(wallet_address, contract_address, contract_abi):
  # Connect to the Ethereum network
  web3 = web3.Web3(web3.Web3.EthereumTesterProvider())

  # Get the contract instance
  contract = web3.eth.contract(address=contract_address, abi=contract_abi)

  # Call the contract's balanceOf function to get the number of NFTs owned by the player
  nft_count = contract.functions.balanceOf(wallet_address).call()

  # Return the number of NFTs owned by the player
  return nft_count
