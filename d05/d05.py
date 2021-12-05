# **************************************************************************** #
#                                                                              #
#                             |                         _...._                 #
#                          \  _  /                    .::o:::::.               #
#                           (\o/)                    .:::'''':o:.              #
#                       ---  / \  ---                :o:_    _:::              #
#                            >*<                     `:}_>()<_{:'              #
#                           >0<@<                 @    `'//\\'`    @           #
#                          >>>@<<*              @ #     //  \\     # @         #
#                         >@>*<0<<<           __#_#____/'____'\____#_#__       #
#                        >*>>@<<<@<<         [__________________________]      #
#                       >@>>0<<<*<<@<         |=_- .-/\ /\ /\ /\--. =_-|       #
#                      >*>>0<<@<<<@<<<        |-_= | \ \\ \\ \\ \ |-_=-|       #
#                     >@>>*<<@<>*<<0<*<       |_=-=| / // // // / |_=-_|       #
#       \*/          >0>>*<<@<>0><<*<@<<      |=_- |`-'`-'`-'`-'  |=_=-|       #
#   ___\\U//___     >*>>@><0<<*>>@><*<0<<     | =_-| o          o |_==_|       #
#   |\\ | | \\|    >@>>0<*<<0>>@<<0<<<*<@<    |=_- | !     (    ! |=-_=|       #
#   | \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<  _|-,-=| !    ).    ! |-_-=|_      #
#   |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<@</=-((=_| ! __(:')__ ! |=_==_-\     #
#   |\\_|_|&&_// ||*.*.*.*|_\\db//__     (\_/)-=))-|/^\=^=^^=^=/^\| _=-_-_\    #
#   """"|'.'.'.|~~|.*.*.*|     ____|_   =('.')=//   ,------------.             #
#   jgs |'.'.'.|   ^^^^^^|____|>>>>>>|  ( ~~~ )/   (((((((())))))))            #
#       ~~~~~~~~         '""""`------'  `w---w`     `------------'             #
#                                                                              #
#                    Kingmar  |  https://github.com/K1ngmar                    #
#                                                                              #
# **************************************************************************** #

class Coordinate:

	def __init__(self, coordinates):
		coordinates	= coordinates.split(",")
		self.x		= int(coordinates[0])
		self.y		= int(coordinates[1])

class Line:

	def __init__(self, coords):
		coords		= coords.split(" -> ")
		self.begin	= Coordinate(coords[0])
		self.end	= Coordinate(coords[1])
		# meths
		self.slope	= 0 
		determinant = self.end.x - self.begin.x
		# (y2 - y1) / (x2 - x1)
		if determinant != 0:
			self.slope	= (self.end.y - self.begin.y) / determinant
		# b = y - ax
		self.start	= self.begin.y - self.slope * self.begin.x

	def calc_line(self):
		if self.begin.x == self.end.x:
			self.calc_line_vertical()
		else:
			self.calc_line_not_vertical()

	def calc_line_vertical(self):
		# ol switcheroo if end > begin
		if self.begin.y > self.end.y:
			tmp = self.begin
			self.begin = self.end
			self.end = tmp
		for y in range(self.begin.y, self.end.y + 1):
			x = self.begin.x
			if (x,y) in line_points.keys():
				line_points[(x, y)] += 1
			else:
				line_points[(x, y)] = 1

	def calc_line_not_vertical(self):
		# ol switcheroo if end > begin
		if self.begin.x > self.end.x:
			tmp = self.begin
			self.begin = self.end
			self.end = tmp
		for x in range(self.begin.x, self.end.x + 1):
			# y = ax + b
			y = int(self.slope * x + self.start)
			if (x,y) in line_points.keys():
				line_points[(x, y)] += 1
			else:
				line_points[(x, y)] = 1

def calculate_points(ex, slopeybois):
	for coord in coords:
		tmp = Line(coord)
		# discard all non horizontal / vertical lines
		if slopeybois == True or tmp.begin.x == tmp.end.x or tmp.begin.y == tmp.end.y:
			tmp.calc_line()
	print(ex, sum(map(lambda x:line_points[x]>1, line_points)))
	line_points.clear()

coords = open("d05.input").read().splitlines()
line_points = dict()
calculate_points("ex00:", False)
calculate_points("ex01:", True)
