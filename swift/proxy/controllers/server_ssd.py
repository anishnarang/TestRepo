import socket
#from flush_ssd import *
# from chkdisk import *
import commands
import os
def check(s):
	cmd = "df -h "+s
	output = commands.getoutput(cmd)
	output=output.split()
	#x=os.system("df -h /media/hduser/UUI/")
	x=output[11].strip("%")
	return int(x)

def main():
	f = open('/home/hduser/swift/swift/proxy/controllers/spindowndevices','r')
	s = f.read()
	list_device = s.split('\n')
	list_device.remove('')
	f.close()
	serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serv.bind(('localhost',8888))
	serv.listen(20)
	while True:
		#print "in while"
		conn, addr = serv.accept()
		#print "after accept"
		data = conn.recv(512)
		# print data
		if data == 'start':
			perc = check('/mnt/sdb1/ssd')
		 	if perc > 85:
				for i in list_device:
					print i
				# os.system('mount -t xfs -L %s /srv/node/%s'%(i,i))	
			    #flush()
			    # for i in range(ord('d'),ord('g')):
				# os.system('umount /dev/sd%s'%(chr(i)))
		conn.send('done')


if __name__ == '__main__':
	 main()
