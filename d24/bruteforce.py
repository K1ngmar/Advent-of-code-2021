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
from itertools import product

class ALU:
####        ####
## Operations ##
####        ####

	def inp(self, key, val):
		self.memory[key] = val

	def add(self, reg, val):
		self.memory[reg] += val

	def mul(self, reg, val):
		self.memory[reg] *= val

	def div(self, reg, val):
		self.memory[reg] = self.memory[reg] // val

	def mod(self, reg, val):
		self.memory[reg] = self.memory[reg] % val

	def eql(self, reg, val):
		self.memory[reg] = int(self.memory[reg] == val)

####    ####
# Dispatch #
####    ####

	execute = {
		"inp": inp,
		"add": add,
		"mul": mul,
		"div": div,
		"mod": mod,
		"eql": eql
	}

####       ####
# Constrution #
####       ####

	def __init__(self):
		self.memory = defaultdict(lambda: 0)
		self.memory["w"]
		self.memory["x"]
		self.memory["y"]
		self.memory["z"]
		self.res = None

	def parse(self, line, inp = None):
		operator, *tokens = line.split()
		if len(tokens) > 1:
			tok = tokens[1]
			val = int(tok) if tok.isalpha() == False else self.memory[tok]
			ALU.execute[operator](self, tokens[0], val)
		else:
			self.res = operator
			ALU.execute[operator](self, tokens[0], inp)

lines = open("d24.input").read().splitlines()

possibilities = product("987654321", repeat=14)
for val in possibilities:
	computor = ALU()
	i = 0
	for x in range(14):
		computor.parse(lines[i], int(val[x]))
		i += 1
		for line in lines[i:]:
			if line[:3] == "inp":
				break
			i += 1
			computor.parse(line)
	if computor.memory["z"] == 0:
		print("".join(val))
		quit()
