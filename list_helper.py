class ListHelper:
    def greatest_frequency(my_list: list):
        return max(set(my_list), key=my_list.count)

    def doubles(my_list: list):
        element_count = []
        for element in my_list:
            if my_list.count(element) > 1:
                element_count.append(element)
        return len(set(element_count))



if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))