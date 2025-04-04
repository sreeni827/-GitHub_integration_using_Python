import requests

owner = "owner"
repo = "repo-name"
token = "your_personal_access_token"
workflow_id = "ci.yml"  # or the workflow numeric ID

url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}
data = {
    "ref": "main",  # branch name
    "inputs": {
        "env": "staging"
    }
}
response = requests.post(url, headers=headers, json=data)
print("Workflow triggered!" if response.status_code == 204 else response.text)
