import random
def get_random_code():
    num = random.randint(1000, 9999)
    return "Your random code is: {}".format(num)