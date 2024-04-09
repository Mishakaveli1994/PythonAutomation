from flatdict import FlatDict

# example_json = {
#     "title": "Squad Heroes",
#     "squads": [
#         {"name": "Team Rocket",
#          "members": [
#              {
#                  "name": "Molecule Man",
#                  "age": 29,
#                  "secretIdentity": "Dan Jukes",
#                  "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
#              },
#              {
#                  "name": "Madame Uppercut",
#                  "age": 39,
#                  "secretIdentity": "Jane Wilson",
#                  "powers": [
#                      "Million tonne punch",
#                      "Damage resistance",
#                      "Superhuman reflexes"
#                  ]
#              },
#          ]},
#         {"name": "Team Sausage",
#          "members": [
#              {
#                  "name": "Eternal Flame",
#                  "age": 1000000,
#                  "secretIdentity": "Unknown",
#                  "powers": [
#                      "Immortality",
#                      "Heat Immunity",
#                      "Inferno",
#                      "Teleportation",
#                      "Interdimensional travel"
#                  ]
#              },
#              {
#                  "name": "Super Dimo 3000",
#                  "age": 29,
#                  "secretIdentity": "Unknown",
#                  "powers": [
#                      "Immortality",
#                      "Heat Immunity",
#                      "Inferno",
#                      "Teleportation",
#                      "Mega Programmer"
#                  ]
#              },
#              {
#                  "name": "Goshu",
#                  "age": 29,
#                  "secretIdentity": "Unknown",
#                  "powers": [
#                      "Immortality",
#                      "Heat Immunity",
#                      "Inferno",
#                      "Teleportation",
#                      "Mega Programmer"
#                  ]
#              }
#          ]}
#     ]
# }

# Standard for loop
# for squad in example_json["squads"]:
#     squad_name = squad["name"]
#     for member in squad["members"]:
#         if member['age'] == 29:
#             print(f"{squad_name}: {member['name']}")

# List comprehension - UUUGLYYY
# [print(f"{squad['name']}: {member['name']}") for squad in example_json["squads"] for member in squad['members'] if member['age'] == 29]

# FlatDict

example_flat_json = {
    "Squad Heroes":
        {"Team Rocket": {
            "Molecule Man": {"age": 29,
                             "secretIdentity": "Dan Jukes",
                             "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}
        },
        "Team Team": {
            "Eternal Flame": {"age": 29,
                             "secretIdentity": "Dan Jukes",
                             "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]}
        }},


}

flat_dict = FlatDict(example_flat_json, delimiter=".")
print(flat_dict)
print(flat_dict['Squad Heroes.Team Rocket.Molecule Man.age'])