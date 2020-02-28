import pygame
import math
from shapely.geometry import LineString, Polygon
#from queue import PriorityQueue
pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((1000, 450))
gameDisplay.fill(white)

pixAr = pygame.PixelArray(gameDisplay)


pygame.draw.rect(gameDisplay, blue, (200,350,300,75), 3)

pygame.draw.polygon(gameDisplay, blue, ((300,300), (400,300), (350,125)), 3)

pygame.draw.polygon(gameDisplay, blue, ((250,290), (300,150), (250,50), (150,150), (175,270)),3) 

pygame.draw.polygon(gameDisplay, blue, ((550,390), (600,340), (510,250)),3) 

pygame.draw.polygon(gameDisplay, blue, ((400,175), (550,100), (475,40), (400,50)),3) 

pygame.draw.rect(gameDisplay, blue, (570,60,100,220),3)

pygame.draw.polygon(gameDisplay, blue, ((690,100), (740,60), (790,110), (730,310)),3) 

pygame.draw.polygon(gameDisplay, blue, ((680,290), (720,340), (720,390), (670,420), (640,390), (640,320)),3) 

pygame.draw.circle(gameDisplay, green, (160,370), 5)

pygame.draw.circle(gameDisplay, red, (780,70), 5)

poly = []

poly.append(Polygon([(200,350),(500,350),(500,425),(200,425)]))

poly.append(Polygon([(300,300), (400,300), (350,125)]))

poly.append(Polygon([(250,290), (300,150), (250,50), (150,150), (175,270)])) 

poly.append(Polygon([(550,390), (600,340), (510,250)])) 

poly.append(Polygon([(400,175), (550,100), (475,40), (400,50)])) 

poly.append(Polygon([(570,60),(670,60),(670,280),(570,280)]))

poly.append(Polygon([(690,100), (740,60), (790,110), (730,310)])) 

poly.append(Polygon([(680,290), (720,340), (720,390), (670,420), (640,390), (640,320)])) 

class Node:
	def __init__(self, xCord, yCord):
		self.xCord = xCord
		self.yCord = yCord

vertices = []
op = []
cl = []
o = []
c = []
vertices.append(Node(160,370))
vertices.append(Node(200,425))
vertices.append(Node(200,350))
vertices.append(Node(500,350))
vertices.append(Node(500,425))

vertices.append(Node(300,300))
vertices.append(Node(350,125))
vertices.append(Node(400,300))

vertices.append(Node(250,50))
vertices.append(Node(150,150))
vertices.append(Node(175,270))
vertices.append(Node(250,290))
vertices.append(Node(300,150))

vertices.append(Node(400,50))
vertices.append(Node(475,40))
vertices.append(Node(550,100))
vertices.append(Node(400,175))

vertices.append(Node(510,250))
vertices.append(Node(550,390))
vertices.append(Node(600,340))

vertices.append(Node(570,60))
vertices.append(Node(670,60))
vertices.append(Node(670,280))
vertices.append(Node(570,280))

vertices.append(Node(740,60))
vertices.append(Node(690,100))
vertices.append(Node(790,110))
vertices.append(Node(730,310))

vertices.append(Node(680,290))
vertices.append(Node(720,340))
vertices.append(Node(720,390))
vertices.append(Node(670,420))
vertices.append(Node(640,390))
vertices.append(Node(640,320))
vertices.append(Node(780,70))
#print(len(vertices))
print(len(vertices))
def ception(Node1):
	for x in range(len(vertices)):
		#print(x)
		seg = LineString([(Node1.xCord,Node1.yCord), (vertices[x].xCord, vertices[x].yCord)])
		inter = False
		for p in poly:

			if seg.intersects(p) == False and seg.touches(p) == True:

				inter = True
				
				
				#x = x + 1
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == True:
				#print("TESSSSSSSSSSSSSSSSSSSSSSSSSSSSST")
				inter = True
				#x = x + 1
				#	print(x)
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == False:
				inter = False
				break
				#o.append(vertices[x])
				#x = x + 1
		if inter:
			#print(inter)
			o.append(vertices[x])
			#x = x + 1


def gdistance(Node1, Node2):
	Node1 = Node1
	Node2 = Node2
	distance = math.sqrt((Node1.xCord - Node2.xCord)** 2 + (Node1.yCord - Node2.yCord) ** 2)
	return distance
	print(distance)

def hdistance( Node1):
	Node1 = Node1
	distance = math.sqrt((Node1.xCord - vertices[34].xCord)** 2 + (Node1.yCord - vertices[34].yCord) ** 2)
	return distance
	print(distance)

def search(Node1):
	for i in range(len(cl)):
		if Node1 == cl[i]:
			return True

def visted():
	i = 0
	while i < len(o):
		if search(o[i]) == True:
			print(o[1])
			del o[i]
			i = i +1
		else:
			i = i +1

def total(nBest):
	x = 0
	while x < len(o):
		f = (gdistance(nBest, o[x])) + (hdistance(o[x]))
		#print(f)
		#print(o[x])
		op.append([f,o[x]])
		x = x + 1


def action(Node1):
	for x in range(len(vertices)):
		#print(x)
		seg = LineString([(Node1.xCord,Node1.yCord), (vertices[x].xCord, vertices[x].yCord)])
		inter = False
		for p in poly:

			if seg.intersects(p) == False and seg.touches(p) == True:

				inter = True
				
				
				#x = x + 1
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == True:
				#print("TESSSSSSSSSSSSSSSSSSSSSSSSSSSSST")
				inter = True
				#x = x + 1
				#	print(x)
				#o.append(vertices[x])
			elif seg.intersects(p) == True and seg.touches(p) == False:
				inter = False
				break
				#o.append(vertices[x])
				#x = x + 1
		if inter:
			#print(inter)
			c.append(vertices[x])
			#x = x + 1

def move():
	new = op[0]
	cl.append(new[1])
	op.clear()

def take_first(elem):
    return elem[0]

def drawLine(Node1,Node2):
	Node1 = Node1
	Node2 = Node2
	pygame.draw.line(gameDisplay,black,(Node1.xCord,Node1.yCord), (Node2.xCord,Node2.yCord), 5)

def printcl():
	x = 0
	while x < (len(cl) - 1):
		p1 = cl[x]
		p2 = cl[x + 1]
		drawLine(p1,p2)
		x = x + 1

def sort():
	x = 0
	c = op[x]
	n = op[len(op) - 1]
	current = c[0]
	nex = n[0]
	while x < len(op):
		if(current < nex):
			op.append(c)
			x = x + 1
		else:
			x = x + 1 



def astar():
	goal = vertices[34]
	nBest = cl[ len(cl) - 1]
	if nBest == goal:
		print("FUCK YA!")
	else:
		ception(nBest)
		visted()
		total(nBest)
		#print(op)
		op.sort(key=take_first)
		#sort()
		x = 0
		print("++++++++++++")
		while x < len(op):
			next_item = op[x]
			print(next_item)
			x = x + 1
		move()

#print(len(o))
#print(vertices[1])
cl.append(vertices[0])
astar()
#astar()
#astar()
print(len(o))
astar()
astar()
astar()
astar()
astar()
astar()
astar()
astar()
astar()
astar()



printcl()




x = 0
while x < len(op):
	next_item = op[x]
	print(next_item)
	x = x + 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()