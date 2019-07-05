import sys

def greet_users(usernames):
    usernames_up = usernames[0].upper()
    print("Hello,", usernames_up+usernames[1:]+'!')

args = sys.argv[1:]
for name in args:
    greet_users(name)
