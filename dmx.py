import array
from ola.ClientWrapper import ClientWrapper
dmxwrapper = ClientWrapper()


def DmxSent(state):
	global dmxwrapper
  	dmxwrapper.Stop()

def SendDmx(dmxuniverse, dmxdata):
	global dmxwrapper
	dmxclient = dmxwrapper.Client()
	dmxclient.SendDmx(dmxuniverse, dmxdata, DmxSent)
	dmxwrapper.Run()

dmxuniverse = 1
dmxdata = array.array('B', [11, 5, 25, 32 ,34])

SendDmx(dmxuniverse, dmxdata)