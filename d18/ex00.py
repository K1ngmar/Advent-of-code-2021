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

from math import floor, ceil
from itertools import permutations
from copy import deepcopy

lines = [x for x in open("d18.input").read().split()]

class Node:

	def __init__(self, val = None, parent = None):
		self.val	= val
		self.left	= None
		self.right	= None
		self.parent	= parent

	def __str__(self):
		if isinstance(self.val, int):
			return str(self.val)
		return f"[{str(self.left)},{str(self.right)}]"

def magnitude(x):
	if x.val != None:
		return x.val
	return 3 * magnitude(x.left) + 2 * magnitude(x.right)

def make_tree(line, root):
	global idx

	while idx < len(line):
		if line[idx] == ",":
			idx += 1
		if line[idx] == "[":
			idx += 1
			root.left = make_tree(line, Node(None, root))
			root.right = make_tree(line, Node(None, root))
			return root
		elif line[idx] == "]":
			idx += 1
		else:
			root.val = int(line[idx:idx+1])
			idx += 1
			return root
	return root
	
def combine(x, y):
	root = Node()
	root.left = x
	root.right = y
	x.parent = root
	y.parent = root
	return root

def epic_explosions(x):
	global fml

	if x.left == None or x.right == None:
		return
	if x.left.val == None or x.right.val == None:
		return
	fml = True
	# do explosion stuff
	epic_left_explosion(x.left)
	epic_right_explosion(x.right)

	# destroy old node
	x.val = 0
	x.left = None
	x.right = None

def epic_left_explosion(x):
	tmp	= x.parent
	prev = x

	# go up until you can go left
	while tmp != None and tmp.left == prev:
		prev = tmp
		tmp = tmp.parent

	# if not root, go left once then go all the way right
	if tmp != None:
		tmp = tmp.left
		while tmp.right != None:
			tmp = tmp.right
		tmp.val += x.val

def epic_right_explosion(x):
	tmp		= x.parent
	prev	= x

	# go up until you can go right
	while tmp != None and tmp.right == prev:
		prev = tmp
		tmp = tmp.parent

	# if not root, go right once then go all the way left
	if tmp != None:
		tmp = tmp.right
		while tmp.left != None:
			tmp = tmp.left
		tmp.val += x.val


def who_to_explode(x, depth = 0):
	if x == None:
		return
	if depth >= 4:
		epic_explosions(x)
	else:
		who_to_explode(x.left, depth + 1)
		who_to_explode(x.right, depth + 1)

def split_them_values(x):
	global gvd

	if x == None or gvd == True:
		return
	split_them_values(x.left)

	if x.val != None and x.val >= 10:
		x.left = Node(floor(x.val / 2), x)
		x.right = Node(ceil(x.val / 2), x)
		x.val = None
		gvd = True

	split_them_values(x.right)
			
trees = []
for line in lines:
	idx = 0
	trees.append(make_tree(line, Node()))

gvd = True
def fuckMyLife(trees):
	global gvd

	final = trees[0]
	for i in range(1, len(trees)):
		final = combine(final, trees[i])
		gvd = True
		while gvd == True:
			fml = True
			while fml == True:
				fml = False
				who_to_explode(final)
			gvd = False
			split_them_values(final)
	return final

def iHateThis(trees):
	fuckdezedag = permutations(trees, 2)
	highest = 0
	for item in fuckdezedag:
		hell = deepcopy(item)
		tmp = magnitude(fuckMyLife(hell))
		if tmp > highest:
			highest = tmp
	return highest

print("ex00:", magnitude(fuckMyLife(deepcopy(trees))))
print("ex01:", iHateThis(deepcopy(trees)))
