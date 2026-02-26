import ctypes
import time

# Constantes de Windows
ES_CONTINUOUS = 0x80000000
ES_DISPLAY_REQUIRED = 0x00000002

def keep_screen_awake():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_DISPLAY_REQUIRED
    )

while True:
    keep_screen_awake()
    time.sleep(60)