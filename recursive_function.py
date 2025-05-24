def fill_list(numbers: list):
    """ If the length of the list is less than 10, add items to the list """
    if len(numbers) < 10:
        numbers.append(0)
        # call the function again
        fill_list(numbers)

if __name__ == "__main__":
    test_list = [1, 2, 3 ,4]
    fill_list(test_list)
    print(test_list)
