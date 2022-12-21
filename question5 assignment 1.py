import math as m
i=0
for i in range(0,346,15):
    
    x=m.sin(m.radians(i))
    y=m.cos(m.radians(i))
    print('%.4f' % (x),'%.4f' % (y))
    
