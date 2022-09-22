from pytube import YouTube

link = input("Link : ")
yt = YouTube("https://www.youtube.com/watch?v=s8FgiPAcJ8Q&list=LL&index=9")

print("Title : ", yt.title)
print("Views : ", yt.views)

yd = yt.streams.get_highest_resolution()

# Add Folder Here
yd.download('./YTfolder')
