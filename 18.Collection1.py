#1____________:
#tuple :
#t = (11,22)
#print(t)
#print(t[0])
#print(t[1])

#2____________:
#namedtuple:
#from collections import namedtuple
#Point = namedtuple("Point",["x","y"])
#p = Point(10,5)
#print(p[0]+p[1])
#print(p.x+p.y)
#print(p)

#3____________:
#namedtuple:
#from collections import namedtuple
#Point = namedtuple("Point",("x","y"))
#p = Point(11,22)
#print(p._asdict())

#4____________:
#namedtuple:
#from collections import namedtuple
#Point = namedtuple("Point",("x","y"))
#p = Point(11,33)
#print(p._replace(x=4))


#5____________:
#namedtuple:
#from collections import namedtuple
#Point = namedtuple("Point",("x","y"))
#print(Point._fields)
#Color = namedtuple("Color","red")
#Pixel = namedtuple("Pixel",Point._fields+Color._fields)
#print(Pixel(11,22,128))


#6_______:
#La collection deque :
#from collections import deque
#L = deque()
#L.append(15)
#L.appendleft(180)
#print(L)

#7_______:
#La collection ChainMap :
#from collections import ChainMap
#d1= {"a":1,"b":2}
#d2= {"a":1,"b":2}
#d3= {"a":1,"b":2}
#c=ChainMap(d1,d2,d3)
#print(c)

#8_______:
#La collection ChainMap :
#from collections import ChainMap
#d1= {"a":1,"b":2}
#d2= {"a":1,"b":2}
#d3= {"a":1,"b":2}
#c=ChainMap(d1,d2,d3)
#print(c)
#for k,v in c.items():
 #   print(k,v,end=",")

































