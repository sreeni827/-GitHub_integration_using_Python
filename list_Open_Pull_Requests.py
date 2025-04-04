from github import Github

g = Github("your_personal_access_token")
repo = g.get_repo("owner/repo-name")

pulls = repo.get_pulls(state="open", sort="created")
print("Open Pull Requests:")
for pr in pulls:
    print(f"#{pr.number} - {pr.title}")
