from itsdangerous import json


import json
# import pprint

l = ['apple','orange','banana', 'peach', 'mango']
l.insert(0,l[:])
# #print(l)

# pp = pprint.PrettyPrinter(indent=4,width=40,compact=True)
# pp.pprint(l)

#json

d = {'a':'A','b':'B','c':{'x':{'y':'Y'}}}

# [
#     [
#         "apple",
#         "orange",
#         "banana",
#         "peach",
#         "mango"
#     ],
#     "apple",
#     "orange",
#     "banana",
#     "peach",
#     "mango"
# ]
print(json.dumps(l,indent=4))

# {
#     "a": "A",
#     "b": "B",
#     "c": {
#         "x": {
#             "y": "Y"
#         }
#     }
# }
print(json.dumps(d,indent=4))
