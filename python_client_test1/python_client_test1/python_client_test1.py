from uuid import getnode as get_mac
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2020))
#s.connect(('localhost', 135))
#s.connect(('localhost', 139))
mac = get_mac()
output=str(mac)+","+"helloooooo"
print("Encoded value",output.encode('utf-8'))
a=output.encode('utf-8')
print("Decoded value",a.decode('utf-8'))
#s.sendall(output.encode('utf-8','ignore'))
s.sendall(output.encode())
#s.send(output)
#s.sendall('Hello, world')
data = s.recv(8000)
#receive.decode('utf_8')    -- might not be needed
s.close()
#new_data=data.decode('utf-8')
#new_data1=data.encode('utf-8')
#print ('Received', repr(data))
#print ('Decoded trial 1: ',new_data)
#print ('Decoded trial 1: ',new_data1)
print ('Received', repr(data.decode('utf-8')))

