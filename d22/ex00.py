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

from itertools import product

grid = [[[False for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)]
lines = open("d22.input").read().splitlines()

class Instructions:

	def __init__(self, line):
		l = line.split()
		self.on = True if l[0] == "on" else False
		xd, yd, zd = l[1].split(",")
		xb = [int(q) for q in xd[2:].split("..")]
		self.x = [xb[0] + 50, xb[1] + 50]
		yb = [int(q) for q in yd[2:].split("..")]
		self.y = [yb[0] + 50, yb[1] + 50]
		zb = [int(q) for q in zd[2:].split("..")]
		self.z = [zb[0] + 50, zb[1] + 50]
		self.combinations = product(range(self.x[0], self.x[1] + 1), range(self.y[0], self.y[1] + 1), range(self.z[0], self.z[1] + 1))

	def gridstuff(self, grid):
		if self.x[0] > 100 or self.x[0] < 0 or self.x[1] > 100 or self.x[1] < 0:
			return
		if self.y[0] > 100 or self.y[0] < 0 or self.y[1] > 100 or self.y[1] < 0:
			return
		if self.z[0] > 100 or self.z[0] < 0 or self.z[1] > 100 or self.z[1] < 0:
			return
		for combo in self.combinations:
			grid[combo[0]][combo[1]][combo[2]] = self.on

instructions = []
for line in lines:
	instructions.append(Instructions(line))

for insie in instructions:
	insie.gridstuff(grid)

answ = 0
for x in range(-50, 51):
	for y in range(-50, 51):
		for z in range(-50, 51):
			answ += int(grid[x][y][z])
print(answ)
