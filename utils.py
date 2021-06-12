from random import randint
##generate a random identifier
def rand_identifier():
    rand_id  = []
    for i in range(12):
        rand_id.append(chr(randint(65,122)))

    return "".join(rand_id)