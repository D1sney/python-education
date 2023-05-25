people=float(input('How many people? '))
hotdogs=float(input('How many hot dogs for everyone? '))

if people*hotdogs/10 == people*hotdogs//10:
    sauseges=people*hotdogs//10
else:
    sauseges=(people*hotdogs//10)+1

if people*hotdogs/8 == people*hotdogs//8:
    bread=people*hotdogs//8
else:
    bread=(people*hotdogs//8)+1

if people*hotdogs/10 == people*hotdogs//10:
    x = people*hotdogs%10
else:
    x = 10-(people*hotdogs%10)

if people*hotdogs/8 == people*hotdogs//8:
    y = people*hotdogs%8
else:
    y = 8-(people*hotdogs%8)


if people>=0 and hotdogs>=0:
    print(f'You need {sauseges:^5,.0f}package of sausages')
    print(f'You need {bread:^5,.0f}package of bread')
    print(f'{x:>7,.0f}sauseges left')
    print(f'{y:>7,.0f}breds left')
else:
    print('fuck minus')