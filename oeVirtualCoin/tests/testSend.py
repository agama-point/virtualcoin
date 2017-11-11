from pybitcoin import BlockcypherClient

recipient_address = '1EEwLZVZMc2EhMf3LXDARbp4mA3qAwhBxu'
blockchain_client = BlockcypherClient(BLOCKCYPHER_API_KEY)
send_to_address(recipient_address, 10000, private_key.to_hex(), blockchain_client)