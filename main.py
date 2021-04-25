import csv
from collections import Counter

import pandas

df = {}

for year in reversed(range(2009, 2021)):
    filename = "files//gsoc" + str(year) + ".csv"
    r = csv.DictReader(open(filename))
    dic = []
    for raw in r:
        dic.append(raw)
    df[year] = dic

combined = {'Organizations': [], 'About': [], 'Technology': [], 'Category': [], 'Topics': [], 'year': []}

for year in df:
    print(year)
    for item in df[year]:
        for key in combined:
            if (key != 'year'):
                try:
                    combined[key].append(item[key])
                except:
                    combined[key].append(None)
        combined['year'].append(year)


def remove(string):
    return "".join(string.split())


org = Counter()
for organization in combined['Organizations']:
    org[remove(organization).lower()] += 1

org = dict(org)

final = []

for organization in sorted(org.keys()):
    for i, j, k, l, m, n in zip(combined['Organizations'], combined["About"], combined['Technology'],
                                combined['Category'],
                                combined['Topics'], combined['year']):
        if organization == remove(i).lower():
            final.append({
                "Organizations": i,
                "About": j,
                "Technology": k,
                "Category": l,
                "Topics": m,
                "Count": org[organization],
                "Last Appeared": n
            })
            break

pandas.DataFrame(final).to_csv("out.csv")

pandas.DataFrame(final).to_json("client//src//data//out.json", orient='records')
