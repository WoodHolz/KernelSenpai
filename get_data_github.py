import requests
import json

# GitHub API 导出 Linux 项目的所有 commit、PR 和 issue
def export_github_linux_data():
    repo_owner = "torvalds"  # Linux 项目的所有者（Linus Torvalds）
    repo_name = "linux"  # Linux 项目的名称

    # 获取所有 commit
    commits_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    commits_response = requests.get(commits_url)
    commits_data = json.loads(commits_response.text)
    commits = [commit["commit"]["message"] for commit in commits_data]

    # 获取所有 PR
    prs_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    prs_response = requests.get(prs_url)
    prs_data = json.loads(prs_response.text)
    prs = [pr["title"] for pr in prs_data]

    # 获取所有 issue
    issues_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    issues_response = requests.get(issues_url)
    issues_data = json.loads(issues_response.text)
    issues = [issue["title"] for issue in issues_data]

    return commits, prs, issues

# 从 kernel.org 网站导出所有内核版本的 changelog
def export_kernel_org_changelog():
    kernel_org_url = "https://www.kernel.org/"
    kernel_versions_url = f"{kernel_org_url}releases.json"

    # 获取所有内核版本信息
    versions_response = requests.get(kernel_versions_url)
    versions_data = json.loads(versions_response.text)

    changelogs = []
    for version in versions_data["releases"]:
        version_number = version["version"]
        changelog_url = f"{kernel_org_url}pub/linux/kernel/v{version_number}/ChangeLog-{version_number}"
        changelog_response = requests.get(changelog_url)
        changelog_data = changelog_response.text
        changelogs.append(changelog_data)

    return changelogs

# 执行导出操作，并返回处理后的数据
github_commits, github_prs, github_issues = export_github_linux_data()
kernel_changelogs = export_kernel_org_changelog()

# 将数据保存为文本文件
with open("github_data.txt", "w", encoding="utf-8") as file:
    for commit in github_commits:
        file.write(f"COMMIT: {commit}\n")
    for pr in github_prs:
        file.write(f"PR: {pr}\n")
    for issue in github_issues:
        file.write(f"ISSUE: {issue}\n")

with open("kernel_changelogs.txt", "w", encoding="utf-8") as file:
    for changelog in kernel_changelogs:
        file.write(f"CHANGELOG:\n{changelog}\n")