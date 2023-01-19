import requests

r = requests.get("https://example.com")

print(str(r.content)[:20])