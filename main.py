import csv
from collections import Counter

import pandas

# df = pandas.read_csv(os.path.join(pathlib.Path(__file__).parent.absolute(), "files", "gsoc2009.csv")).to_dict()
# print(df["Organizations"])
df = {}

for year in reversed(range(2009, 2021)):
    filename = "files//gsoc" + str(year) + ".csv"
    r = csv.DictReader(open(filename))
    dic = []
    for raw in r:
        dic.append(raw)
    df[year] = dic

combined = {'Organizations': [], 'About': [], 'Technology': [], 'Category': [], 'Topics': []}

for year in df:
    for item in df[year]:
        # print(item)
        for key in combined:
            try:
                combined[key].append(item[key])
            except:
                combined[key].append(None)
        # combined['Organizations'].append(item['Organizations'])

org = Counter()
for organization in combined['Organizations']:
    org[organization] += 1

org = dict(org)

final = []

for organization in sorted(org.keys()):
    for i, j, k, l, m in zip(combined['Organizations'], combined["About"], combined['Technology'], combined['Category'],
                             combined['Topics']):
        if organization == i:
            final.append({"Organizations": organization, "About": j, "Technology": k, "Category": l, "Topics": m,
                          "Count": org[organization]})
            break

print(pandas.DataFrame(final).to_csv("out.csv"))
