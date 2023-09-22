import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)
print("Listening...")

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == " ":
         subprocess.call(["termux-tts-speak"," "])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hey" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hello neon" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "hey neon" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "love you" in inp:
         subprocess.call(["termux-tts-speak","ohh Really,me too"])
         
     elif "Love you" in inp:
         subprocess.call(["termux-tts-speak","ohh Really,me too"])
         
     elif "I love you" in inp:
         subprocess.call(["termux-tts-speak","ohh Really,me too"])
         
     elif "i love you" in inp:
         subprocess.call(["termux-tts-speak","ohh Really,me too"])
         
     elif "Sorry" in inp:
         subprocess.call(["termux-tts-speak","No need of that , its okay"])
     
     elif "sorry" in inp:
         subprocess.call(["termux-tts-speak","No need of that , its okay"])
     
     elif "I am sorry" in inp:
         subprocess.call(["termux-tts-speak","No need of that , its okay"])
     
     elif "i am sorry" in inp:
         subprocess.call(["termux-tts-speak","No need of that , its okay"])
         
     elif "that not for you" in inp:
         subprocess.call(["termux-tts-speak","Okay , I am sorry"])
     
     elif "its not for you" in inp:
         subprocess.call(["termux-tts-speak","Okay , I am sorry"])
         
     elif "not for you" in inp:
         subprocess.call(["termux-tts-speak","Okay , I am sorry"])
         
     elif "I will fuck you" in inp:
         subprocess.call(["termux-tts-speak"," But programs can't you fuck"])
      
     elif "fuck you" in inp:
         subprocess.call(["termux-tts-speak"," But programs can't you fuck"])
      
     elif "Fuck you" in inp:
         subprocess.call(["termux-tts-speak"," But programs can't you fuck"])
      
     elif "thank you so much" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
    
     elif "Thank you" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
     
     elif "thank you" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
      
     elif "Thank you so much" in inp:
         subprocess.call(["termux-tts-speak","You're welcome,sir "])
      
     elif "Shut Down" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         
     elif "shutdown" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         
     elif "shut down" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
         
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","I am good sir, how was the your day "])
        
     elif "day is just started" in inp:
        subprocess.call(["termux-tts-speak","oohh I think you will enjoy your day,sir "])
        
     elif "its going good" in inp:
        subprocess.call(["termux-tts-speak","oohh great"])
        
     elif "show battery status" in inp:
         subprocess.call(["termux-battery-status"])
    
     elif "show battery" in inp:
         subprocess.call(["termux-battery-status"])
    
     elif "tell me about battery" in inp:
         subprocess.call(["termux-battery-status"])
    
     elif "go on sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "goto sleep mode" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)

     elif "goto sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
      
     elif "make a call" in inp:
         os.system("termux-telephony-call +91")
         
     elif "call my Mom" in inp:
         os.system("termux-telephony-call 9021016359")
         
     elif "call my mom" in inp:
         os.system("termux-telephony-call 9021016359")
         
     elif "call my Papa" in inp:
         os.system("termux-telephony-call 7057593627")
         
     elif "call my Papa" in inp:
         os.system("termux-telephony-call 7057593627")
         
     elif "flashlight" in inp:
         os.system("termux-torch on")
     
     elif "turn on torch" in inp:
         os.system("termux-torch on")
     elif "turn off torch" in inp:
         os.system("termux-torch off")
         
     elif "torch off" in inp:
         os.system("termux-torch on")
     elif "torch on" in inp:
         os.system("termux-torch off")
    
     elif "then on torch" in inp:
         os.system("termux-torch on")
     elif "then off torch" in inp:
         os.system("termux-torch off")
         
     elif "Then on torch" in inp:
         os.system("termux-torch on")
     elif "Then off torch" in inp:
         os.system("termux-torch off")
         
     elif "turn on flashlight" in inp:
         os.system("termux-torch on")
     elif "turn off flashlight" in inp:
         os.system("termux-torch off")
         
     elif "flashlight off" in inp:
         os.system("termux-torch on")
     elif "flashlight on" in inp:
         os.system("termux-torch off")
    
     elif "then on flashlight" in inp:
         os.system("termux-torch on")
     elif "then off flashlight" in inp:
         os.system("termux-torch off")
         
     elif "Then on flashlight" in inp:
         os.system("termux-torch on")
     elif "Then off flashlight" in inp:
         os.system("termux-torch off")
         
     elif "done off flashlight" in inp:
         os.system("termux-torch off")
     elif "done off torch" in inp:
         os.system("termux-torch off")
     elif "done on flashlight" in inp:
         os.system("termux-torch off")
     elif "done on torch" in inp:
         os.system("termux-torch off")
      
     elif "open YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "open Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "launch YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "launch Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "view contacts" in inp:
         os.system("termux-contact-list")
     elif "open contacts" in inp:
         os.system("termux-contact-list")
     elif "show me all contacts" in inp:
         os.system("termux-contact-list")
     elif "view contact" in inp:
         os.system("termux-contact-list")
     elif "open contact" in inp:
         os.system("termux-contact-list")
     elif "show me all contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistant Neon"])
         
     elif "what is time" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "tell me time" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "what is timing" in inp:
         subprocess.call(["termux-tts-speak",t])
     elif "tell me timing" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "what is your name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Neon "])
     elif "tell me your name" in inp:
         subprocess.call(["termux-tts-speak","you can call me Neon "])
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","I am edited by Gaurav Prajapati"])
     
     elif "alexa" in inp:
         subprocess.call(["termux-tts-speak","Go and ask to that bitch alexa"])
     elif "siri" in inp:
         subprocess.call(["termux-tts-speak","Go and ask to that bitch siri"])
     elif "Alexa" in inp:
         subprocess.call(["termux-tts-speak","Go and ask to that bitch alexa"])
     elif "Siri" in inp:
         subprocess.call(["termux-tts-speak","Go and ask to that bitch siri"])
       
     
     else:
       subprocess.call(["termux-tts-speak","Please tell me something else I can't understand it"])
 
system()

os.system("python main.py")