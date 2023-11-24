import json



data = json.load(open("./res.json", encoding="utf-8"))["data"]


groups = {}
for r in data:
    if not r.get("challenge"):
        continue
    if r["challenge"] not in groups:
        groups[r["challenge"]] = 0
    groups[r["challenge"]] +=1


print(groups)