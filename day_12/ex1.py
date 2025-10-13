import random
import string

def random_user_id():
    chars = string.ascii_lowercase + string.digits
    user_id = "".join(random.choice(chars) for _ in range(6))
    return user_id

print(random_user_id())


def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))

    characters = string.ascii_lowercase + string.digits  # a-z + 0-9

    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        print(user_id)

# Example usage
user_id_gen_by_user()

