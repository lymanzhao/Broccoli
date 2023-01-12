from brocTask import blenderender
import os
import sys
from pathlib import Path
# import threading

blender = 'D:/PortableApps/blender-2.92.0-windows64/blender.exe -b '
startframe = int(10)
endframe = int(12)
blenderfile = "D:/GitHub/Broccoli/to_encode/Blender290.blend"
renderfile = "//render/####.png"

for rangeframe in range(startframe,endframe):
    # str(rangeframe)
    blenderendering = str(blender + blenderfile + ' -E CYCLES -s ' +
                          str(rangeframe) + ' -e ' + str(rangeframe) + ' -a -o ' + renderfile)
# blenderendering = 'D:/PortableApps/blender-2.92.0-windows64/blender.exe -b "D:/GitHub/Broccoli/to_encode/Blender290.blend" -E CYCLES -s 1 -e 2 -a -o "//render/####.png" --cycles-device CUDA'
    # thread = threading.Thread(target=blenderender, args=(
    #     blenderendering,))
    # thread.start()

if __name__ == "__main__":
    blenderender.delay(blenderendering)
