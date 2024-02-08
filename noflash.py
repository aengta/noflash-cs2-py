import pymem
import pymem.process

pm = pymem.Pymem("cs2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

while True:
    localPlayer = pm.read_longlong(client + 0x16BC5B8)

    # NoFlash
    flashDur = pm.read_int(localPlayer + 0x1468)

    if flashDur > 0:
        pm.write_int(localPlayer + 0x1468, 0)
