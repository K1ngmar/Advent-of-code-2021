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

class Octopus:
	flashes = 0

	def __init__(self, nbr):
		self.nbr = nbr
		self.flashed = False
	
	def increase(self):
		if self.flashed == False:
			self.nbr += 1
			if self.nbr > 9:
				self.do_flash()
				return True
		return False
	
	def do_flash(self):
		self.nbr = 0
		self.flashed = True
		Octopus.flashes += 1

def reset_octipi_flash():
	for y in range(len(octipi)):
		for x in range(len(octipi[y])):
			octipi[y][x].flashed = False

def octopus_flash(x, y):
	if (x < 0 or y < 0 or y >= len(octipi) or x >= len(octipi[y])):
		return
	if octipi[y][x].increase() == True:
		octopus_flash(x + 1, y + 1)
		octopus_flash(x + 1, y)
		octopus_flash(x, y + 1)
		octopus_flash(x - 1, y + 1)
		octopus_flash(x + 1, y - 1)
		octopus_flash(x - 1, y - 1)
		octopus_flash(x - 1, y)
		octopus_flash(x, y - 1)

def check_flashed():
	for y in range(len(octipi)):
		for x in range(len(octipi[y])):
			if octipi[y][x].flashed == False:
				return False
	return True
def simulate():
	step = 0
	while check_flashed() == False:
		reset_octipi_flash()
		for y in range(len(octipi)):
			for x in range(len(octipi[y])):
				octopus_flash(x, y)
		step += 1
	print(step)

octipi = [[Octopus(int(y)) for y in x] for x in open("d11.input").read().split()]
simulate()
