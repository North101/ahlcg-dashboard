import requests

from ahlcg_dashboard.data import (Faction, Investigator, InvestigatorData,
                                     Stats)

r = requests.get('https://arkhamdb.com/api/public/cards/')
data = list[Investigator]()
for item in r.json():
  if item['type_code'] != 'investigator':
    continue

  name = item['name']
  if item['pack_code'] in ('rod', 'aon', 'bad', 'btb', 'rtr'):
    name = f'(P) {name}'
  investigator = Investigator(
      name,
      Faction[item['faction_name']],
      stats=Stats(
          item['skill_willpower'],
          item['skill_intellect'],
          item['skill_combat'],
          item['skill_agility'],
          item['health'],
          item['sanity'],
      ),
  )
  if investigator not in data:
    data.append(investigator)

InvestigatorData(data).write()
