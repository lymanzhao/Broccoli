from brocTask import encoding
ffmpegcmd = 'D:/GitHub/Broccoli/bin/ffmpeg.exe -y -i "D:/GitHub/Broccoli/to_encode/Tom.and.Jerry.2021.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-NWD.mkv" -c copy "D:/GitHub/Broccoli/encoded/Tom.and.Jerry.2021.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-NWD.mp4" '

if __name__ == "__main__":
    encoding.delay(ffmpegcmd)
