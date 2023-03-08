#!/usr/bin/python3
for i in range(97, 123):
    if alpha(i) == 'q' or alpha(i) == 'e':
        continue
    print(alpha(i).format(i), end='')
