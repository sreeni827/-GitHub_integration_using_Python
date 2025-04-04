#!/usr/bin/env python3

import sys
import requests
from getpass import getpass

# GitHub API URL
API_URL = "https://api.github.com"

# Get GitHub username and token (you can prompt securely)
username = input("Enter your GitHub username: ")
token = getpass("Enter your GitHub personal access token: ")

# Get repo owner and name from command-line args
if len(sys.argv) < 3:
    print("Usage: python script.py <repo_owner> <repo_name>")
    sys.exit(1)

repo_owner = sys.argv[1]
repo_name = sys.argv[2]

# Function to make a GET request to GitHub API
def github_api_get(endpoint):
    url = f"{API_URL}/{endpoint}"
    response = requests.get(url, auth=(username, token))
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        sys.exit(1)
    return response.json()

# Function to list users with read access
def list_users_with_read_access():
    endpoint = f"repos/{repo_owner}/{repo_name}/collaborators"
    collaborators = github_api_get(endpoint)

    users_with_read = [
        user['login'] for user in collaborators
        if user.get('permissions', {}).get('pull', False)
    ]

    if not users_with_read:
        print(f"No users with read access found for {repo_owner}/{repo_name}.")
    else:
        print(f"Users with read access to {repo_owner}/{repo_name}:")
        for user in users_with_read:
            print(user)

# Main
print(f"Listing users with read access to {repo_owner}/{repo_name}...")
list_users_with_read_access()
