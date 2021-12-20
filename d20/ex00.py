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

algo, ref = open("d20.input").read().split("\n\n")

img = ref.split()

litty = set()
for y, l in enumerate(img):
	for x, c in enumerate(l):
		if c == "#":
			litty.add((x, y))

def make_binary(algo, litty, i, new, x, xmin, xmax, y, ymin, ymax):
	binary = ""
	for my in range(-1, 2):
		for mx in range(-1, 2):
			if xmin <= mx + x <= xmax and  ymin <= my + y <= ymax :
				binary += str(int((x + mx, y + my) in litty))
			else:
				binary += str(int(i % 2 == 1))

	if algo[int(binary, 2)] == "#":
		new.add((x, y))

def simulate(litty, algo, amt):
	for i in range(amt):
		new = set()
		
		xmin = min([p[0] for p in litty])
		xmax = max([p[0] for p in litty])
		ymin = min([p[1] for p in litty])
		ymax = max([p[1] for p in litty])

		for x in range(xmin - 1, xmax + 2):
			for y in range(ymin - 1, ymax + 2):
				make_binary(algo, litty, i, new, x, xmin, xmax, y, ymin, ymax)
		litty = new

	print(len(litty))

simulate(litty, algo, 50)
