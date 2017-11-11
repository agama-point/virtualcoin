from pybitcoin import BitcoinPrivateKey

class LitecoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 48
    
private_key = BitcoinPrivateKey()
litcoin_private_key = LitecoinPrivateKey(private_key.to_hex())
lcpkwif = litecoin_private_key.to_wif()
print lcpkwif 

litecoin_public_key = litecoin_private_key.public_key()
lcaddr = litcoin_public_key.address()
print "LTC.addr: "+lcaddr
