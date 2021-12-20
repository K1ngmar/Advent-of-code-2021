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

from math import sqrt
from itertools import permutations

lines = [[y for y in x.split()] for x in open("d19.input").read().split("\n\n")]

for i in range(len(lines)):
	lines[i] = lines[i][4:]

class Coordinate:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def draaien_met_die_hap(self, idx):
		x = self.x
		y = self.y
		z = self.z
		
		return [
			(+x, +y, +z), (+y, +z, +x), (+z, +x, +y),
			(+z, +y, -x), (+y, +x, -z), (+x, +z, -y),
			(+x, -y, -z), (+y, -z, -x), (+z, -x, -y),
			(+z, -y, +x), (+y, -x, +z), (+x, -z, +y),
			(-x, +y, -z), (-y, +z, -x), (-z, +x, -y),
			(-z, +y, +x), (-y, +x, +z), (-x, +z, +y),
			(-x, -y, +z), (-y, -z, +x), (-z, -x, +y),
			(-z, -y, -x), (-y, -x, -z), (-x, -z, -y)
		][idx]

	def __str__(self):
		return f" x: {str(self.x)},  \ty: {str(self.y)},  \tz: {str(self.z)}"

class Scanner:

	def __init__(self, beacons):
		self.beacons = []
		self.x = None
		self.y = None
		self.z = None
		self.r = None
		self.fixed = []

		for beacon in beacons:
			i = 0
			x,y,z = [int(i) for i in beacon.split(",")]
			self.beacons.append(Coordinate(x, y, z))
	
	def create_fixed(self):
		for beacon in self.beacons:
			self.fixed.append((beacon.x, beacon.y, beacon.z))
	
	def alles_moet_omgegooid_worden(self, mod):
		for beacon in self.beacons:
			x,y,z = beacon.draaien_met_die_hap(self.r)
			beacon.x = x + mod[0]
			beacon.y = y + mod[1]
			beacon.z = z + mod[2]

	def setpos(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]

	def __str__(self):
		ret = "Scanner:\n"
		for beacon in self.beacons:
			ret += str(beacon) + "\n"
		return ret

scanners = []
for line in lines:
	scanners.append(Scanner(line))

fixed = [scanners[0]]
fixed[0].x = 0
fixed[0].y = 0
fixed[0].z = 0
fixed[0].r = 0
fixed[0].create_fixed()
scanners.pop(0)

def ismatch(fixed, to_be_matched):

	distance = {}
	for p1 in fixed:
		for p2 in to_be_matched:
			d = (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])
			if d in distance:
				distance[d] += 1
			else:
				distance[d] = 1
	for key, value in distance.items():
		if value >= 12:
			return (True, key)
	return (False, None)

def dit_werkt_voor_geen_meter(fixed, unmatched):

	for scanner in unmatched:
		for r in range(24):
			points = []
			for beacon in scanner.beacons:
				points.append(beacon.draaien_met_die_hap(r))
			for fix in fixed:
				match = ismatch(fix.fixed, points)
				if match[0] == True:
					scanner.r = r
					scanner.setpos(match[1])
					scanner.alles_moet_omgegooid_worden(match[1])
					scanner.create_fixed()
					fixed.append(scanner)
					unmatched.remove(scanner)
					return

while len(scanners) > 0:
	dit_werkt_voor_geen_meter(fixed, scanners)

woop = set()
for fix in fixed:
	for f in fix.fixed:
		woop.add(f)

print(len(woop))

distances = set()
fml = permutations(fixed, 2)
for p1, p2 in fml:
	distances.add(abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z))

print(max(distances))
