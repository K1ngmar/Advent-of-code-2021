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

class bingo_card:

	def __init__(self, lines):
		liners = lines.split("\n")
		self.numbers = []
		for line in liners:
			self.numbers.append([int(nbr) for nbr in line.split()])

	def check_number(self, nbr):
		for nb in self.numbers:
			for i in range(len(nb)):
				if nb[i] == nbr:
					nb[i] = -1
					break

	def check_row(self):
		for row in self.numbers:
			count = 0
			for i in range(len(row)):
				if row[i] < 0:
					count += 1
			if count == len(row):
				return True
		return False

	def check_column(self):
		for i in range(len(self.numbers)):
			count = 0
			for j in range(len(self.numbers[i])):
				if self.numbers[j][i] < 0:
					count += 1
			if count == len(self.numbers):
				return True
		return False

	def count_score(self):
		count = 0
		for row in self.numbers:
			for nbr in row:
				if nbr > 0:
					count += nbr
		return count

	def check_bingo(self):
		if self.check_row() == True:
			return True
		return self.check_column()

lines = open("d04.input").read().split("\n\n")

bingo_numbers = [int(x) for x in lines[0].split(",")]

cards = []
for line in lines[1:]:
	cards.append(bingo_card(line))

for number in bingo_numbers:
	for card in cards:
		card.check_number(number)
		if card.check_bingo() == True:
			print(card.count_score() * number)
			exit()
