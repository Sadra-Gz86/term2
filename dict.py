# eng_to_per = {
#     'hello': 'salam',
#     'bye': 'khodahafez'
# }
# phones = {
#     'baba': '09112354789',
#     'reza': '09142565478',
# }
grades = {
    'ali': 19,
    'reza': 20,
    'ahmad': 18,
    'jasem': 19,
    'ghasem': 20,
    'nosrat': 18
}
name = input('enter name')
grades.update({name: 19})
grades[name] = 19
# a = input("Nomreye kio mikhay?")
# print(grades.get(a, 'tooye dictionary nist.'))
# for name in grades.values():
#     print(f"nomreye {name} shod.")