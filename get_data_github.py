import requests

def get_github_data(owner, repo, data_type):
    base_url = f'https://api.github.com/repos/{owner}/{repo}/{data_type}'
    response = requests.get(base_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {data_type}. Status code: {response.status_code}")
        return None

def main():
    owner = 'torvalds'  # Linux项目的所有者
    repo = 'linux'      # Linux项目的仓库名称

    commits = get_github_data(owner, repo, 'commits')
    prs = get_github_data(owner, repo, 'pulls')
    issues = get_github_data(owner, repo, 'issues')

    if commits:
        print(f"Commits count: {len(commits)}")
        # 在这里处理commits数据，根据需要提取信息

    if prs:
        print(f"Pull Requests count: {len(prs)}")
        # 在这里处理PR数据，根据需要提取信息

    if issues:
        print(f"Issues count: {len(issues)}")
        # 在这里处理issues数据，根据需要提取信息

if __name__ == "__main__":
    main()
