from defining_methods import NumberStats

user_choice = 0
number_stats = NumberStats()
while user_choice != -1:
    user_choice = int(input("Enter your choice: "))
    if user_choice != -1:
        number_stats.add_number(user_choice)
all_numbers = number_stats.all_numbers
even_numbers = [x for x in all_numbers if x % 2 == 0]
odd_numbers = [x for x in all_numbers if x % 2 != 0]
print(f"Sum of all numbers is {number_stats.get_sum()}")
print(f"Mean of all numbers is {number_stats.average()}")
print(f"Sum of even numbers: {sum(even_numbers)}")
print(f"Sum of odd numbers: {sum(odd_numbers)}")