''' Implementation of the codejam you can go your own way
	qualification round 2019
	url: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da '''

import turtle

class Own_Way:

	example = "SEEESSES"

	def __init__(self, path):
		self.path = path

	def Location(self):
		road_stops = [[0,0]]
		position_x = 0
		position_y = 0
		for move in self.path:
			if move == "E":
				position_x += 1
				road_stops.append([position_x,position_y])
			else:
				position_y += 1
				road_stops.append([position_x,position_y])

		return road_stops

	def Multi_Path_Generator(self, *patterns):
		for pattern in patterns: #function recives multiple arguments at once 
			our_path = ''.join(['E' if move == "S" else "S" for move in pattern])
			Own_Way.count += 1
			print ("Case #%d: %s" % (Own_Way.count, our_path))

	def Path_Generator(self):
		our_path = ''.join(['E' if move == "S" else "S" for move in self.path])
		self.our_path = our_path
		return self.our_path
	
	def visualizer(self, route, color):
		# turtle.write("AAAAAAAA", align="right", font=("Arial", 16, "normal"))
		turtle.bgcolor("#eaecef")
		loadWindow = turtle.Screen()
		turtle.speed(0)
		turtle.pensize(1)

		STEP = (int(1000 / ((len(route)+2)/2)))
		LENGTH = 1000
		for i in range(0, LENGTH, STEP):
			turtle.penup()
			turtle.setpos(-LENGTH/2, LENGTH/2 - i)
			turtle.pendown()
			turtle.setpos(LENGTH/2, LENGTH/2 - i)
			turtle.penup()
			turtle.setpos(-LENGTH/2 + i, LENGTH/2)
			turtle.pendown()
			turtle.setpos(-LENGTH/2 + i, -LENGTH/2)

		turtle.pensize(3)
		turtle.color(color)
		if len(route) > 14:
			ts = turtle.speed(10)
		else: 
			ts = turtle.speed(6)

		turtle.penup()
		turtle.setpos(-LENGTH/2 + 50, LENGTH/2 - 50)
		turtle.pendown()
		turtle.speed(1)


		for move in route:				
			# turtle.write(turtle.position(), move=True, align="right")
			if move == 'S':
				th = turtle.setheading(270)
				turtle.forward(STEP-15)
				turtle.penup()
				turtle.forward(15)
				turtle.pendown()
				print(turtle.position())
			else:
				th = turtle.setheading(0)
				turtle.forward(STEP-15)
				turtle.penup()
				turtle.forward(15)
				turtle.pendown()


	def Visual(self):
		self.visualizer(self.path, "#f9d939")
		self.visualizer(self.our_path, "#2464cc")


c = Own_Way("SEEESSEESS")
# print(c.Location())
c.Path_Generator()
c.Visual()



