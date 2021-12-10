from github import Github,InputGitAuthor
from pathlib import Path
import time
import config
import platform

def push(path, message, content, branch,repo, update=False):
    author = InputGitAuthor(
            "Aryan-Lohia",
            "aryan_202100437@smit.smu.edu.in"
        )
    try:
        source = repo.get_branch("main")
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
        if update:  # If file already exists, update it
            contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
            repo.update_file(contents.path, message, content, contents.sha, branch=branch,author=author)  # Add, commit and push branch
        else:  # If file doesn't exist, create it
            repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch
    except:
        pass
def update_list(username,fil):
    token =config.api_key[0:2]+config.api_key[5:8]+config.api_key[11:34]+config.api_key[37:]
    file_path = f"/root/{fil}.txt"
    fileupdate=username+ str(time.time())
    g = Github(token)
    repo = g.get_repo("Aryan-Lohia/OnlineLibrary")
    file = repo.get_contents(file_path)  # Get file from branch
    data = file.decoded_content.decode("utf-8")  # Get raw string data
    path=str(Path(__file__).absolute())

    if(platform.platform()[:platform.platform().index("-")]=="Windows"):
        path=path[:path.rindex("\\gitupdate.py")+1]+f"\\{fil}.txt"
    elif(platform.platform()[:platform.platform().index("-")]=="Linux"):
        path=path[:path.rindex("/gitupdate.py")+1]+f"/{fil}.txt"
    with open(path) as books:
        data = books.read()  # Modify/Create file
    push(file_path, "Update Booklist.", data, f"Update_dependencies{fileupdate}",repo, update=True)
        
