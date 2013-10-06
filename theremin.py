

#from __future__ import division
from time import sleep
from pyo import *
from pyo import midiToHz
from random import *
#from visual import *
from read import *
#import sys, os

#os.system("comtest.exe")
def xzToNote(L):
    #print L
    x=L[0]
    y=L[1]
    print y
    z=L[2]
    """
    c3=[48,0x84,"C3"]
    d3=[50,0x44,"D3"]
    e3=[52,0x24,"E3"]
    g3=[55,0x14,"G3"]
    a3=[57,0x0c,"A3"]
    c4=[60,0x82,"C4"]
    d4=[62,0x42,"D4"]
    e4=[64,0x22,"E4"]
    g4=[67,0x12,"G4"]
    a4=[69,0x0A,"A4"]
    c5=[72,0x81,"C5"]
    scale = [x[0] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c5]]
    hexscale = [x[1] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c5]]
    strscale = [x[2] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c5]]
    """
    IDK=.25
    #print x
    x=(x+.8)*100
    #print x
    if x<27:
        if z>IDK: return 5
        else: return 0
        #return C
    elif x<49:
        if z>IDK: return 6
        else: return 1
        #return D
    elif x<71:
        if z>IDK: return 7
        else: return 2
        #return E
    elif x<92:
        if z>IDK: return 8
        else: return 3
        #return G
    elif x<115:
        if z>IDK: return 9
        else: return 4
        #return A
    else:
        if z>IDK: return 5
        else: return 11
    """
    x=(x+.54)*100
    if x<18:
        if z>IDK:
        else: 
        #return C
    elif x<36:
        if z>IDK:
        else:
        #return D
    elif x<54:
        if z>IDK:
        else:
        #return E
    elif x<72:
        if z>IDK:
        else:
        #return G
    elif x<90:
        if z>IDK:
        else:
        #return A
    elif x<120:
        if z>IDK:
        else:
        #return higher octave C
    """


s = Server().boot()

c3=[48,0x84,"C3",(-5.5,-3,0)]
d3=[50,0x44,"D3",(-3.3,-3,0)]
e3=[52,0x24,"E3",(-1.1,-3,0)]
g3=[55,0x14,"G3",(1.1,-3,0)]
a3=[57,0x0c,"A3",(3.3,-3,0)]
c4=[60,0x82,"C4",(-5.5,-3,0)]
d4=[62,0x42,"D4",(-3.3,-3,0)]
e4=[64,0x22,"E4",(-1.1,-3,0)]
g4=[67,0x12,"G4",(1.1,-3,0)]
a4=[69,0x0A,"A4",(3.3,-3,0)]
c5=[72,0x81,"C5",(5.5,-3,0)]
c0=[21,0x81,"C0",(5.5,-3,0)]

'''
c3=[48,0x84,"C3",(0,-3,0)]
d3=[50,0x44,"D3",(0,-3,0)]
e3=[52,0x24,"E3",(0,-3,0)]
g3=[55,0x14,"G3",(0,-3,0)]
a3=[57,0x0c,"A3",(0,-3,0)]
c4=[60,0x82,"C4",(0,-3,0)]
d4=[62,0x42,"D4",(0,-3,0)]
e4=[64,0x22,"E4",(0,-3,0)]
g4=[67,0x12,"G4",(0,-3,0)]
a4=[69,0x0A,"A4",(0,-3,0)]
c5=[72,0x81,"C5",(0,-3,0)]
'''
notes = [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c5,c0]
scale = [x[0] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c0,c5]]
hexscale = [x[1] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c0,c5]]
strscale = [x[2] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c0,c5]]
notecoords = [x[3] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4,c0,c5]]
#Note = text(height=2,text="Note Played", pos=(0,0,0),align='center', depth=-0.3, color=color.green)
#rt = shapes.rectangle(pos=(0,-3), width=11, height=1)
#extrusion(shape=rt)
#points(pos=[(0,-3,0)], size=35, color=color.red)
#notepos = sphere(pos=(0,-3,0), radius=0.5, color=color.blue)
repeatx=None
repeaty=None
#sleep(1)
s.start()
while True:
    cooords=get_coords()
    r = xzToNote(cooords)
    ycord=(cooords[1]+.75)
    #print r
    y=midiToHz(scale[r])
    if repeatx !=r:
        a = Sine(freq=y, mul=(ycord)).out()
        #Note.text=strscale[r]
       #print(strscale[r])
    repeatx = r

    #Note.text=strscale[r]
    #notepos.pos=notecoords[r]
    #print(strscale[r])#,notecoords[r])
    #extrusion(shape=notept)
    #sleep(.25*[1,2,4][randint(0,2)])
s.stop()



"""
#scale_degrees = [midiToHz(m+7) for m in [36,43.01,48,55.01,60]]

#print scale_degrees
#for x in scale_degrees:

while True:
#for x in range(40,500):
    x = int(raw_input("Enter midi number: "))
    x=midiToHz(x)
    a = Sine(freq=x, mul=(1)).out()
    #b = Sine(freq=(x+3), mul=(1)).out()
    print(x)
    #s.gui(locals())
    #text(text=str(x))
    sleep(.5)
    #s.stop
    #text.visible=False

#s.gui(locals())

"""


