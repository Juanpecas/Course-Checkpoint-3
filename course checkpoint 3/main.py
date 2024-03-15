#question 1

my_string = "Hello, world"
my_number = 42
my_list = [1, 2, 3, 4, 5]
my_boolean = True

#question 2
my_three_letters = my_string[:3]

#question 3
first_element = my_list[0]

#question 4
new_number = my_number + 10

#question 5
last_element = my_list[4]

#question 6
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')

#question 7
my_string = "Hello, world"
first_word = my_string[:5].upper()
new_string = first_word + my_string[5:]

#question 8
print(f"My number variable is {my_number}.")

#question 9
print("hello world")


#####

my_string = "Hello, how are you? Hello, world!"
hello_position = my_string.find("Hello")
hello_selected = my_string[hello_position:hello_position + len("Hello")]
string_replaced = my_string.replace("Hello", "goodbye")

    
print("Original String:", my_string)
print("Selected word:", hello_selected)
print("Replaced string:", string_replaced)