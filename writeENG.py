from transTools import *

video = getVideo()
English = 'English '+video+'.srt'
videoTitle = video+'.mp4'

English = getLines(English)
Chinese = []

outputfile = open(video+'.ass','w')
writeStart(outputfile,video,highQual=True) # use highQual=False for 720 qual vids

writeSubs(Chinese,English,outputfile)
outputfile.close()
