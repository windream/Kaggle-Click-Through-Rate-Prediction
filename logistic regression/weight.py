# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:50:27 2014

@author: windream
"""

fgbrt = open("/Users/windream/Desktop/project/weight/gbrt","r")
flibfm = open("/Users/windream/Desktop/project/weight/libfm","r")
flr = open("/Users/windream/Desktop/project/weight/lr","r")
fid = open("/Users/windream/Desktop/project/test_ID","r")
fw = open("/Users/windream/Desktop/project/weightpredict","w")

wgbrt = 0.433333333334
wlibfm = 0.433333333333
wlr = 0.133333333333

fw.write("id,click\n")
for cnt in range(4577464):
    dgbrt = fgbrt.readline().strip()
    dlibfm = flibfm.readline().strip()
    dlr = flr.readline().strip()
    did = fid.readline().strip()
    
    res = wgbrt * float(dgbrt) + wlibfm * float(dlibfm) + wlr * float(dlr)
    fw.write(did+','+str(res)+'\n')
    
fgbrt.close()
flibfm.close()
flr.close()
fid.close()
fw.close()