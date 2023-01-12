from celery import Celery
import subprocess
# import fileinput
# import eventlet

app = Celery('encoding', broker='redis://localhost:6379/0')


# ffmpegcmd = "ffmpeg -y -i 'D:\GitHub\encoder\to_encode\Tom.and.Jerry.2021.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-NWD.mkv'  -c copy 'D:\GitHub\encoder\encode\Tom.and.Jerry.2021.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-NWD.mkv'"

@app.task
def encoding(ffmpegcmd):
    ffmpegcmdrun = subprocess.Popen(
        ffmpegcmd, shell=True,
        stdout=subprocess.PIPE)
    while ffmpegcmdrun.poll() is None:
        cmdoutput = ffmpegcmdrun.stdout.readline()
        # with open("foo.log", "w") as fo:
        #     fo.write(cmdoutput)
        print (cmdoutput)
        
    # stdout, stderr = ffmpegcmdrun.communicate()
    # print(stdout, stderr)
    # print(ffmpegcmd+'完成')

@app.task
def blenderender(blenderendering):
    blendercmdrun = subprocess.Popen(
        blenderendering, shell=True)
    # stdout, stderr = blendercmdrun.communicate()
    # print(stdout, stderr)
    # print(ffmpegcmd+'完成')
