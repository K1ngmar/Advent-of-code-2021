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

template,lines = open("d14.input").read().split("\n\n")

lines = [x for x in lines.splitlines()]
transformations = dict()
occurrences = dict()
pairs = dict()

for line in lines:
	key,value = line.split(" -> ")
	transformations[key] = [value, key[:1] + value, value + key[1:]]
	occurrences[value] = 0
	pairs[key] = 0

for i in range(len(template) - 1):
	pairs[template[i:i + 2]] += 1
	occurrences[template[i:i+1]] += 1
occurrences[template[len(template)-1:len(template)]] += 1

def generate_steps(ex, steps):
	occur = occurrences.copy()
	trans = transformations.copy()
	pr = pairs.copy()
	for _ in range(steps):
		copy = pr.copy()
		for pair in copy:
			if copy[pair] > 0:
				transformer = transformations[pair]
				cp = copy[pair]
				pr[transformer[1]] += cp
				pr[transformer[2]] += cp
				occur[transformer[0]] += cp
				pr[pair] -= cp
	print(max(occur.values()) - min(occur.values()))

generate_steps("ex00:", 10)
generate_steps("ex01:", 40)
