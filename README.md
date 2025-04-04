# -GitHub_integration_using_Python
# 🔗 GitHub Integration with Python (DevOps Use Cases)

This project demonstrates how to use **Python** and the **GitHub REST API** (via the `PyGithub` library and `requests`) to automate common DevOps workflows such as listing repositories, managing issues, triggering workflows, and more.

---

## 📦 Features & Use Cases

| Use Case | Description |
|----------|-------------|
| 🔍 List Repositories | Fetch all public/private repositories for the authenticated user. |
| 👥 List Collaborators with Read Access | Identify users with pull (read) permissions on a given repository. |
| 🛠️ Create GitHub Issues | Automatically open issues for tracking or monitoring tasks. |
| 🚀 Trigger GitHub Actions Workflows | Dispatch GitHub Actions workflows from a Python script. |
| 🧹 Delete a Repository | Remove a GitHub repository (requires admin access). |
| 📜 List Open Pull Requests | View all open PRs for a specific repository. |

---

## ⚙️ Setup

### 1. Install Dependencies

```bash
pip install PyGithub requests
