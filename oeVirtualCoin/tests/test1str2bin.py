#from oeCrypto import *
import hashlib, binascii

def strtobin(str):
  return bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in str), 0))
   
def bintostr(bin):
  n = int(bin, 2)
  return binascii.unhexlify('%x' % n)


def strtobin7(mystr):
  ixs = 0
  retstr =""
  for si in mystr:
     ##     bin5 = (bin(int(si, base=16))) 
     bin7 = strtobin(si)[-7:].replace("b", "0")
     #print mystr[ixs],bin7
     ixs = ixs+1
     retstr=retstr+bin7
  return retstr

def bin7tostr(bstr):
  retstr =""
  for isx in range (len(bstr)/7):
    bin7 ="0b"+bstr[isx*7:isx*7+7]
    #print isx,bin7,bintostr(bin7)
    retstr=retstr+bintostr(bin7)
  return retstr  

mystr="abc123ABC"


print "---"
print mystr 
b7s = strtobin7(mystr)
print b7s
print bin7tostr(b7s)
"""
print mystr+" s2b: "+strtobin(mystr)

arrbin = []

for ixs in mystr:
  print ixs, strtobin(ixs)
  arrbin.append(strtobin(ixs))

for ixb in arrbin:
  print ixb, bintostr(ixb)
"""

  

  
