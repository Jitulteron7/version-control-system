import sys
import os
from pathlib import Path
from git_tools.commands import CatFileCommand, HashObjectCommand
from git_tools.client import GitClient

gitClient = GitClient()

def createGitDir():
    os.mkdir(".vcs")
    os.mkdir(".vcs/objects")
    os.mkdir(".vcs/refs")
    with open(".vcs/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")
    print("Initialized vcs directory")

def runCatFileCommand():
    flag = sys.argv[3]
    commitSHA = sys.argv[4]
    
    command = CatFileCommand(flag, commitSHA)
    gitClient.run(command)

def runHashObjectCommand():
    flag = sys.argv[3]
    filePath = sys.argv[4]
    
    if not filePath:
        filePath = flag
        flag = None
    command = HashObjectCommand(flag, filePath)
    gitClient.run(command)
     
     
def main():
    command = sys.argv[1]
    if command == "init":
        createGitDir()
    elif command == "cat-file":
        runCatFileCommand() 
    elif command == "hash-object":
        runHashObjectCommand() 
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()

