import json
from pprint import pprint

import requests

# link = 'http://minecraft2d.pythonanywhere.com/player/?player=Subvius'
#
link = 'http://127.0.0.1:5000/'


# res = requests.post(link + "player", params={"player": "Subvius", "add_task": True}, data=json.dumps({
#     "id": "2e0603a8-2f17-41e4-aeef-32f47d8af955",
#     "title": "Посетить Лиса",
#     "type": "exploring",
#     "questor": "Цебк",
#     "requirements": [
#         {
#             "title": "Поговорить с Лисом в его таверне.",
#             "type": "check_location",
#             "check_param": "location == 'Fox tavern'"
#         }
#     ],
#     "short_desc": "Цебк арендовал комнату в таверне Лиса. Осталось только найти её..",
#     "fraction": "нейтральная",
#     "deadline": -1
# }))

res = requests.get(link + "player", params={"player": "Subvius"})

pprint(res.json())
