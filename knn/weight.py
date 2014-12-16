# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:50:27 2014

@author: windream
"""

fgbrt = open("../ensemble/gbrt.sdx","r")
flibfm = open("../ensemble/libfm.sdx","r")
flr = open("../ensemble/lr.sdx","r")
fid = open("test_ID","r")
fw = open("weightpredict","w")

fw.write("id,click\n")
for cnt in range(4577464):
    dgbrt = fgbrt.readline().strip()
    dlibfm = flibfm.readline().strip()
    dlr = flr.readline().strip()
    did = fid.readline().strip()
    l = [float(dgbrt), float(dlibfm), float(dlr)]
    ans = 0.40 * l[0] + 0.45 * l[1] + 0.15 * l[2]
    
    fw.write(did+','+str(ans)+'\n')
    
fgbrt.close()
flibfm.close()
flr.close()
fid.close()
fw.close()
