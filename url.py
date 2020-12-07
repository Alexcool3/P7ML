# This file contains all URLs needed for this project.
from enum import Enum
#  URLs:
#  "https://p7server.000webhostapp.com/download_table.php"
#  "https://p7server.000webhostapp.com/Participants/"
#  "https://p7server.000webhostapp.com/Test/"
#  "https://p7server.000webhostapp.com/Alternative/"


# This enum contains URL's for folders or files on the server.
class URL(Enum):
    """
    This enum contains the URL for folders or files on the server.
    """
    PARTICIPANTS = "https://p7server.000webhostapp.com/Participants/"
    TEST = "https://p7server.000webhostapp.com/Test"
    ALTERNATIVE = "https://p7server.000webhostapp.com/Alternative/"
    TABLE = "https://p7server.000webhostapp.com/download_table.php"


# This enum refers to the tables in the mysql database.
class TABLE(Enum):
    """
    This enum contains all the tables in the mysql database.
    """
    TEST = "test"
    PARTICIPANTS = "participants"
