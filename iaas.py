#!/usr/bin/python2

import  cgi,cgitb,os,commands,time
import mysql.connector as mariadb

cgitb.enable()	#enable the exception handler

#print  "Content-type:text/html"		#To tell the client what kind of data is following, here HTML
#print  ""				#blank line, end of headers

web=cgi.FieldStorage()	#FieldStorage class to get at submitted form data

mariadb_connection = mariadb.connect(user='root', password='', database='cloud_project')
cursor = mariadb_connection.cursor()
if "vmlaunch" not in web:			#change1 redhat --> vmlaunch
	username=web.getvalue('uname')+""
	password=web.getvalue('psw')+""
	cursor.execute("SELECT * FROM login where username=%s AND password=%s",(username,password));
	flag=len(cursor.fetchall())
	if flag == 1:
		url = '<meta http-equiv = "refresh" content = "5; url = http://www.localhost.localdomain/dashboard.html?username='+username+'" />'
		#change2 concatenating username as link parameter in the url
		print "Content-type:text/html"
		print ""
		print "<html>"
		print "<body>"
		print "<h1>Redirecting...</h1>"
		print url	# change3 printing url variable
		print "</body>"
		print "</html>"
	else:
		print "Location: http://www.localhost.localdomain/", "\n\n";
else:
	username = web.getvalue('username')
	print "Content-type:text/html"
	print ""
	print "OS Preparing",username
	cursor.execute("SELECT location FROM vm where username=%s",(username));
	address=cursor.fetchall()[0]
	print "Redirecting"
	print '<meta http-equiv = "refresh" content = "5; url ='+ address+" />'
	


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





