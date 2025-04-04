from github import Github

g = Github("your_personal_access_token")
repo = g.get_repo("owner/repo-name")

#WARNING: This is destructive
repo.delete()
print("Repository deleted successfully.")
