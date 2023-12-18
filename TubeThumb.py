#Youtube Thumbnail Downloader

import os
from pytube import exceptions
from pytube import YouTube
from urllib.request import urlretrieve

downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Get Youtube Thumbnail
def Get_Thumbnail(link):
    yt = YouTube(link)
    print("Downloading...")
    thumbnail_url = yt.thumbnail_url
    filename_path = f"{downloads_folder}/{yt.title}.png"
    try:
        urlretrieve(thumbnail_url, filename_path)
    except Exception as e:
        print(f"Error: {e}")

#Program Welcome Prompt
print("Youtube Thumbnail Downloader")
print('To close program, hit option C or type "quit"')

while True:
    user_input = input('Enter Youtube Link: ')
    if user_input == 'quit':
        isRunning = False
        break
    else:
        try:
            Get_Thumbnail(user_input)
            print("Thumbnail Downloaded Successfully")
        except Exception as e:
            if isinstance(e, exceptions.RegexMatchError):
                print('Error: Link is not a valid Youtube link. Try Again.')
            else:
                print(f"An Error Occured: {type(e)}")            