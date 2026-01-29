import subprocess

import schemdraw
import schemdraw.elements as elm
from schemdraw import flow

# print("START")
# with open('labels.txt','r') as file:
#     label = file.read().splitlines()

with schemdraw.Drawing() as d:
    d.config(unit=10)
    label = ['33 KV MAIN BUS BAR PANTHER']  # Define label as a list with appropriate values
    # top bus
    d.move(-40,0)
    # bus_start = d.here
    d+= elm.Line().right(50).label(label[0],loc='top')
    d.push()
    d.move_from(d.here, dx=-10)
    d+= elm.Line().up(5)
    d.pop()
    # LEFT FEEDER
    d.push()
    d.move_from(d.here,dx=-25)
    #isolator
    d+= elm.Switch(open=True).down()
    d+= elm.Label().label('ISOLATOR\n33KV\nN/C',loc='right')
    #VCB
    d+= elm.Line().down(1)
    d+= elm.Breaker().down()
    d+= elm.Label().label('VCB\n33KV',loc='right')
    d+= elm.Line().down(3)
    #CT
    d+= elm.Line().down(4)
    d+= elm.Dot()
    d+= elm.Label().label('CT\n300/1A', loc='right')
    d+= elm.Line().down(3)
    #LA
    d+= elm.Line().down(4)
    d+= elm.Label().label('LA',loc='right')
    d+= elm.Line().down(3)
    #TRANSFORMER
    d+= elm.Line().down(4)
    d+= elm.Transformer()
    d+= elm.Label().label('Power Transformer',loc='right')
    d.pop()
    # for the right side vala 
    d.push()
    d.move_from(d.here,dx=20)
    d+= elm.Line().down(5)
    #isolator
    d+= elm.Switch(open=True).down()
    d+= elm.Label().label('ISOLATOR\n33KV\nN/C',loc='right')
    d+= elm.Line().down(3)
    #VCB
    d+= elm.Line().down(1)
    d+= elm.Breaker().down()
    d+= elm.Label().label('VCB\n33KV',loc='right')
    d+= elm.Line().down(3)
    #CT
    d+= elm.Line().down(4)
    d+= elm.Dot()
    d+= elm.Label().label('CT\n300/1A', loc='right')
    d+= elm.Line().down(3)
    #LA
    d+= elm.Line().down(4)
    d+= elm.Label().label('LA',loc='right')
    d+= elm.Line().down(3)
    #TRANSFORMER
    d+= elm.Line().down(4)
    d+= elm.Transformer()
    d+= elm.Label().label('Power Transformer',loc='right')
    d.pop()