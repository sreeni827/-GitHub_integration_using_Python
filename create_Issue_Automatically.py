from github import Github

g = Github("your_personal_access_token")
repo = g.get_repo("owner/repo-name")

issue = repo.create_issue(
    title="Auto-generated Issue",
    body="This issue was created using Python script for DevOps automation."
)
print(f"Issue created: {issue.html_url}")
