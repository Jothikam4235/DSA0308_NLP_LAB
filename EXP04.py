def plural_fsm(noun):
    state = 0
    if noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        state = 1
    elif noun.endswith('y') and len(noun) > 1 and noun[-2] not in 'aeiou':
        state = 2
    else:
        state = 3
    if state == 1:
        plural = noun + "es"
    elif state == 2:
        plural = noun[:-1] + "ies"
    else:
        plural = noun + "s"
    return plural
nouns = ["cat", "bus", "box", "baby", "city", "dog", "church"]
print("Jothika M 192324235")
print("Singular Noun\tPlural Noun")
print("--------------------------------")
for noun in nouns:
    print(noun, "\t\t", plural_fsm(noun))
