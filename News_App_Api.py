import requests
query=input("enter the interest: ")
api="66580b820ee0498fa69cec0c476e9a0f"
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-07-16&sortBy=publishedAt&apiKey={api}"
r=requests.get(url)
data=r.json()
articles=data["articles"]
for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n-----------------------------\n")