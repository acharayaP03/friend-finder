# Ask the user for a list of 3 friends

# Fo each friend, we'll tell the user whether they are nearby.
#  for each nearby friend, we'll save their name to 'nearby_friend.txt'

import re

print('-----------------Nearby Friends---------------')
print()


def get_user_input():
    user_input = input('Enter your friends name (can be comma separated or space separated): ')

    return re.split(r'[,\s]+', user_input)

def read_names_from_file(filename):
    with open(filename, 'r') as filename:
        return [line.strip() for line in filename]

# with open('nearby_friends.txt', 'r') as file:
#     contents = file.readlines()
#     formatted_contents = [name.strip() for name in contents]
#
# print(formatted_contents)



def main():
    file_name = 'nearby_friends.txt'
    friends = read_names_from_file(file_name)

    print(f"Friends list from file: {friends}")

    while True:
        print('Welcome to Nearby Friends finder...')
        friends = get_user_input()
        print(friends)

        user_choice = input("Do you want to keep continue search?. (yes/no)").lower()

        if not user_choice.startswith('y'):
            break

    print("Thank you for using Nearby Friends Finder!")

if __name__ == '__main__':
    main()