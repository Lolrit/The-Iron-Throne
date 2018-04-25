from time import time
import threading
#Imports
#Team modules


wait_Tkint=0
wait_Citidel=0
wait_Davos=0
wait_Lang=0
wait_Mel=0
wait_LF=0

def call_council():

    start_time=time()
    def get_Tkint():
        a=time()
        global wait_Tkint
        from Tkint import Tkint
        wait_Tkint=Tkint
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nTkint time log- '+str(time()-a))
    getting_Tkint=threading.Thread(target=get_Tkint)
    getting_Tkint.start()
    def get_Citidel():
        a=time()
        global wait_Citidel
        from Citidel import Citidel
        wait_Citidel=Citidel
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nCitidel time log- '+str(time()-a))
    getting_Citidel=threading.Thread(target=get_Citidel)
    getting_Citidel.start()
    def get_Lang():
        a=time()
        global wait_Lang
        from High_Valyrian import The_Language
        wait_Lang=The_Language
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nLanguage time log- '+str(time()-a))
    getting_Lang=threading.Thread(target=get_Lang)
    getting_Lang.start()
    def get_Davos():
        a=time()
        global wait_Davos
        from Davos import Davos
        wait_Davos=Davos
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nDavos time log- '+str(time()-a))
    getting_Davos=threading.Thread(target=get_Davos)
    getting_Davos.start()
    def get_Mel():
        a=time()
        global wait_Mel
        from Mel import Mel
        wait_Mel=Mel
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nMel time log- '+str(time()-a))
    getting_Mel=threading.Thread(target=get_Mel)
    getting_Mel.start()
    def get_LF():
        a=time()
        global wait_LF
        from LittleFinger import LittleFinger
        wait_LF=LittleFinger
        with open('Logger//Time_log.txt','a') as f:
            f.write('\nLittleFinger time log- '+str(time()-a))
    getting_LF=threading.Thread(target=get_LF)
    getting_LF.start()

    getting_Citidel.join()
    Citidel=wait_Citidel
    getting_Mel.join()
    Mel=wait_Mel
    getting_Lang.join()
    The_Language=wait_Lang
    getting_Tkint.join()
    Tkint=wait_Tkint
    getting_Davos.join()
    Davos=wait_Davos
    getting_LF.join()
    LittleFinger=wait_LF

    with open('Logger//Time_log.txt','a') as f:
        f.write('\nTotal time log- '+str(time()-start_time)+'\n\n\n')


    return Citidel,Mel,The_Language,Tkint,Davos,LittleFinger