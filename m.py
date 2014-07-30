from sphinxit.core.processor import Search

from sphinxit.core.helpers import BaseSearchConfig

class SphinxitConfig(BaseSearchConfig):
    WITH_STATUS = False


search_query = Search(indexes=['cigar'], config=SphinxitConfig)
search_query = search_query.match("cohiba")

# search_query.

rs = search_query.ask()

print(rs)

s = ''

for i in rs['result']['items']:
    print(i['id'], ",")
    s += str(i['id']) + ","

print(s)

