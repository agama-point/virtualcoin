# -*- coding: cp936 -*-
from coinkit.keypair import BitcoinKeypair
import threading
class vb4(BitcoinKeypair):
    # _pubkeyhash_version_byte=10
    def __init__(self,pubkey_byte):
        BitcoinKeypair._pubkeyhash_version_byte = pubkey_byte
        BitcoinKeypair.__init__(self)

class finder(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.thread_stop = False

        def run(self): #Overwrite run() method, put what you want the thread do here
            while not self.thread_stop:
                verb4 = vb4(100);
                count = 0;
                while(verb4.address().upper().find('ZAO')<0|count<500):
                    count=count+1
                    print 'address    '+verb4.address()+'------'+str(count)+'  addressed searched!'
                    verb4 = vb4(80);
                    self.thread_stop = True
            print 'address    '+verb4.address()
            print 'priv key   '+verb4.private_key()
            print 'public_key '+verb4.public_key()

        def stop(self):
            self.thread_stop = True

f1=finder()
f1.start()
