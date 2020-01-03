from googletrans import Translator

# v2.1
GTSW_version = 2.0
tr = Translator()
def warp_once(text): # this is the script to run text through google translate once
    stg1 = tr.translate(text, dest="es",src="en")
    stg2 = tr.translate(stg1.text, dest="la",src="es")
    stg3 = tr.translate(stg2.text, dest="ja",src="la")
    stg4 = tr.translate(stg3.text, dest="hr",src="ja")
    stg5 = tr.translate(stg4.text, dest="en",src="hr")
    return stg5.text
        
def warpstat(text,times): # this script is used to warp the text multiple times with status updates
    for index in range(times):
        if (index==0):
            L = warp_once(text)
            print('Warped 1 time' )
        else:
            L = warp_once(L)
            print('Warped '+ str(int(index)+1)+' times' )
    return L
    
def warp(text,times): # this script is used to warp the text multiple times without status updates
    for index in range(times):
        if (index==0):
            L = warp_once(text)
            print('Warped 1 time' )
        else:
            L = warp_once(L)
            print('Warped '+ str(int(index)+1)+' times' )
    return L

use_example = True # change to False if you want to use this as a module
if (use_example == True):
    print('Google Translate String Warp v'+str(GTSW_version))
    text = input('Text to warp: ')
    times = int(input('The power of the warp: '))
    warptext = warpstat(text,times)
    print(warptext)
