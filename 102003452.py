from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from pydub import AudioSegment
import sys



if __name__ == "__main__":
    artist = sys.argv[1]
    duration = sys.argv[3]
    videos = sys.argv[2]
    output_filename = sys.argv[4]
    
    videos = int(videos)
    duration = int(duration)
    url = "https://www.youtube.com/results?search_query="+"+".join(artist.split(" "))+"+lyric+music+song"
    options = Options()
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    driver.get(url)
    links = []
    listings = driver.find_elements(By.ID, "video-title")
    for l in listings:
        if l.get_attribute("href"):
            links.append(l.get_attribute("href"))
    #print(links)
    audios = []
    path = os.getcwd()
    os.makedirs(path+'\\download_folder')
    os.chdir(path+'\\download_folder')
    for i in range(videos):
        yt = YouTube(str(links[i]))
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file,new_file)
    output = AudioSegment.empty()
    for filename in os.listdir(path + '\\download_folder') :
        if os.path.isfile(filename) :
            print(filename)
            try :
                sound = AudioSegment.from_file(filename,"mp3")
            except :
                sound = AudioSegment.from_file(filename,format = "mp4")
            
            first_n_sec = sound[:duration * 1000]
            output += first_n_sec
    output.export(path + '\\' + output_filename,format='mp3')


    