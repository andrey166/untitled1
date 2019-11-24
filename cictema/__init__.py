from mcpi.minecraft import Minecraft
mc = Minecraft.create()

va = 0,1
x0, y0, z0= 2,3
a = 0
import math
xn, yn = math.cos(a), math.sin(a)
while True:
    a += va
    xc, yc = math.cos(a), math.sin(a)
    if(xc != xn)|(yc != yn):
        mc.setBlock(x0 + xc,y0 + yc, z0, )