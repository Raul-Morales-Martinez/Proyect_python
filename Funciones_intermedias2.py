#1
x = [ [5,2,3], [15,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

#2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for objeto in some_list:
        # print(objeto)# se accede a un objeto de la lista por cada iteración
        keyes = []
        for key in objeto:
            keyes.append(key)
            keyes.append("-")
            keyes.append(objeto[key])
            keyes.append(",")
            # print(key,"-", objeto[key]) #se accede a la clave del objeto
            # print(objeto[key]) #elemento a traves de la clave del objeto
        keyes.pop()
        print(*keyes)
    return some_list
iterateDictionary(students)
#3
def iterateDictionary2(key_name, some_list):
    for objeto in some_list:
        # print(objeto)# se accede a un objeto de la lista por cada iteración
            for key in objeto:
                if key_name == key:
                    print(objeto[key])
iterateDictionary2 ('first_name', students)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def prinInfo(some_dict):
    for key in some_dict:
        print()
        print(len(some_dict[key]),key)
        for x in range (len(some_dict[key])):
            print(some_dict[key][x])


prinInfo(dojo)
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# def iterateDictionary2 (sport_directory2):
#     for key in sport_directory2:
#         print(key)
#         print(sport_directory2[key])
#         for x in range(len(sport_directory2[key])):
#             print(sport_directory2[key][x])
#     return sport_directory2
# iterateDictionary2 (sports_directory)