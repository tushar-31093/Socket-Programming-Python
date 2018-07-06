from winreg import *

Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
#RawKey = OpenKey(Registry, "SOFTWARE\Microsoft\Windows NT\CurrentVersion")
#RawKey = OpenKey(Registry, "SOFTWARE\Classes")
#RawKey = OpenKey(Registry, "SOFTWARE\Microsoft\Ole")
RawKey = OpenKey(Registry, "SYSTEM\CurrentControlSet\Control\hivelist")

#HKEY_LOCAL_MACHINE \SYSTEM : \system32\config\system
#HKEY_LOCAL_MACHINE \SAM : \system32\config\sam
#HKEY_LOCAL_MACHINE \SECURITY : \system32\config\security
#HKEY_LOCAL_MACHINE \SOFTWARE : \system32\config\software
#HKEY_USERS \UserProfile :  \winnt\profiles\username
#HKEY_USERS.DEFAULT : \system32\config\default


print(RawKey)

try:
    i = 0
    while 1:
        name, value, type = EnumValue(RawKey, i)
        print(name, value, i)
        i += 1
except WindowsError:
    print("Windows error occured")