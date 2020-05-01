from transTools import *

video = getVideo()
videoTitle = video+'.mp4'

os.system('ffmpeg -i "'+videoTitle+'" -vf "ass='+video+'.ass'+'" ENGsub.mp4')
