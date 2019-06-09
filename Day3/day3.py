#!/usr/bin/python3
#  now importing  time library 
import  webbrowser 
import  time
import  subprocess
import os
import youtube
import search
option='''
Press  1  to  start  your  vlc  media player :
Press  2  to  play your fav song in youtube :  
Press  3  to  search something  on google   :  
Press  4  to send whatsapp message to your fav number  :  
Press  5  to  check current  time and date  :
press  6  to reboot your machine  : 
'''
print(option)

#  taking  input from  user  
#  1 st
choice=input()
#  input function will take input in str  format 
#   conditional  state
if   choice  ==   '5' :
    #   to connect  our BIOS  time 
    current_time=time.ctime()
    print(current_time)

elif  choice  ==  '1'  :
    #   to connect  os level application we use subprocess 
    subprocess.getoutput('vlc')

elif choice == '6'  :
    # System call
    exe = 'reboot'
    os.system(exe)

elif choice == '2' : 
    Data=input("type your search :--->")
    url=[]
    for i in search(Data,stop=5):
        print(i)
        time.sleep(1)
        url.appent(i)
    
    #webbrowser.open_new("https://www.youtube.com/results?search_query="+Data)


elif  choice  ==  '3' :
    data=input("type your search :--->  ")
    webbrowser.open_new_tab('https://www.google.com/search?q='+data)
else  :
    print("hiiii")




