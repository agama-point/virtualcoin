from oeCrypto import *

def strto6bin(mystr):
  ixs = 0
  for si in mystr:
     ##     bin5 = (bin(int(si, base=16))) 
     bin5 = strtobin(si)[-6:]
     print mystr[ixs],bin5
     ixs = ixs+1

mystr="abcdefgh-123456789.xyz*-=ABC"


print "---"
strto6bin(mystr)

"""
print mystr+" s2b: "+strtobin(mystr)

arrbin = []

for ixs in mystr:
  print ixs, strtobin(ixs)
  arrbin.append(strtobin(ixs))

for ixb in arrbin:
  print ixb, bintostr(ixb)
"""

  

  
