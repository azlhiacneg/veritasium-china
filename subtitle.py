from transTools import *

video = getVideo()
Chinese = getCHNFile()
English = getENGFile()

English = getLines(English)
Chinese = getLines(Chinese)

outputfile = open(video+'.ass','w')
writeStart(outputfile,video) # use highQual=False for 720 qual vids

writeSubs(Chinese,English,outputfile)
outputfile.close()
