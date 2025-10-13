import random
import string

def random_user_id():
    chars = string.ascii_lowercase + string.digits
    user_id = "".join(random.choice(chars) for _ in range(6))
    return user_id

print(random_user_id())