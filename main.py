i = 0
item_dict = {}
while True:

    try:
        item = input()
        item = item.upper()

        if item in item_dict:

            number_in_dictionary = item_dict[item]
            item_dict[item] = number_in_dictionary + 1




        else:

            item_dict[item] = 1




    except EOFError:
        length = item_dict.__len__()
        for key, value in item_dict.items():
            print(value, key)

        break
