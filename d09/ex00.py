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

nbr = [[int(y) for y in x] for x in open("d09.input").read().splitlines()]

def check_neighbours(x, y):
	n = nbr[y][x]
	if x > 0 and nbr[y][x - 1] <= n:
		return False
	if x < len(nbr[y]) - 1 and nbr[y][x + 1] <= n:
		return False
	if y > 0 and nbr[y - 1][x] <= n:
		return False
	if y < len(nbr) - 1 and nbr[y + 1][x] <= n:
		return False
	return True

count = 0
for y in range(len(nbr)):
	for x in range(len(nbr[y])):
		if check_neighbours(x, y) == True:
			count += nbr[y][x] + 1

print(count)
