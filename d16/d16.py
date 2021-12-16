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

letterlijk_nul_en_een	= "".join([bin(int(x, 16))[2:].zfill(4) for x in open("d16.input").read().split()[0]])
idx = 0

def letterlijk_plus_impl(letterlijk_voogd):
	value = 0
	for bastard in letterlijk_voogd.children:
		value = value + bastard.kalqleren_met_die_hap()
	return value

def letterlijk_keer_impl(letterlijk_voogd):
	value = 1
	for bastard in letterlijk_voogd.children:
		value = value * bastard.kalqleren_met_die_hap()
	return value

def letterlijk_minimaal_impl(letterlijk_voogd):
	value = 420691337
	for bastard in letterlijk_voogd.children:
		tmp = bastard.kalqleren_met_die_hap()
		if tmp < value:
			value = tmp
	return value

def letterlijk_maximaal_impl(letterlijk_voogd):
	value = 0
	for bastard in letterlijk_voogd.children:
		tmp = bastard.kalqleren_met_die_hap()
		if tmp > value:
			value = tmp
	return value

def letterlijk_letterlijk_impl(letterlijk_voogd):
	return letterlijk_voogd.value

def letterlijk_groter_broer_impl(letterlijk_voogd):
	return letterlijk_voogd.children[0].kalqleren_met_die_hap() > letterlijk_voogd.children[1].kalqleren_met_die_hap()

def letterlijk_niet_groter_impl(letterlijk_voogd):
	return letterlijk_voogd.children[0].kalqleren_met_die_hap() < letterlijk_voogd.children[1].kalqleren_met_die_hap()

def letterlijk_hetzelfde_impl(letterlijk_voogd):
	return letterlijk_voogd.children[0].kalqleren_met_die_hap() == letterlijk_voogd.children[1].kalqleren_met_die_hap()

class LetterlijkEenDoos:

	LETTERLIJK_PLUS			= 0
	LETTERLIJK_KEER			= 1
	LETTERLIJK_MINIMAAL		= 2
	LETTERLIJK_MAXIMAAL		= 3
	LETTERLIJK_LETTERLIJK	= 4
	LETTERLIJK_GROTER_BROER = 5
	LETTERLIJK_NIET_GROTER	= 6
	LETTERLIJK_HETZELFDE	= 7

	LETTERLIJK_EEN_LIJST = [
		letterlijk_plus_impl,
		letterlijk_keer_impl,
		letterlijk_minimaal_impl,
		letterlijk_maximaal_impl,
		letterlijk_letterlijk_impl,
		letterlijk_groter_broer_impl,
		letterlijk_niet_groter_impl,
		letterlijk_hetzelfde_impl
	]

	def __init__(self):
		global idx

		self.value = 0
		self.version = int(letterlijk_nul_en_een[idx:idx+3], 2)
		self.id = int(letterlijk_nul_en_een[idx+3:idx+6], 2)
		idx += 6
		self.children = []
		self.switchboi()

	def switchboi(self):

		if self.id != LetterlijkEenDoos.LETTERLIJK_LETTERLIJK:
			self.letterlijk_niet_literal()
		else:
			self.literal()

	def letterlijk_niet_literal(self):
		global idx

		idx += 1
		if letterlijk_nul_en_een[idx - 1] == "0":
			self.letterlijk_een_onderDoos(15)
		else:
			self.letterlijk_ook_een_onderDoos(11)

	def letterlijk_een_onderDoos(self, inc):
		global idx

		nbsp = int(letterlijk_nul_en_een[idx:idx+inc], 2)
		idx += inc
		tmp = idx
		goal = tmp + nbsp
		while idx < goal:
			self.children.append(LetterlijkEenDoos())

	def letterlijk_ook_een_onderDoos(self, inc):
		global idx

		nosp = int(letterlijk_nul_en_een[idx:idx+inc], 2)
		idx += inc
		for _ in range(nosp):
			self.children.append(LetterlijkEenDoos())

	def literal(self):
		global idx

		bit = "1"
		val = ""
		while bit != "0":
			bit = letterlijk_nul_en_een[idx]
			val += letterlijk_nul_en_een[idx + 1:idx + 5]
			idx += 5
		self.value = int(val, 2)

	def kalqleren_met_die_hap(self):
		return LetterlijkEenDoos.LETTERLIJK_EEN_LIJST[self.id](self)

p = LetterlijkEenDoos()
print(p.kalqleren_met_die_hap())
