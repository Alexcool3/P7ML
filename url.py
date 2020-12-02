# This file contains all URLs needed for this project.

from enum import Enum

#  URLs:
#  "https://p7server.000webhostapp.com/download_files.php"
#  "https://p7server.000webhostapp.com/Participants/"
#  "https://p7server.000webhostapp.com/Test/"
#  "https://p7server.000webhostapp.com/Alternative/"


class URL(Enum):
    SEND = ""  # Must send to PHP file on the Server.
    PARTICIPANTS = "https://p7server.000webhostapp.com/Participants/"
    TEST = "https://p7server.000webhostapp.com/Test"
    ALTERNATIVE = "https://p7server.000webhostapp.com/Alternative/"



