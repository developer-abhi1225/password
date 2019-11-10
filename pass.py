from password_strength import PasswordStats
from password_strength import PasswordPolicy
import datetime

hdfcpolicy = PasswordPolicy.from_names(
    length=6,  # min length: 8
    uppercase=5,  # need min. 2 uppercase letters
    numbers=5,  # need min. 2 digits
    special=5,  # need min. 2 special characters
    nonletters=5,  # need min. 2 non-letter characters (digits, specials, anything)
)




import string
from random import *


print(str(datetime.datetime.now()))
while True:
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(20, 20)))
    print("Pass ==> " + password + " strength==> " + str(PasswordStats(password).strength()))
    if not (len(hdfcpolicy.test(password))):
        if PasswordStats(password).strength() >= 0.75:
            print("Chosen Pass ==> "+password+" strength==> "+str(PasswordStats(password).strength()))
            break