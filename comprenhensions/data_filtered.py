DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'EduMining',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'EduMining',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'EduMining',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'EduMining',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():

  all_python_devs = [x["name"] for x in DATA if x["language"] == "python" ]
  all_edumining_workers = [x["name"] for x in DATA if x["organization"] == "EduMining" ]
  adults = list(filter(lambda x : x["age"] > 17 , DATA))
  adults = list(map(lambda x : x["name"] , adults))
  old_people = [dict(i, **{"old" : i["age"] > 70 })  for i in DATA ]

  print(all_edumining_workers)
  print(all_python_devs)
  print(adults)
  print(old_people)

if __name__ == '__main__': 
  main()