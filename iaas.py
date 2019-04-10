#!/usr/bin/python2

import  cgi,cgitb,os,commands,time

cgitb.enable()	#enable the exception handler

#print  "Content-type:text/html"		#To tell the client what kind of data is following, here HTML
#print  ""				#blank line, end of headers

web=cgi.FieldStorage()	#FieldStorage class to get at submitted form data

if "redhat" not in web:
	username=web.getvalue('uname')+""
	password=web.getvalue('psw')+""
	if username == "rashi" and password == "rashi":
		print "Content-type:text/html"
		print ""
		print "<html>"
		print "<body>"
		print "<h1> YOU ARE LOGGED IN</h1>"
		print "</body>"
		print "</html>"
	else:
		print "Location: http://www.localhost.localdomain/", "\n\n";
else:
	#vm=web.getvalue('redhat')
	print "Content-type:text/html"
	print ""
	print "OS Preparing"
	


'''flag=os.path.exists('/var/lib/libvirt/images/'+vm_name+'.qcow2')


if flag:
	print '<pre>'
	print '<h1>'
	print vm_name+" already exits!! try different name \n\n Redirecting to previous page..."
	print '</h1>'
	print '</pre>'
	print '<meta http-equiv = "refresh" content = "5; url = 192.168.119.160" />'
	exit()	
if  os_name ==  "3"  :
	print  os.system('sudo  virt-install  --name '+vm_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk  --cdrom  /ubuntu1610.iso --noautoconsole')

elif  os_name == "2"  :
	print  os.system('sudo  virt-install  --name '+vm_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/osrhel75.qcow2,size='+os_hdd+'  --location ftp://192.168.10.254/pub/rhel75/')

elif  os_name ==  "1"  :
	print "os is prepairing!!"
	port="8041"
	host_port="8042"
	commands.getoutput('sudo  qemu-img   create -f  qcow2 -b  /rhvmdnd.qcow2  /var/lib/libvirt/images/'+vm_name+'.qcow2')
	os.system('sudo  virt-install  --name '+vm_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+vm_name+'.qcow2  		--import  --noautoconsole --os-variant rhel7.5 --graphics=vnc,listen=192.168.119.160,port='+port+',password=redhat123')
	print commands.getoutput('websockify --web=/usr/share/novnc '+host_port+' 192.168.119.160:'+port)
	time.sleep(10)
	print '<a href= "http://192.168.119.160:8042" > Launch VM here</a>' '''

#print '<pre>'
#print commands.getoutput("sudo virsh list --all")
#print '</pre>'





