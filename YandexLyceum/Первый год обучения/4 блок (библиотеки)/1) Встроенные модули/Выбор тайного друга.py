import sys
from random import sample


def secret_friend(l_friends):
    while True:
        diff = True
        secret_friends = sample(l_friends, k=len(l_friends))
        for j in range(len(secret_friends)):
            if secret_friends[j] == l_friends[j]:
                diff = False
                break
        if diff:
            return secret_friends


friends = (list(map(str.strip, sys.stdin)))
list_secret = secret_friend(friends)
for i in range(len(friends)):
    print(f"{friends[i]} - {list_secret[i]}")
