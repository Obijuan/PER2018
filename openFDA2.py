import http.client
import json

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?search=acetylsalicylate&limit=20")
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read().decode("utf-8")
conn.close()

# -- Read the data as a json object
data = json.loads(data1)
meta = data['meta']
disclaimer = meta['disclaimer']
terms = meta['terms']
license2 = meta['license']
meta_results = meta['results']
limit = meta_results['limit']
total = meta_results['total']
results = data['results']


print("\n")
print("* SHOWN: {}/{}".format(limit, total))
print("-------------")

manufacturers = []
for n, drug in enumerate(results):
    if drug['openfda']:
        manufacturer_name = drug['openfda']['manufacturer_name'][0]
        try:
            manufacturers.index(manufacturer_name)
        except ValueError:
            manufacturers.append(manufacturer_name)
            print("* [{}]: {}".format(len(manufacturers), manufacturer_name))
