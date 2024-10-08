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

def find_all_matching_friends(friends, friends_name):
    matches = []
    for friend in friends_name:
        for search in friends:
            if search.lower() in friend.lower():
                matches.append(friend)
                break
    return matches

def main():
    print('Welcome to Nearby Friends finder...')
    file_name = 'nearby_friends.txt'
    friends_name = read_names_from_file(file_name)

    print(f"Friends list from file: {friends_name}")

    while True:
        friends = get_user_input()
        matches = find_all_matching_friends(friends, friends_name)

        # if matches is not empty
        if matches:
            print("Near by friends are found... checkout the list")
            for index, friend in enumerate(matches):
                print(f"{index + 1}). {friend}")
        else:
            print("No nearby friends found matching the entered names.")


        user_choice = input("Do you want to keep continue search?. (yes/no)").lower()
        if not user_choice.startswith('y'):
            break

    print("Thank you for using Nearby Friends Finder!")

if __name__ == '__main__':
    main()