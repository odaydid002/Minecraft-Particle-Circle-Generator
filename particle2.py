import math, numpy
z=0
r=0.5
n=0
fname=input('File_name:')
f=open(str(fname) + ".mcfunction","a+")
gr = numpy.linspace(0,2*math.pi)
particle = input('Particle( EX: minecraft:basic_flame_particle ): ')
scoreboard = input('Scoreboard objective name: ')
for t in gr:
    command="execute @a[scores={"+str(scoreboard)+"="+str(n)+"}] ~ ~ ~ particle "+str(particle)+" ~"+str(r*math.cos(t))+" ~"+str(z)+" ~"+str(r*math.sin(t))
    f.write("\n"+command)
    z+=0.02
    n+=1
    if n == 49:
        break
z = 1
n = 49
for t in gr:
    command="execute @a[scores={"+str(scoreboard)+"="+str(n)+"}] ~ ~ ~ particle "+str(particle)+" ~"+str(r*math.cos(t))+" ~"+str(z)+" ~"+str(r*math.sin(t))
    f.write("\n"+command)
    z+=0.02
    n+=1
    if n == 98:
        break

z = 2
n = 98
for t in gr:
    command="execute @a[scores={"+str(scoreboard)+"="+str(n)+"}] ~ ~ ~ particle "+str(particle)+" ~"+str(r*math.cos(t))+" ~"+str(z)+" ~"+str(r*math.sin(t))
    f.write("\n"+command)
    z-=0.02
    n+=1
    if n == 149:
        break
z = 1
n = 149
for t in gr:
    command="execute @a[scores={"+str(scoreboard)+"="+str(n)+"}] ~ ~ ~ particle "+str(particle)+" ~"+str(r*math.cos(t))+" ~"+str(z)+" ~"+str(r*math.sin(t))
    f.write("\n"+command)
    z-=0.02
    n+=1