# -*- coding: cp1250 -*-
import pyqrcode
import pygame, random, sys, os, time
from pygame.locals import * # MOUSEBUTTONDOWN...
from json import *
from datetime import datetime 
from bitcoin import *

startTime = time.time()
pygame.init()

from oeLib.oePygame import *
from myWallets import *
from oeLib.oeCrypto import * 
testCrypto = True

font={}             # pamet, ve ktere je ulozeny font, nacetny z externiho souboru
myMatrix={}     # hlavní velká
myMatrix2={}    # pomocná veláimport pyqrcode
myMatSil={}     # šedá malá
myMatFilt={}    # filtrovaná malá   

myDir = "data/"
notePrefix="B.test:"
logTime = datetime.now().strftime("%Y%m%d_%H%M%S") 
logFile = myDir+logTime+"log.txt"
fileJpg = myDir+logTime+".jpg"
filePng = myDir+logTime+".png"
wbtc = getWBTC()
pbtc=wbtc+wbtc

addLog(logFile,"octopusEngine - VirtualCoin02 - beta")
addLog(logFile,"log: "+str(logTime))

myFont = pygame.font.SysFont("monospace", 15)

# Set up some variables containing the screeen size
sizeWinX=900
sizeWinY=500

colYel = (255,255,0)
colWhi = (255,255,255)
colRed = (255,0,0)
colBlu = (0,0,255)
colSil = (128,128,128)
colBla = (0,0,0)

hA= mxW() #main matrix width
hB= mxH() #main matrix height
hBod = mxP()
hW=hA*hBod #velikost
hH=hB*hBod
hX=0   #pozice
hY=0

winMat = pygame.display.set_mode([hA,hB]) # Create the pygame matrix window
win = pygame.display.set_mode([sizeWinX,sizeWinY]) # Create the pygame window
pygame.display.set_caption("oeVirtualCoin")        

##==================================================================
cisloCrypto = 123456789

if (testCrypto):
  cislo = cisloCrypto
  print cislo
  wifcislo = numtowif(cislo)
  print wifcislo
  print wiftonum(wifcislo)

  hextobin(hex(cislo))
  
  print "---bin---"
  strb = "aaa"
  print strb
  print strtobin(strb)
  print bintostr(strtobin(strb))
  strb = wifcislo
  print strb
  print strtobin(strb)
  print bintostr(strtobin(strb))
##==================================================================

butty = 35
bty = 10
btx1 = 660
btx2 = btx1+100
chy = 390
ch1 = CheckBox(win,200,chy);ch1.initChBox("select 1")
ch2 = CheckBox(win,330,chy);ch2.initChBox("select 2")
ch3 = CheckBox(win,460,chy);ch3.initChBox("select 3")

bt1 = ButtBox(win,btx1,bty);bt1.labelButt("clear")        
bt3 = ButtBox(win,btx1,bty+butty);bt3.labelButt("invert")
bt5 = ButtBox(win,btx1,bty+butty*2);bt5.labelButt("noise")
bt7 = ButtBox(win,btx1,bty+butty*3);bt7.labelButt("info")
bt9 = ButtBox(win,btx1,bty+butty*4);bt9.labelButt("qr1")
bt11 = ButtBox(win,btx1,bty+butty*5);bt11.labelButt("qr2")

bt2 = ButtBox(win,btx2,bty);bt2.labelButt("save")
bt4 = ButtBox(win,btx2,bty+butty);bt4.labelButt("load")
bt6 = ButtBox(win,btx2,bty+butty*2);bt6.labelButt("gen1")
bt8 = ButtBox(win,btx2,bty+butty*3);bt8.labelButt("gen2")
bt10 = ButtBox(win,btx2,bty+butty*4);bt10.labelButt("test")
bt12 = ButtBox(win,btx2,bty+butty*5);bt12.labelButt("quit")

def startWin():
  print "clrMat>"
  setMat(myMatrix,0)
  print "time>" + str(time.time()-startTime)
  print "printMat>"
  plotMat(win,myMatrix)
  print "time>" + str(time.time()-startTime)

  label = myFont.render("test Virtual Coin", 1, colYel)
  win.blit(label, (chy, 10))

  ## hriste
  print "hriste>"
  doHriste(win)

  print "test znak a slovo>"
  mxChar(win, myMatrix,51,220,10,inverze=False)
  mxStr(win, myMatrix,"IMAGE text TEST",5,135)
  co = "size:" + str(hA)+"x"+str(hB)
  mxStr(win, myMatrix,co,5,145)
  mxStr(win, myMatrix,wbtc,5,155)

  ## qr test wall
  #qrBig = pyqrcode.create(w11,error="L",version=27,mode="binary")
  #qrBig.png("qr.png", scale = 6,module_color=[0,0,0,128],background=[0xff,0xff,0xcc])	
	
  #createQR(wbtc+wbtc+wbtc,3)
  #obr = pygame.image.load(myDir+"tempqr.png") #src/knize.bmp
  #obrRect = obr.get_rect()
  #obrRect = obrRect.move(hX*2+hW,hY+200)
  #win.blit(obr, obrRect)   

  # nacteni dvoubarevneho BMP obrazku 128x128 bodu do promenne mapa[]
  print "bmp>"
  #doBmp128x128("knize.bmp")
  doBmp2Mat(myMatrix,"src/o128i.bmp",20,5)
  print "time>" + str(time.time()-startTime)
  print "printMat>"
  plotMat(win,myMatrix)
  print "time plot>" + str(time.time()-startTime)

