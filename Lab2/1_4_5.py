def own_insert(my_list, index, value):
    my_list[index:index] = [value]
    return my_list

if __name__ == "__main__":
    my_list = [1, 5, 2, 9, 4, 2]
    index = 2
    value = 100
    print(own_insert(my_list, index, value))