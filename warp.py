from googletrans import Translator

tr = Translator()
def warp_once(text): # this is the script to run text through google translate once
    stg1 = tr.translate(text, dest="es",src="en")
    stg2 = tr.translate(stg1.text, dest="la",src="es")
    stg3 = tr.translate(stg2.text, dest="ja",src="la")
    stg4 = tr.translate(stg3.text, dest="hr",src="ja")
    stg5 = tr.translate(stg4.text, dest="en",src="hr")
    return stg5.text
        
def warp(text,times): # this script is used to warp the text multiple times
    for index in range(times):
        if (index==0):
            L = warp_once(text)
        else:
            L = warp_once(L)
    return L

use_example = True # change to false if you want to use this as a module
if (use_example == True):
    text = input('Text to warp: ')
    times = int(input('The power of the warp: '))
    warptext = warp(text,times)
    print(warptext)
