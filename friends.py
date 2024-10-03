# Ask the user for a list of 3 friends

# Fo each friend, we'll tell the user whether they are nearby.
#  for each nearby friend, we'll save their name to 'nearby_friend.txt'


print('-----------------Nearby Friends---------------')

find_friend_input = input("Enter names of the friends: ")

print(find_friend_input)

with open('allfriends.txt', 'r') as file:
    contents = file.readlines()
    formatted_contents = [name.strip() for name in contents]

print(formatted_contents)