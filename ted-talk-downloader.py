##Generalised script to use it as a CLI 
#TO EXECUTE IT AS A CLI USE
# python ted-talk-downloader.py www.url.com/download/me
import requests #getting content from url
from bs4 import BeautifulSoup #web scrapper
import re #regex 
import sys #for system control

#Exception Handling

if len(sys.argv)>1:
    url=sys.argv[1]
else:
    sys.exit("Error:Please enter the correct URL")

r= requests.get(url)
print("Download about to start.....")

soup= BeautifulSoup(r.content,features="lxml")

for val in soup.findAll("script"):
    if(re.search("__NEXT_DATA__",str(val))) is not None:
        result=str(val)
        # print(str(val))
   

# print(soup.prettify())

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

print(result_mp4)

mp4_url=result_mp4.split('"')[0]  #ACtually has no effects 

print(mp4_url)



print("Downloading video from ......" +mp4_url)

# file_name= mp4_url.split("/")[len(mp4_url.split("/").split('?')[0])]
file_name="video.mp4"

print("Storing video in......"+file_name)

r=requests.get(mp4_url)
with open(file_name,'wb') as f:
    f.write(r.content)

print("Download process finished......")