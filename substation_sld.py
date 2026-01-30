
import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing(show=False)
d.config(unit=10)

label = ['33 KV MAIN BUS BAR PANTHER']

# top bus
d.here = (-40, 0) #
d += elm.Line().right(50).label(label, loc='top')
bus_end = d.here

# small tap up
d.here = bus_end
d.move(dx=-10) #
d += elm.Line().up(5)

# LEFT FEEDER
d.here = bus_end
d.move(dx=-25)
d += elm.Line().down(5)
d += elm.Switch(open=True).down().label('ISOLATOR\n33KV\nN/C', loc='right')
d += elm.Breaker().down().label('VCB\n33KV', loc='right')
d += elm.Dot().label('CT\n300/1A', loc='right')
d += elm.Line().down(4).label('LA', loc='right')
d += elm.Transformer().label('Power Transformer', loc='right')

# RIGHT FEEDER
d.here = bus_end
d += elm.Line().down(5)
d += elm.Switch(open=True).down().label('ISOLATOR\n33KV\nN/C', loc='right')
d += elm.Breaker().down().label('VCB\n33KV', loc='right')
d += elm.Dot().label('CT\n300/1A', loc='right')
d += elm.Line().down(4).label('LA', loc='right')
d += elm.Transformer().label('Power Transformer', loc='right')

# SAVE IMAGE
d.save("substation.png")
