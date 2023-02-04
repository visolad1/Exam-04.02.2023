days = int(input('Enter days: '))
weeks = 0
years = 0

if days >= 365:
    years = days // 365
    days %= 365 

if days >= 7:
    weeks = days // 7
    days %= 7 

print('Years:', years)
print('Weeks:', weeks)
print('Days:', days)