# generate a random identifier to add to the db email field
from secrets import SystemRandom

sysrandom = SystemRandom()

def rand_identifier():
    rand_id = []
    for i in range(12):
        rand_id.append(chr(sysrandom.randint(65, 122)))

    return "".join(rand_id)
