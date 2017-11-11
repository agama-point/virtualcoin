from pybitcoin import BitcoinPrivateKey

class VertcoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 72
    
private_key = BitcoinPrivateKey()
vertcoin_private_key = VertcoinPrivateKey(private_key.to_hex())
vcpkwif = vertcoin_private_key.to_wif()
print vcpkwif 

vertcoin_public_key = vertcoin_private_key.public_key()
vcaddr = vertcoin_public_key.address()
print "VTC.addr: "+vcaddr
