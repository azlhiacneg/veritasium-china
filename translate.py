from transTools import *
from googletrans import Translator

translator = Translator()
video = getVideo()
(start, end, ENGsub) = getENG_ass(video +'.ass')

outputname = video + '_new.ass'
output = open(outputname,'w')
writeStart(output,video,highQual=True) # Use highQual = False for 720

for i in range(len(ENGsub)):
    CHNline = translator.translate(ENGsub[i].strip(),dest='zh-cn')
    output.write('Dialogue: 0,' + start[i].strip() + ',' + end[i].strip() + ',Chinese,,0,0,0,,' + CHNline.text + '\n')
    output.write('Dialogue: 0,' + start[i].strip() + ',' + end[i].strip() + ',English,,0,0,0,,' + ENGsub[i])
    print(end[i].strip()) # use as a progress bar

output.close()
