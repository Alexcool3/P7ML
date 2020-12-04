import urllib
from bs4 import BeautifulSoup
import pandas as pd
import requests
import url


# Function that returns all files URL in a folder.
def get_all_files_url(url):
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
        df.append(pd.read_csv(file, delimiter=";"))
    return df


# When using pandas .to_csv function give index=False as an argument
# to avoid the index column from being exported.


def get_table(table):
    r = requests.post(url.URL.TABLE.value, data={"table": table})
    data = []
    #Append each row from table to the data list.
    for row in r.text.splitlines():
        data.append(row.split(';'))
        # Parse numeric values to float or integer.
        for value in range(len(data[-1])):
            if is_number(data[-1][value]):
                data[-1][value] = float(data[-1][value]) if data[-1][value].find('.') != -1 else int(data[-1][value])
    # Returns data list as pandas DataFrame.
    return table_to_data_frame(data)


def table_to_data_frame(table):
    return pd.DataFrame(table, columns=['ID', 'Sex', 'Age', 'Time', 'Completion'])


def is_number(input_string):
    return any(char.isdigit() for char in input_string)
