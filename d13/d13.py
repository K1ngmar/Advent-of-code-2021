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

lines = [x for x in open("d13.input").read().splitlines()]

positions = dict()
for i in range(len(lines)):
	if lines[i] == "":
		lines = lines[i + 1:]
		break
	else:
		x,y = lines[i].split(",")
		if int(x) in positions:
			positions[int(x)].append(int(y))
		else:
			positions[int(x)] = [int(y)]

width = max(positions.keys()) + 1
height = 0
for x in positions:
	for y in positions[x]:
		if y + 1 > height:
			height = y + 1

paper = [['.' for x in range(width)] for y in range(height)]
for x in positions:
	for y in positions[x]:
		paper[y][x] = "#"

moves = []
for line in lines:
	line = line.strip("fold along ")
	axis,pos = line.split("=")
	moves.append((axis, int(pos)))

def flip_x(pos):
	global paper
	global width
	for x in range(pos, width):
		new_pos = pos - (x - pos)
		if new_pos < 0:
			pass
		for y in range(height):
			if (paper[y][x] == "#"):
				paper[y][new_pos] = "#"
	for y in range(height):
		paper[y] = paper[y][:pos]
	width = pos

def flip_y(pos):
	global paper
	global height
	for y in range(pos, height):
		new_pos = pos - (y - pos)
		if new_pos < 0:
			pass
		for x in range(width):
			if paper[y][x] == "#":
				paper[new_pos][x] = "#"
	paper = paper[:pos]
	height = pos

def print_paper():
	global paper
	global height
	for y in range(height):
		print(paper[y])

def count_squares():
	global width
	global height
	global paper
	count = 0
	for y in range(height):
		for x in range(width):
			if paper[y][x] == "#":
				count += 1
	return count

def calc_moves(ex, lim):
	if len(moves) < lim or lim < 0:
		lim = len(moves)
	for i in range(lim):
		if moves[i][0] == "x":
			flip_x(moves[i][1])
		else:
			flip_y(moves[i][1])
	print(ex, count_squares())

calc_moves("ex00:", 1)
calc_moves("ex01:", -1)
print_paper()
