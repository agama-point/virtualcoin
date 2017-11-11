#import numpy as np
from bitcoin import *
from pybitcoin import BitcoinPrivateKey
from pybitcoin import BitcoinPublicKey

#print bin( ~ np.uint64(5)) #8,16,32,64

class LitecoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 48

class NamecoinPrivateKey(BitcoinPrivateKey):
  _pubkeyhash_version_byte = 52

class VertcoinPrivateKey(BitcoinPrivateKey):
    _pubkeyhash_version_byte = 71

import hashlib, binascii
t='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def numtowif(numpriv):
 step1 = '80'+hex(numpriv)[2:].strip('L').zfill(64)
 step2 = hashlib.sha256(binascii.unhexlify(step1)).hexdigest()
 step3 = hashlib.sha256(binascii.unhexlify(step2)).hexdigest()
 step4 = int(step1 + step3[:8] , 16)
 return ''.join([t[step4/(58**l)%58] for l in range(100)])[::-1].lstrip('1')

def wiftonum(wifpriv):
 return sum([t.index(wifpriv[::-1][l])*(58**l) for l in range(len(wifpriv))])/(2**32)%(2**256)

def hextowif(numhex):
  hex(wiftonum('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')) 

def wiftohex(wif):
  return hex(wiftonum(wif)) 

def validwif(wifpriv):
 return numtowif(wiftonum(wifpriv))==wifpriv
 
def hextobin(hexn):
  #bin(private_key1.to_bin())
  return (bin(int(hexn, base=16)))
  #print len(PK1bits) 

def bintohex(binx):
   return hex(int(binx, 2))
   
def bin8tohex(strh):	
   tB = []
   tBs ="0x"	
   #print("len:"+str(len(strh)))
   #print(strh)
   try:
     for ib in range (0,160):
       Bapp = bintohex("0b"+str(strh)[2+ib*8:2+ib*8+8])	 
       tB.append(Bapp)
       print Bapp,
       tBs = tBs+tB[ib][2:4]
       #print ib,tB[ib]
   except: 
     err=True
     print ib,
   #print tB  
   return tBs  
    
def strtobin(str):
  return bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in str), 0))
   
def bintostr(bin):
  n = int(bin, 2)
  return binascii.unhexlify('%x' % n)

def oeN2Wtest(num):
	print("---")
	print(num)
	print(hex(num))
	print(numtowif(num))

def oeShort(s,num):
  return str(s[:num])+"..."+str(s[-num:])  

#---https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
  
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    
def addLog(logFile,co):
    print("log: "+co)
    fLog = open(logFile,"a") #a
    #fLog.write("test-log")
    #pomTemp=self.getProcTemp()
    #fLog.write("procTemp:"+str(pomTemp))
    fLog.write(co+"\n")
    fLog.close

def createWall(pk):
   if (len(pk)>20):
      private_key = BitcoinPrivateKey(pk) 
   else:
      private_key = BitcoinPrivateKey() 
	
   pkwif = private_key.to_wif()
   public_key = private_key.public_key()
   pubhex =public_key.to_hex()
   wall = public_key.address()
   return private_key, pkwif,public_key,pubhex, wall  

#------------------------json tx---------------------------
def oeJTxSumVal(j):
  sumsat = 0
  for uval in j:
    sumsat =sumsat + uval["value"]
  return float(sumsat)/100000000
    
    
    
  
  
