rom pybitcoin import BitcoinPrivateKey

class LitecoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 48

litcoin_private_key = LitecoinPrivateKey(private_key.to_hex())
lcpkwif = namecoin_private_key.to_wif()
print lcpkwif 

litecoin_public_key = namecoin_private_key.public_key()
lcaddr = litcoin_public_key.address()
print lcaddr
