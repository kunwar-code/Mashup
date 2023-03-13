from pytube import YouTube
import os
from youtubesearchpython import VideosSearch

def searchVids(name, nov):
    videosSearch = VideosSearch(str(name), limit = nov)
    res=[]
    for i in range(nov):
        res.append(videosSearch.result()['result'][i]['link'])
    return res

def downloadVids(nov, res):
    namesList=[]
    for i in range(nov):
        yt = YouTube(str(res[i]))
        video = yt.streams.filter(only_audio=True).first()
        destination =''
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        namesList.append(new_file)
        # print()
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")
    # for i in range(nov):
    #     print(namesList[i])
    return namesList


