from coinkit.keypair import BitcoinKeypair
import threading
import sys
class vb4(BitcoinKeypair):
    # _pubkeyhash_version_byte=10
    def __init__(self,pubkey_byte):
        BitcoinKeypair._pubkeyhash_version_byte = pubkey_byte
        BitcoinKeypair.__init__(self)




verb4 = vb4(0);
count = 0;
while(verb4.address().upper().find(sys.argv[1].upper(),0,len(sys.argv[1]))<0):
    print 'address    '+verb4.address()+'------'+str(count)+'  pubkey_byte!'
    count=count+1
    verb4 = vb4(count);

print 'address    '+verb4.address()+'  founded !!---'+str(count)
print 'priv key   '+verb4.private_key()
print 'public_key '+verb4.public_key()
