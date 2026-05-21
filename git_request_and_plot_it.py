import requests
import json
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
print(response_dict.keys())

with open("github.json", "w", encoding="utf-8") as file:
    json.dump(response_dict, file, indent=4)

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

import requests
import json
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

repo_names = []
repo_stars = []
repo_links = []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    repo_stars.append(repo_dict['stargazers_count'])
    repo_links.append(repo_dict["html_url"])

# Визуализация
fig = px.bar(
    x=repo_names,
    y=repo_stars,
    title="Top Python Repositories by Stars",
    labels={"x": "Repository", "y": "Stars"}
)

fig.update_traces(
    customdata=repo_links,
    hovertemplate="<b>%{x}</b><br>⭐ Stars: %{y}<br>🔗 URL: %{customdata}<extra></extra>"
)

fig.show()

print("Selected information about each repository: ")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
