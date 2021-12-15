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

grid = [[int(y) for y in x] for x in open("d15.input").read().split()]

goal = (len(grid[0]) - 1, len(grid) - 1)

ans = 420691337

visited = {}

pos = (0,0)
def calc_paths(x, y, count):
	global ans
	global grid
	global goal
	if count > ans:
		return
	pos = (x, y)
	count += grid[y][x]
	if pos not in visited.keys():
		visited[pos] = count
	elif visited[pos] > count:
		visited[pos] = count
	else:
		return 
	if x == goal[0] and y == goal[1]:
		if count < ans:
			ans = count
	if x < goal[0]:
		calc_paths(x + 1, y, count)
	if y < goal[1]:
		calc_paths(x, y + 1, count)
	if x > 0:
		calc_paths(x - 1, y, count)
	if y > 0:
		calc_paths(x, y - 1, count)

calc_paths(0,0,0 - grid[0][0])

print(ans)