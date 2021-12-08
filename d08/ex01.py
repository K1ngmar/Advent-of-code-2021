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

lines = open("d08.input").read().splitlines()

def contains_characters(haystack, needle):
	for c in needle:
		if c not in haystack:
			return False
	return True

def decode(inp):
	code = dict()
	for x in inp:
		if (len(x) == 2):
			code[1] = x
		elif (len(x) == 3):
			code[7] = x
		elif (len(x) == 4):
			code[4] = x
		elif (len(x) == 6):
			# its either 0, 9 or 6
			if contains_characters(x, code[1]):
				if contains_characters(x, code[4]):
					code[9] = x
				else:
					code[0] = x
			else:
				code[6] = x
		elif (len(x) == 5):
			# its either 2, 3 or 5
			if contains_characters(x, code[7]):
				code[3] = x
			elif contains_characters(code[6], x):
				code[5] = x
			else:
				code[2] = x
		elif (len(x) == 7):
			code[8] = x
	return {code[k]:k for k in code}


ret = 0
for line in lines:
	sig, out = line.split("|")
	sig = sorted(["".join(sorted(i)) for i in sig.split()], key=lambda l: len(l))
	out = ["".join(sorted(i)) for i in out.split()]
	# dont question this
	for i in range(3):
		tmp = sig[3 + i]
		sig[3 + i] = sig[6 + i]
		sig[6 + i] = tmp
	code = decode(sig)

	nbr = 0
	for n in out:
		nbr = nbr * 10 + code[n]
	ret += nbr

print(ret)
