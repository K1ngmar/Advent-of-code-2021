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

class Cord:

	def __init__(self, inp):
		inp = inp.split("=")[1]
		self.top = int(inp.split("..")[1])
		self.bot = int(inp.split("..")[0])

	def aah_its_inside_me(self, x):
		return x <= self.top and x >= self.bot

	def letterlijk_lager(self, y):
		return y < self.bot

e,z = open("d17.input").read().split(",")

goal_x = Cord(e)
goal_y = Cord(z)
highest = 0
hit = []

def Trickshot(xvel, yvel):
	global goal_x
	global goal_y
	global highest
	global hit

	x = 0
	y = 0
	top = 0
	dupx = xvel
	dupy = yvel
	while goal_y.letterlijk_lager(y) == False:
		if goal_x.aah_its_inside_me(x) == True:
			if goal_y.aah_its_inside_me(y) == True:
				if (dupx, dupy) not in hit:
					hit.append((dupx, dupy))
				if top > highest:
					highest = top
		x += xvel
		y += yvel
		if yvel == 0:
			top = y
		if xvel > 0:
			xvel -= 1
		yvel -= 1

for x in range(0, 420):
	for y in range(-420, 420):
		Trickshot(x, y)

print("ex00:", highest)
print("ex01:", len(hit))
