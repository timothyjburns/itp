def get_power(x, n):
    return x ** n

def print_graph(n):
    for i in range(-8, 9):
        get_power(i, n)
        print("*" * get_power(i, n))
    print('')

n = int(input("Enter an integer number: "))
print_graph(n)