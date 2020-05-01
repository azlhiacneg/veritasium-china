#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes in a YouTube subtile file format and video and generates .txt file with only the script

Created on Fri Aug 17 00:02:18 2018

@author: alicezhang
"""

from transTools import *

video = getVideo()
engSub = 'English '+video+'.srt'
chnSub = 'Chinese '+video+'.srt'

deleteTime(engSub,'EngSubs.txt')
deleteTime(chnSub,'ChnSubs.txt')
