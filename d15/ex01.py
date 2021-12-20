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

from queue import PriorityQueue

def dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def mario_is_going_to_be_jealous_of_a_star(grid):
	start = (0, 0)
	target = (len(grid[0]) - 1, len(grid) - 1)

	cur = PriorityQueue()
	cur.put((0, start))
	visited = {start: None}
	risk = {start: 0}

	pos = None
	while not cur.empty():
		pos = cur.get()[1]

		if pos == target:
			break

		for neighbor in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			new_pos = (pos[0] + neighbor[0], pos[1] + neighbor[1])

			if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
				new_risk = risk[pos] + grid[new_pos[1]][new_pos[0]]

				if new_pos not in visited or new_risk < risk[new_pos]:
					risk[new_pos] = new_risk
					rating = new_risk + dist(new_pos, target)
					cur.put((rating, new_pos))
					visited[new_pos] = pos

	return risk[pos]

grid = [[int(y) for y in x] for x in open("d15.input").read().split()]

def expand(grid):
	ogheight = len(grid)
	ogwidth = len(grid[0])
	expanded = [[0 for _ in range(ogwidth * 5)] for _ in range(ogheight * 5)]
	for y in range(5):
		for x in range(5):
			for i in range(ogheight):
				for j in range(ogwidth):
					expanded[y * ogheight + i][x * ogwidth + j] = grid[i][j] + x + y
					if expanded[y * ogheight + i][x * ogwidth + j] >= 10:
						expanded[y * ogheight + i][x * ogwidth + j] -= 9
	return expanded
					
expanded = expand(grid)

path = mario_is_going_to_be_jealous_of_a_star(expanded)
print(path)
