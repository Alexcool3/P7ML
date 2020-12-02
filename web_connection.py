import urllib
import url
from bs4 import BeautifulSoup
import pandas


# Function that returns all files URL in a folder.
def get_all_files_url(url=url.URL.TEST.value):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    files = []
    for link in soup.findAll('a'):
        if str(link).find('.csv') != -1:
            filename = link.get('href')
            files.append(str(f'{url}/{filename}'))
    return files


# This function returns data as pandas data frame from URL.
def read_csv_files_from_url(url):
    df = []
    for file in get_all_files_url(url):
        df.append(pandas.read_csv(file))
    return df


tmp = read_csv_files_from_url(url.URL.TEST.value)

