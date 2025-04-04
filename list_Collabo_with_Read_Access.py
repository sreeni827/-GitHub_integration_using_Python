from github import Github

g = Github("your_personal_access_token")
repo = g.get_repo("owner/repo-name")

print("Users with read access:")
for collab in repo.get_collaborators():
    if repo.get_collaborator_permission(collab) == "read":
        print(collab.login)
