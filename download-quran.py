# Description: Download all the mp3 files of the Quran from the website https://www.tvquran.com

# Install the required packages (IMPORTANT Before running)
#python3 -m pip install requests
#python3 -m pip install beautifulsoup4
#python3 -m pip install tqdm

#How to use:
#1- Open the terminal
#2- Go to the directory where the file is located
#3- Run the following command: python3 download-quran.py
#4- Wait for the download to complete



import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
def download_mp3(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)

def fetch_tvquran_mp3s(url):
    if not os.path.exists('Quran-Mohamed-Toure'):
        os.makedirs('Quran-Mohamed-Toure')
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the <a> tags with the 'download' attribute
    download_links = soup.find_all('a', attrs={'download': True})
    # Extract the file name and URL of each download link
    for link in tqdm(download_links):
        file_name = link.parent.find('div', {'class': 'share-box'}).get('data-title')
        url = f"https:{link.get('href')}"
        with open('Quran-Mohamed-Toure/' + file_name + '.mp3', 'wb') as f:
            f.write(requests.get(url).content)

if __name__ == '__main__':
    url = "https://www.tvquran.com/ar/scholar/355/profile/محمد-الهادي-توري#google_vignette"
    fetch_tvquran_mp3s(url)


