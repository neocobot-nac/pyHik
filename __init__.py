import platform
sysstr = platform.system()
sysbit = platform.architecture()[0]
if sysstr == 'Windows':
    if sysbit == '32bit':
        from .libs.windows.x86.pyhik import *
    if sysbit == '64bit':
        from .libs.windows.x64.pyhik import *
elif sysstr == 'Linux':
    pass
    # if sysbit == '32bit':
    #     from .libs.bit32.libNeoService4c import pyNeoService, Endpos
    # if sysbit == '64bit':
    #     from .libs.bit64.libNeoService4c import pyNeoService, Endpos
