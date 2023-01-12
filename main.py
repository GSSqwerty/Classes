from Class import Posi_list, Student


def main():
    a = Posi_list()
    values = [ 10, -8, 88, 100, -8, -100, 1000, [] ]
    for elem in values:
        a.append(elem)
    print(a)
    group = Student('Vasiliy', 'Utkin', 7)
    print(group.first_name, group.last_name, group.score)
    group.score = 10
    print(group.first_name, group.last_name, group.score)
main()