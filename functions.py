def sum(a, b):
    return a + b

def list_sort(my_list):
    my_list.sort()
    return len(my_list),my_list

print(list_sort([4,2,7,1,0]))

def all_even():
    n = 0
    while True:
        yield n
        n+=2

my_gen = all_even()

for i in range(5):
    print(next(my_gen))

do_something = 4
do_something += 3

for i in range(100):
    print(next(my_gen))