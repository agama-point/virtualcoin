rom pybitcoin import BitcoinPrivateKey

class NamecoinPrivateKey(BitcoinPrivateKey):
  _pubkeyhash_version_byte = 52

namecoin_private_key = NamecoinPrivateKey(private_key.to_hex())
namecoin_private_key.to_wif()
'73zteEjenBCK7qVtG2yRPeco2TP5w93qBW5sJkxYoGYvbWwAbXv'
namecoin_public_key = namecoin_private_key.public_key()
namecoin_public_key.address()
'MyMFt8fQdZ6rEyDhZbe2vd19gD8gzagr7Z'