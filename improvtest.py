from time import sleep
from pyo import *
from pyo import midiToHz
from random import *
from visual import *

def xzToNote(x,z):

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
    #c5=72
    scale = [x[0] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]
    hexscale = [x[1] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]
    strscale = [x[2] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]

    """
    x=(x+.55)*100
    if x<22:
        if z>IDK:
        else: 
        #return C
    elif x<44:
        if z>IDK:
        else:
        #return D
    elif x<66:
        if z>IDK:
        else:
        #return E
    elif x<88:
        if z>IDK:
        else:
        #return G
    elif x<120:
        if z>IDK:
        else:
        #return A
    """
    

s = Server().boot()

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
#c5=72
scale = [x[0] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]
hexscale = [x[1] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]
strscale = [x[2] for x in [c3,d3,e3,g3,a3,c4,d4,e4,g4,a4]]#,c5]

Note = text(text="Note Played")

s.start()
while True:
    r = randint(0,len(scale)-1)
    y=midiToHz(scale[r])
    a = Sine(freq=y, mul=(1)).out()
    Note.text=strscale[r]
    sleep(.25*[1,2,4][randint(0,2)])
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


