def do_something(strs):
    print('Hey there! I am ' + strs)
do_something('Darshil')

def display_options():
    print('OPTIONS:\n')
    print('1. Add a Student\n')
    print('2. Update Student Details\n')
    print('3. Delete a Student\n')
    print('4. View All Students\n')
    print('5. Calculate Average Marks of a Student\n')
    print('6. Save Students to File\n')
    print('7. Load Students from File\n')
    print('8. Exit\n')

def main():
    display_options();
    input = input('Select a option')
    if input.isdigit():
        decide_method(int(input))

def decide_method(option):
    if not isinstance(option, int):
        raise TypeError('option must be an integer.\n')
    match(option):
        case 1:
            print('You selected the option of adding a student.\n')
        case 2:
            print('You selected the option of updating student details.\n')
        case 3:
            print('You selected the option of deleting a student.\n')
        case 4:
            print('You selected the option of viewing all students.\n')
        case 5:
            print('You selected the option of calculating average marks of a student.\n')
        case 6:
            print('You selected the option of saving students to a file.\n')
        case 7:
            print('You selected the option of loading students from a file.\n')
        case 8:
            print('Exiting...\n')


    