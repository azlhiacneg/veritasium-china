from transTools import *
import os

os.system('python CHNconv.py')
os.system('python ENGconv.py')
video = getVideo()
Chinese = 'Chinese.srt'
English = 'English.srt'

CHNlines = getLines(Chinese)
ENGlines = getLines(English)

title = video + '_new.ass'
newFormat = open(title,'w')
writeStart(newFormat,video)
writeSubsNew(CHNlines,ENGlines,newFormat)
newFormat.close()
