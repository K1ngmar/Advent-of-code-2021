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

from collections import defaultdict

lines = open("d22.input").read().splitlines()

class Instructions:

	def __init__(self, line):
		l = line.split()
		self.on = 1 if l[0] == "on" else -1
		xd, yd, zd = l[1].split(",")
		self.xbot, self.xtop = [int(q) for q in xd[2:].split("..")]
		self.ybot, self.ytop = [int(q) for q in yd[2:].split("..")]
		self.zbot, self.ztop = [int(q) for q in zd[2:].split("..")]
		self.cub = (self.xbot, self.xtop, self.ybot, self.ytop, self.zbot, self.ztop)

def overlap(cub1, amt, cub2):
	maxMinX = max(cub1[0], cub2[0]) # right most x value, left side of cubes
	minMaxX = min(cub1[1], cub2[1]) # left most x value, right side of cubes
	maxMinY = max(cub1[2], cub2[2]) # highest y value, bottom side of cubes
	minMaxY = min(cub1[3], cub2[3]) # lowest y value, top side of cubes
	maxMinZ = max(cub1[4], cub2[4]) # deepest z value, front of cubes
	minMaxZ = min(cub1[5], cub2[5]) # closest z value, back of cubes

	# create overlapping cube
	if maxMinX <= minMaxX and maxMinY <= minMaxY and maxMinZ <= minMaxZ:
		grid[(maxMinX, minMaxX, maxMinY, minMaxY, maxMinZ, minMaxZ)] -= amt

instructions = []
for line in lines:
	instructions.append(Instructions(line))

grid = defaultdict(lambda: 0)
grid[instructions[0].cub] = instructions[0].on
for i in range(1, len(instructions)):
	tmp = grid.copy()
	for cube, amt in tmp.items():
		overlap(cube, amt, instructions[i].cub)
	if instructions[i].on == 1:
		grid[instructions[i].cub] += instructions[i].on

answer = 0
for cube, amt in grid.items():
	x0, x1, y0, y1, z0, z1 = cube
	answer += (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * amt
print(answer)