#myMatrix2 = myMatrix
#copyMat(myMatrix,myMatrix2)
#setMat(myMatrix,1)
#plotMat(win,myMatrix)
#print "time clr2>" + str(time.time()-startTime)

#myMatrix = myMatrix2
#restoreMat(myMatrix,myMatrix2)
#plotMat(win,myMatrix)
#print "time plot2>" + str(time.time()-startTime)

#hBod=2
#creaMatSil()
#plotMatSil(300,70)
#print "time sil>" + str(time.time()-startTime)
#print "time>" + str(time.time()-startTime)
#pygame.quit()

startWin()
while True:
   #time.sleep(1)
   for event in pygame.event.get():
     if event.type == MOUSEBUTTONDOWN:
        x, y = event.pos
        #print x, y
        ch1.setChBox(x,y)
        ch2.setChBox(x,y)
        ch3.setChBox(x,y)
        sel = 1
        if (ch1.getChBox()): sel = 2
        if (ch2.getChBox()): sel = 5
        if (ch3.getChBox()): sel = 10
        
        if bt1.testClickButt(x,y):
                setMat(myMatrix,0)
                plotMat(win,myMatrix)
                print "time clear>" + str(time.time()-startTime)  
        
        if bt3.testClickButt(x,y):
                #mxStr(win, myMatrix,"invert",5,155)
                invertMat(myMatrix)
                plotMat(win,myMatrix)
                print "time inv>" + str(time.time()-startTime)
                
        if bt5.testClickButt(x,y):
                addnoiseMat(myMatrix)
                #mxStr(win, myMatrix,"noise",5,155)
                plotMat(win,myMatrix)
                print "time noise>" + str(time.time()-startTime)
                
                         
                
        if bt7.testClickButt(x,y):
                print("---save---info---")
                print(cisloCrypto)
                wifinfo = numtowif(cisloCrypto) 
                print("wif:"+wifinfo)
                #infostr = strtobin(wifcislo)
                hexinfo = hex(cislo)
                print("hex:"+hexinfo)
                
                infoMat(myMatrix,sel,hextobin(hexinfo))
                plotMat(win,myMatrix)
                print "time info save>" + str(time.time()-startTime)    
             
        if bt4.testClickButt(x,y):
                print("---load---info---")
                filetPng = myDir+"temp.png"
                myBin = loadMat(win,filetPng,myMatrix,sel)
                print("bin:"+myBin[:260])
                hexinfo=bin8tohex(myBin[:160])
                print("hex:"+hexinfo)
                #print("int:"+str(int(hexinfo, base=16)))
                plotMat(win,myMatrix)
                print "time info>" + str(time.time()-startTime)
                
        if bt6.testClickButt(x,y):
                print("---gen1---")
                pkall = createWall("x")
		        #private_key, pkwif,public_key,pubhex, wall 
                print "time info>" + str(time.time()-startTime) 
                print("0: "+str(pkall[0]))
                pbtc=str(pkall[1])
                addLog(logFile,"1: "+pbtc)
                addLog(logFile,"2: "+str(pkall[2]))
                addLog(logFile,"3: "+str(pkall[3]))
                wbtc=str(pkall[4])
                addLog(logFile,"4: "+wbtc)
        
	if bt10.testClickButt(x,y):
                print("---test unspent---")               
                h = history(addr)
                print h
                u = unspent(addr)
                print u
                print(oeShort(wbtc,8)+" > "+str(oeJTxSumVal(unspent(wbtc))))
                             
        if bt9.testClickButt(x,y):  # test wallet      
                setMat(myMatrix,0)
                mxy = 128
                mxStr(win, myMatrix,notePrefix+logTime,5,mxy)
                mxStr(win, myMatrix,wbtc,5,mxy+10)
                mxStr(win, myMatrix,".....",5,mxy+20)
                #mxStr(win, myMatrix,(wbtc+wbtc),5,161)            
                mxStr(win, myMatrix,oeShort(pbtc,22),5,mxy+30)    
                mxStr(win, myMatrix,"octopusEngine",5,mxy+40) 
           
                filetPng = myDir+"tempqr.png" 
                qrx=5
                qry=5
                
                addLog(logFile,pbtc)
                createQR(pbtc,2)
                loadMatQR(win,filetPng,myMatrix,150,qry)
                obr = pygame.image.load(filetPng) 
                obrRect = obr.get_rect()
                obrRect = obrRect.move(hX*2+100,0)
                win.blit(obr, obrRect)                               
                
                createQR(wbtc,3)
                addLog(logFile,wbtc)
                loadMatQR(win,filetPng,myMatrix,qrx,qry)                
                obr = pygame.image.load(filetPng) 
                obrRect = obr.get_rect()
                obrRect = obrRect.move(hX*2+100,0)
                win.blit(obr, obrRect) 
                
                         
                plotMat(win,myMatrix)
                                                                
        if bt2.testClickButt(x,y):
                if (ch1.getChBox()):
                  saveJpg(win,fileJpg,sizeWinX, sizeWinY)
                else: 
                  winMat = pygame.display.set_mode([hA,hB]) # Create the pygame matrix window
                  #plotMat(winMat,myMatrix)             
                  saveMat(winMat,filePng,myMatrix)
                  print("---ok-save: "+filePng)
                  win = pygame.display.set_mode([sizeWinX,sizeWinY]) # Create the pygame window
                  win.fill(colBla)
                  pygame.display.flip                                    
                  startWin()
     
     if event.type == pygame.QUIT:
                  sys.exit() 
