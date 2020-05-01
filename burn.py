from transTools import *

video = getVideo()
sub = video+'_new.ass'
video = video+'.mp4'

os.system('ffmpeg -i "'+video+'" -vf "ass='+sub+'" output.mp4')
# -crf 17 -r 24 -framerate 24

os.system('cp "' +video+ '" 纯英文版.mp4')
os.system('mv output.mp4 中英字幕版.mp4')
