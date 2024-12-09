import os   # Library to use system commands
import sys  # Library to handle command-line arguments

# Tokens and the name of their corresponding repositories
tokens = ("your_token_1")	# PLACE YOUR TOKENS HERE
tokenNames = ("repo_1_name")	# PLACE THE NAME OF YOUR REPOS HERE
users = ("repo_1_user")		# PLACE THE USER OWNER OF YOUR REPOS HERE
# REMEMBER! For every repo, its token, name and username MUST be in the same position in the list

# Function to check that the selected repo is correct
def repoCheck():
    repo = int(input(f"Select a repository (1 - {len(tokens)})\n>> "))
    while(repo < 1 or repo > len(tokens)):
        repo = int(input("Please select a valid repo\n>> "))
    return repo

# Function to execute the corresponding git pull
def makePull(repo):
    token = tokens[repo - 1]  # Get the token for the selected repo
    username = users[repo - 1]  # Get the username for the selected repo
    repo_name = tokenNames[repo - 1]  # Get the repository name

    # Construct the remote URL with the token
    remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

    try:
        # Run git pull command
        os.system(f"git pull {remote_url}")  # Pull using the token-authenticated URL
        print("\033[92mPull complete!\033[0m")
    except Exception as e:
        print(f"\033[91mERROR: An error occurred during the git pull: {e}\033[0m")

# Function to execute the corresponding git push
def makePush(repo, com):
    token = tokens[repo - 1]  # Get the token for the selected repo
    username = users[repo - 1]  # Get the username for the selected repo
    repo_name = tokenNames[repo - 1]  # Get the repository name

    # Construct the remote URL with the token
    remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

    try:
        # Run git commands
        os.system("git add .")
        os.system(f'git commit -m "{com}"')  # Commit with the user-provided message
        os.system(f"git push {remote_url}")  # Push using the token-authenticated URL
        print("\033[92mPush complete!\033[0m")
    except Exception as e:
        print(f"\033[91mERROR: An error occurred during the git push: {e}\033[0m")

# Check if the program can be used
if(len(tokens) < 1 or len(tokenNames) != len(tokens) or len(users) != len(tokens)):
    print("\033[91mERROR: Check that the tokens, repos and users are correctly declared!\033[0m")
    exit(1) # Error code that indicates that tokens are not well-defined

# Ensure the correct usage of the script
if len(sys.argv) < 2 or sys.argv[1].lower() not in ["push", "pull"]:
    print("\033[91mERROR: Usage: python3 gitmanager.py <push/pull>\033[0m")
    exit(1)

operation = sys.argv[1].lower()

# Program interface
print("=============== [GITMANAGER.PY] ===============")
print("Available repositories:")
for i in range(len(tokens)):
    print(f"{i + 1}. {tokenNames[i]}")
    if(i + 1 >= len(tokens)):
        print("")

# Variable declaration
repo = repoCheck()

if operation == "pull":
    makePull(repo)
elif operation == "push":
    com = input("Enter a commit message\n>> ")
    makePush(repo, com)
