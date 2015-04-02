from estimation.models import Crazyflie2

# note the state is angular vels
# 0.1576,0.9706,0.9572 -> -0.1160,0.9763,0.9418
# xx = [0.9058,0.1270,0.9134,0.6324,0.0975,0.2785,0.5469,0.9575,0.9649,-0.1160,0.9763,0.9418]
xx = [0.9157,0.7922,0.9595,0.6557,0.0357,0.8491,0.9340,0.6787,0.7577,0.1962,0.8166,0.6289]

uu = [0.4854,0.8003,0.1419,0.4218]

cf = Crazyflie2()

#dyn = cf.dynamics(xx,uu)
#for i in dyn:
#	print i

xf = cf.simulate(xx,uu,.05)
for i in xf:
	print i