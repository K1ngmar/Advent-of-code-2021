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

class Link():

	def __init__(self, key):
		self.key		= key
		self.passed		= False
		self.lowercase	= key.islower()
		self.links		= []
	
	def __str__(self):
		return self.key

	def append(self, link):
		self.links.append(link)

def insert_dict(key, value):
	if key not in links:
		links[key] = Link(key)
	if value not in links:
		links[value] = Link(value)
	if links[value] not in links[key].links:
		links[key].append(links[value])

def path_finding_ofzo(rechts, path):
	path.append(rechts.key)
	rechts.passed = True
	if rechts.key == "end":
		global paths
		print(path)
		paths += 1
	else:
		for boven in rechts.links:
			if boven.lowercase == False or boven.passed == False:
				path_finding_ofzo(boven, path)
	path.pop()
	rechts.passed = False

lines = [x for x in open("d12.input").read().split()]
links = dict()
paths = 0

for line in lines:
	key,value = line.split("-")
	insert_dict(key, value)
	insert_dict(value, key)

# paths = []
path_finding_ofzo(links["start"], [])
print(paths)
# for rechts in links.values():
# 	print(rechts.key, [str(x) for x in rechts.links])
