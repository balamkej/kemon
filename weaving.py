import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def mushingIndex(treadleRow):
    return [i for i, j in enumerate(treadleRow) if j == 1]

def mushing(threading,treadleRow):
    row = np.zeros(len(threading[0]), int)
    for i in mushingIndex(treadleRow):
        row = row + threading[i]
        np.clip(row,0,1,row)
    return row

def mushing2(treadleRow,tieup):
    row = np.zeros(len(tieup[:,0]), int)
    for i in mushingIndex(treadleRow):
        row = row + tieup[:,i]
        np.clip(row,0,1,row)
    return row

def weave(treadle, threading, tieup):
    pattern = np.zeros((len(treadle[:,0]),len(threading[0])), int)
    for i in range(len(treadle[:,0])):
        pattern[i] = mushing(threading, mushing2(treadle[i],tieup))
    return pattern

        
#            treadleArray = np.genfromtxt(treadle, delimiter=",")
#            treadleArray = np.nan_to_num(treadleArray)
#            threadingArray = np.genfromtxt(threading, delimiter=",")
#            threadingArray = np.nan_to_num(threadingArray)
#            tieupArray = np.genfromtxt(tieup, delimiter=",")
#            tieupArray = np.nan_to_num(tieupArray)
#            if request.form.get('Rotate') != None: 
#                treadleArray = np.rot90(treadleArray)
#            weaving = weave(treadleArray,threadingArray,tieupArray)
#            plt.imsave('uploads/' + outname + '.png', weaving, cmap=cm.gray)
