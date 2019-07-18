# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
        data = yaml.load(f)

# Find data type of the file
type_of_data = type(data)
print('Test data file type - ', type_of_data)

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print('City - ' + city)

venue = data['info']['venue']
print('Venue - ' + venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
Teams = data['info']['teams']
print('Teams - ' + Teams[0], 'ánd' + ' ' + Teams[1])

print('Toal number of teams - ' + str(len(Teams)))

# Which team won the toss and what was the decision of toss winner ?
toss_won_by = data['info']['toss']['winner']
print('Toss won by - ' + toss_won_by)

decision_taken = data['info']['toss']['decision']
print('Decision of toss winning team - ' + decision_taken)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print('First innings first ball bowler - ' + first_bowler)

first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print('First innings first ball batsman -' + first_batsman)

# How many deliveries were delivered in first inning ?
deliveries_1 = len(data['innings'][0]['1st innings']['deliveries'])
print('Number of deliveries played in 1st innings - ' + str(deliveries_1))

# How many deliveries were delivered in second inning ?
deliveries_2 = len(data['innings'][1]['2nd innings']['deliveries'])
print('Number of deliveries played in 2nd innings - ' + str(deliveries_2))

# Which team won and how ?
winner = data['info']['outcome']['winner']
by = data['info']['outcome']['by']['runs']

print(winner + 'won the match by' + str(by))



