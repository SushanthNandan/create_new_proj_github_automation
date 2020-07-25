import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")


def create():
    folderName = str(sys.argv[1])
    os.makedirs(os.getenv("HOME") + "/MyProjects/" + folderName)
    user = Github(token)
    user.get_user().create_repo(folderName)
    print("Successfully created repository {}".format(folderName))


if __name__ == "__main__":
    create()
