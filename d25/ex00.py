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

def check_east_move(x, y):
	if x + 1 >= len(grid[y]):
		return grid[y][0] == "."
	return grid[y][x+1] == "."

def check_south_move(x, y):
	if y + 1 >= len(grid):
		return grid[0][x] == "."
	return grid[y+1][x] == "."

def check_coords(func, match):
	move = set()

	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == match:
				if func(x, y) == True:
					move.add((x, y))
	return move

def move_east(moves):
	global grid

	for x, y in moves:
		if x == len(grid[y]) - 1:
			grid[y] = ">" + grid[y][1:x] + "."
		else:
			grid[y] = grid[y][:x] + ".>" + grid[y][x+2:]
	
def move_south(moves):
	global grid

	for x, y in moves:
		if y == len(grid) - 1:
			grid[0] = grid[0][:x] + "v" + grid[0][x+1:]
		else:
			grid[y+1] = grid[y+1][:x] + "v" + grid[y+1][x+1:]
		grid[y] = grid[y][:x] + "." + grid[y][x+1:]

def print_grid():
	print()
	for line in grid:
		print(line)

grid = open("d25.input").read().split()

itr = 0
while True:
	east = check_coords(check_east_move, ">")
	move_east(east)
	south = check_coords(check_south_move, "v")
	move_south(south)
	itr += 1
	if len(east) + len(south) == 0:
		break

print(itr)
