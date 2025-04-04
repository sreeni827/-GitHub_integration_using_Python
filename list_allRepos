from github import Github

g = Github("your_personal_access_token")
user = g.get_user()

print("Your Repositories:")
for repo in user.get_repos():
    print(repo.full_name)
