
from pytube import *
from tkinter import *
from tkinter.filedialog import * 
from tkinter.messagebox import *
from threading import *

#total size container
file_size=0

#this fuction is used for updating percentage...
def progress(stream=None,file_handle=None,remaining=None):
   #gets the percentage of the file that has been downloaded...
   file_downloaded=(file_size-remaining)
   per=(file_downloaded/file_size)*100
   dBtn.config(text="{:00.0f} % downloaded".format(per))

def startDownload():
    global file_size
    try:
        url=urlField.get()
        #changing button text
        dBtn.config(text='Please Wait...')
        dBtn.config(state=DISABLED)

        path_to_save_video=askdirectory()
        if path_to_save_video is None:
            return
#creating youtube object with url
        ob=YouTube(url,on_progress_callback=progress)
        #strms=ob.streams.all()
        #for s in strms:
        #    print(s)'''
        
        strm=ob.streams.first()
        file_size=strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        strm.download(path_to_save_video)
        print('done')
        dBtn.config(text='Start Download')
        
        
        dBtn.config(state=NORMAL)
        showinfo('Download Finished!','Downloaded Successfully')
        urlField.delete(0,END)
        vTitle.pack_forget()
        

    except Exception as e:
        print(e)
        print("error!")

def startDownloadThread():
    #create thread...
    thread=Thread(target=startDownload)
    thread.start()

#starting gui building
main=Tk()

#setting the title
main.title('My Youtube Downloader')

#set the icon
main.iconbitmap('youtube_icon.ico')
main.geometry("500x600")

#heading icon
file=PhotoImage(file='youtube.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP,pady=15)

#url text field
urlField=Entry(main,font=("ariel",20),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=20,pady=10)


#download button
dBtn=Button(main,text='Start Download',font=("ariel",20),justify=CENTER,relief='raised',command=startDownloadThread)
dBtn.pack(side=TOP,pady=15)


#video title
vTitle=Label(main,text='Video Title')
#vTitle.pack(side=TOP)

       
        #print(strm)
        #print(strm.filesize)
        #print(strm.title)
        #print(ob.description)

        #now downloading video
        



    
main.mainloop()