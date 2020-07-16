from pytube import *

url='https://www.youtube.com/watch?v=QiBeywmJoRY&list=RDQiBeywmJoRY&start_radio=1'
path_to_save_video='C:\\Users\\Abhya\\Desktop'
#creating youtube object with url
ob=YouTube(url)
strms=ob.streams.all()
for s in strms:
    print(s)
strm=ob.streams.first()
print(strm)
print(strm.filesize)
print(strm.title)
print(ob.description)

#now downloading video

strm.download(path_to_save_video)
print('done')