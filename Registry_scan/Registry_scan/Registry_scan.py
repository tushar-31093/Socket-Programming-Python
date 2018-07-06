import errno, os, winreg
proc_arch = os.environ['PROCESSOR_ARCHITECTURE'].lower()
#proc_arch64 = os.environ['PROCESSOR_ARCHITEW6432'].lower()

if proc_arch == 'x86' and not proc_arch64:
    arch_keys = {0}
elif proc_arch == 'x86' or proc_arch == 'amd64':
    arch_keys = {winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY}
else:
    raise Exception("Unhandled arch: %s" % proc_arch)

for arch_key in arch_keys:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | arch_key)
    for i in range(0, winreg.QueryInfoKey(key)[0]):
        print("The Key for the prog. is :",key)
        skey_name = winreg.EnumKey(key, i)
        skey = winreg.OpenKey(key, skey_name)
        try:
            print(winreg.QueryValueEx(skey, 'DisplayName')[0])
        except OSError as e:
            if e.errno == errno.ENOENT:
                # DisplayName doesn't exist in this skey
                pass
        finally:
            skey.Close()