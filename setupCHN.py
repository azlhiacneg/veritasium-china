from transTools import *

video = getVideo()
(start, end, ENGsub) = getENG_ass(video +'.ass')

outputname = video + '_new.ass'
output = open(outputname,'w')
writeStart(output,video,highQual=True) # Use highQual = False for 720

for i in range(len(ENGsub)):
    output.write('Dialogue: 0,' + start[i].strip() + ',' + end[i].strip() + ',Chinese,,0,0,0,,' + '\n')
    output.write('Dialogue: 0,' + start[i].strip() + ',' + end[i].strip() + ',English,,0,0,0,,' + ENGsub[i])

output.close()
