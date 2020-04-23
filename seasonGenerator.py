import math
import pandas as pd
import numpy as np 
import random
import csv

class Team:
	def __init__(self,name,conference,wins,losses,rating):
		self.name = name
		self.conference = conference
		self.wins = wins
		self.losses = losses
		self.rating = rating

df = pd.read_csv('records2.csv')
df2 = pd.read_csv('all-time-records.csv')

fprimeprime = open('fullSeasonTweets.csv','w+')
fprimeprime.close()

#defenders = Team('DC Defenders','East',0,0,1750)
defenders = Team(df['name'][0],df['conference'][0],df['wins'][0],df['losses'][0],df['rating'][0])
battlehawks = Team(df['name'][1],df['conference'][1],df['wins'][1],df['losses'][1],df['rating'][1])
guardians = Team(df['name'][2],df['conference'][2],df['wins'][2],df['losses'][2],df['rating'][2])
vipers = Team(df['name'][3],df['conference'][3],df['wins'][3],df['losses'][3],df['rating'][3])
renegades = Team(df['name'][4],df['conference'][4],df['wins'][4],df['losses'][4],df['rating'][4])
roughnecks = Team(df['name'][5],df['conference'][5],df['wins'][5],df['losses'][5],df['rating'][5])
wildcats = Team(df['name'][6],df['conference'][6],df['wins'][6],df['losses'][6],df['rating'][6])
dragons = Team(df['name'][7],df['conference'][7],df['wins'][7],df['losses'][7],df['rating'][7])

defenders2 = Team(df2['name'][0],df2['conference'][0],df2['wins'][0],df2['losses'][0],df2['rating'][0])
battlehawks2 = Team(df2['name'][1],df2['conference'][1],df2['wins'][1],df2['losses'][1],df2['rating'][1])
guardians2 = Team(df2['name'][2],df2['conference'][2],df2['wins'][2],df2['losses'][2],df2['rating'][2])
vipers2 = Team(df2['name'][3],df2['conference'][3],df2['wins'][3],df2['losses'][3],df2['rating'][3])
renegades2 = Team(df2['name'][4],df2['conference'][4],df2['wins'][4],df2['losses'][4],df2['rating'][4])
roughnecks2 = Team(df2['name'][5],df2['conference'][5],df2['wins'][5],df2['losses'][5],df2['rating'][5])
wildcats2 = Team(df2['name'][6],df2['conference'][6],df2['wins'][6],df2['losses'][6],df2['rating'][6])
dragons2 = Team(df2['name'][7],df2['conference'][7],df2['wins'][7],df2['losses'][7],df2['rating'][7])

eastConference = [defenders,battlehawks,guardians,vipers]
westConference = [renegades,roughnecks,wildcats,dragons]

#print(eastConference[0].name) #testing objects
#print(westConference[0].name)

individualWeekGames = []

fullTeamLineup = [defenders,battlehawks,guardians,vipers,renegades,roughnecks,wildcats,dragons]

#thisWeek = shuffleOnCommand(fullTeamLineup)

def updateRating(ra, k, sa): #Modified ELO Rating Update post-game
	raPrime = ra + (k*(sa))
	return math.floor(raPrime)

#print(updateRating(1,1,1)) #testing updateRating

def calculateEA(ra,rb): #calculate ea rating
	eA = 1/(1+math.pow(10,((rb-ra)/400)))
	return eA

def calculateEB(ra,rb): #calculate eb rating
	eB = 1/(1+math.pow(10,((ra-rb)/400)))
	return eB

def shuffleOnCommand(list): #python shuffle
	random.shuffle(list)
	return list

def calculateEScoresAcrossWeek(week):
	eaGame0 = calculateEA(week[0].rating,week[1].rating)
	eaGame0Team = week[0].name
	eaGame1 = calculateEA(week[2].rating,week[3].rating)
	eaGame1Team = week[2].name
	eaGame2 = calculateEA(week[4].rating,week[5].rating)
	eaGame2Team = week[4].name
	eaGame3 = calculateEA(week[6].rating,week[7].rating)
	eaGame3Team = week[6].name

	#ebGame0 = calculateEB(week[0].rating,week[1].rating)
	ebGame0 = calculateEB(week[0].rating,week[1].rating)
	ebGame0Team = week[1].name
	ebGame1 = calculateEB(week[2].rating,week[3].rating)
	ebGame1Team = week[3].name
	ebGame2 = calculateEB(week[4].rating,week[5].rating)
	ebGame2Team = week[5].name
	ebGame3 = calculateEB(week[6].rating,week[7].rating)
	ebGame3Team = week[7].name

	eArray = [eaGame0,eaGame0Team,ebGame0,ebGame0Team,eaGame1,eaGame1Team,ebGame1,ebGame1Team,eaGame2,eaGame2Team,ebGame2,ebGame2Team,eaGame3,eaGame3Team,ebGame3,ebGame3Team]
	return eArray

def gameRandomizer(team0,team1,ea,eb):
	score0 = math.floor(random.randint(3,101))
	score1 = math.floor(random.randint(3,101))
	if score0 == score1:
		score0 = score0 + 3
	scoresArray = [team0,score0,team1,score1]
	return scoresArray

def theWeeksScores(week):
	game0 = gameRandomizer(week[0].name, week[1].name, calculateEScoresAcrossWeek(week)[0], calculateEScoresAcrossWeek(week)[2])
	game1 = gameRandomizer(week[2].name, week[3].name, calculateEScoresAcrossWeek(week)[4], calculateEScoresAcrossWeek(week)[6])
	game2 = gameRandomizer(week[4].name, week[5].name, calculateEScoresAcrossWeek(week)[8], calculateEScoresAcrossWeek(week)[10])
	game3 = gameRandomizer(week[6].name, week[7].name, calculateEScoresAcrossWeek(week)[12], calculateEScoresAcrossWeek(week)[14])

	fullWeeksScoresArray = [game0,game1,game2,game3]
	return fullWeeksScoresArray

def winnersAndLosers(aIndex,bIndex,week):
	if theWeeksScores(week)[1] > theWeeksScores(week)[3]:
		week[aIndex].wins = week[aIndex].wins + 1
		week[bIndex].losses = week[bIndex].losses + 1
	else:
		week[aIndex].losses = week[aIndex].losses + 1
		week[bIndex].wins = week[bIndex].wins + 1

def sCalc(matchIndex,eaIndex,ebIndex,week):
	if ((theWeeksScores(week)[matchIndex][1] > theWeeksScores(week)[matchIndex][3]) and (calculateEScoresAcrossWeek(week)[eaIndex] > calculateEScoresAcrossWeek(week)[ebIndex])):
		sValueA = -0.5
		sValueB = 0.5
	elif ((theWeeksScores(week)[matchIndex][1] < theWeeksScores(week)[matchIndex][3]) and (calculateEScoresAcrossWeek(week)[eaIndex] > calculateEScoresAcrossWeek(week)[ebIndex])):
		sValueA = -0.5
		sValueB = 1
	elif ((theWeeksScores(week)[matchIndex][1] > theWeeksScores(week)[matchIndex][3]) and (calculateEScoresAcrossWeek(week)[eaIndex] < calculateEScoresAcrossWeek(week)[ebIndex])):
		sValueA = 1
		sValueB = -0.5
	else:
		sValueA = 0.5
		sValueB = -0.5
	sValuesArray = [sValueA,sValueB]
	return sValuesArray

def fullWeekRatingUpdate(week,kvalue,game0,game1,game2,game3):
	week[0].rating = updateRating(week[0].rating,kvalue,game0[0])
	week[1].rating = updateRating(week[1].rating,kvalue,game0[1])

	week[2].rating = updateRating(week[2].rating,kvalue,game1[0])
	week[3].rating = updateRating(week[3].rating,kvalue,game1[1])

	week[4].rating = updateRating(week[4].rating,kvalue,game2[0])
	week[5].rating = updateRating(week[5].rating,kvalue,game2[1])

	week[6].rating = updateRating(week[6].rating,kvalue,game3[0])
	week[7].rating = updateRating(week[7].rating,kvalue,game3[1])

def updateWinsRecord(team_name_fixed,index_name,range1):
	for i in range (0,range1):
		if team_name_fixed.name == index_name[i].name:
			team_name_fixed.wins = index_name[i].wins
		else:
			i = i + 1

def updateLossesRecord(team_name_fixed,index_name,range1):
	for i in range (0,range1):
		if team_name_fixed.name == index_name[i].name:
			team_name_fixed.losses = index_name[i].losses
		else:
			i = i + 1

def updateRatingsRecord(team_name_fixed,index_name,range1):
	for i in range (0,range1):
		if team_name_fixed.name == index_name[i].name:
			team_name_fixed.rating = index_name[i].rating
		else:
			i = i + 1

#print(fullTeamLineup)
for g in range (0,10):

	thisWeek = shuffleOnCommand(fullTeamLineup)
#demoEscores = calculateEScoresAcrossWeek(thisWeek)
#print(demoEscores)
#print(thisWeek[0].name)
#print(thisWeek[1].name)
#print(calculateEScoresAcrossWeek(thisWeek)[0])
	winnersAndLosers(0,1,thisWeek)
	winnersAndLosers(2,3,thisWeek)
	winnersAndLosers(4,5,thisWeek)
	winnersAndLosers(6,7,thisWeek)

	game0s = sCalc(0,0,2,thisWeek)
	game1s = sCalc(1,4,6,thisWeek)
	game2s = sCalc(2,8,10,thisWeek)
	game3s = sCalc(3,12,14,thisWeek)

	fullWeekRatingUpdate(thisWeek,4,game0s,game1s,game2s,game3s)
#print(thisWeek[0].name)
#print(thisWeek)

#print(thisWeek[0].name)
#print(thisWeek[0].wins)
#print(thisWeek[0].losses)
#print(thisWeek[0].rating)

#print(theWeeksScores(thisWeek))
	#print(thisWeek[0].wins)
	d = theWeeksScores(thisWeek)
	#df2 = pd.DataFrame(data = d)

	#for i in range (0, 8):
		#d2 = [thisWeek[i].name,thisWeek[i].wins,thisWeek[i].losses,thisWeek[i].rating]
		#with open(r'test.csv','a') as f:
			#writer = csv.writer(f)
			#writer.writerow(d2)


	#with open(r'weeklyscores.csv','w') as f:
	#	writer = csv.writer(f)
	#	writer.writerow(d)

	game0team0 = d[0][0]
	game0score0 = d[0][1]
	game0team1 = d[0][2]
	game0score1 = d[0][3]
	game1team0 = d[1][0]
	game1score0 = d[1][1]
	game1team1 = d[1][2]
	game1score1 = d[1][3]
	game2team0 = d[2][0]
	game2score0 = d[2][1]
	game2team1 = d[2][2]
	game2score1 = d[2][3]
	game3team0 = d[3][0]
	game3score0 = d[3][1]
	game3team1 = d[3][2]
	game3score1 = d[3][3]

	game0Tweet = ["Week " + str(g+1) + ": "+ str(game0team0) + " " + str(game0score0) + "-" + str(game0team1) + " " +str(game0score1)]
	game1Tweet = ["Week " + str(g+1) + ": "+ str(game1team0) + " " + str(game1score0) + "-" + str(game1team1) + " " +str(game1score1)]
	game2Tweet = ["Week " + str(g+1) + ": "+ str(game2team0) + " " + str(game2score0) + "-" + str(game2team1) + " " +str(game2score1)]
	game3Tweet = ["Week " + str(g+1) + ": "+ str(game3team0) + " " + str(game3score0) + "-" + str(game3team1) + " " +str(game3score1)]



	fprime = open('fullSeasonTweets.csv','a',newline='')

	with fprime:
		writer = csv.writer(fprime)
		writer.writerow(game0Tweet)
		writer.writerow(game1Tweet)
		writer.writerow(game2Tweet)
		writer.writerow(game3Tweet)

	#print(theWeeksScores(thisWeek)[0][1])
	#print(theWeeksScores(thisWeek)[0][3])
	#print(calculateEScoresAcrossWeek(thisWeek)[0])
	#print(calculateEScoresAcrossWeek(thisWeek)[2])


	g = g + 1

def batchUpdater(team):
	updateWinsRecord(team,thisWeek,8)
	updateLossesRecord(team,thisWeek,8)
	updateRatingsRecord(team,thisWeek,8)

batchUpdater(defenders)
batchUpdater(battlehawks)
batchUpdater(guardians)
batchUpdater(vipers)
batchUpdater(renegades)
batchUpdater(roughnecks)
batchUpdater(wildcats)
batchUpdater(dragons)

batchUpdater(defenders2)
batchUpdater(battlehawks2)
batchUpdater(guardians2)
batchUpdater(vipers2)
batchUpdater(renegades2)
batchUpdater(roughnecks2)
batchUpdater(wildcats2)
batchUpdater(dragons2)


#print(guardians.wins)
#print(vipers.wins)
#print(guardians.losses)
#print(vipers.losses)
#print(guardians.rating)
#print(vipers.rating)
#for i in range (0, 8):
	#d2 = [thisWeek[i].name,thisWeek[i].wins,thisWeek[i].losses,thisWeek[i].rating]
	#with open(r'test.csv','a') as f:
	#	writer = csv.writer(f)
	#	writer.writerow(d2)

def dataFrameRating(i,team):
	#df.iat[i,3] = team.wins
	#df.iat[i,4] = team.losses
	df.iat[i,5] = team.rating

dataFrameRating(0,defenders)
dataFrameRating(1,battlehawks)
dataFrameRating(2,guardians)
dataFrameRating(3,vipers)
dataFrameRating(4,renegades)
dataFrameRating(5,roughnecks)
dataFrameRating(6,wildcats)
dataFrameRating(7,dragons)

#need total record function/df sheet


def dataFrameTotalRecord(i,team):
	previousWins = df2.iloc[i,3]
	previousLosses = df2.iloc[i,4]
	previousRating = df2.iloc[i,5]
	df2.iat[i,3] = (team.wins + previousWins)
	df2.iat[i,4] = (team.losses + previousLosses)
	df2.iat[i,5] = team.rating

dataFrameTotalRecord(0,defenders)
dataFrameTotalRecord(1,battlehawks)
dataFrameTotalRecord(2,guardians)
dataFrameTotalRecord(3,vipers)
dataFrameTotalRecord(4,renegades)
dataFrameTotalRecord(5,roughnecks)
dataFrameTotalRecord(6,wildcats)
dataFrameTotalRecord(7,dragons)


df.to_csv('records2.csv', index = False)

df2.to_csv('all-time-records.csv',index = False)



#df2.to_csv('all-time-records.csv', index = False)
#d = [defenders.name,defenders.conference,defenders.wins,defenders.losses,defenders.rating]
#df = pd.DataFrame(data = d)
#df.to_csv('records.csv')
thisSeasonsWins = []
for i in range(0,8):
	thisSeasonsWins.append({'name': thisWeek[i].name, 'conference': thisWeek[i].conference, 'wins': thisWeek[i].wins, 'rating': thisWeek[i].rating})
	#thisSeasonsWins.append(thisWeek[i].wins)
	i = i + 1

def winReturner(e):
	return e['wins']
def conferenceReturner(e):
	return e['conference']
def ratingRetruner(e):
	return e['rating']


#thisSeasonsWins.sort(key=winReturner, reverse=True)
thisSeasonsWins.sort(key=conferenceReturner, reverse =True)
#print(thisSeasonsWins[0])
#print(thisSeasonsWins[1])
#print(thisSeasonsWins[4])
#print(thisSeasonsWins[5])

thisSeasonsWinsEast = [thisSeasonsWins[4],thisSeasonsWins[5],thisSeasonsWins[6],thisSeasonsWins[7]]
thisSeasonsWinsEast.sort(key=winReturner, reverse = True)
print(thisSeasonsWinsEast[0])
print(thisSeasonsWinsEast[1])
print(thisSeasonsWinsEast[2])
print(thisSeasonsWinsEast[3])

thisSeasonsWinsWest = [thisSeasonsWins[0],thisSeasonsWins[1],thisSeasonsWins[2],thisSeasonsWins[3]]
thisSeasonsWinsWest.sort(key=winReturner, reverse = True)
print(thisSeasonsWinsWest[0])
print(thisSeasonsWinsWest[1])
print(thisSeasonsWinsWest[2])
print(thisSeasonsWinsWest[3])
def playoffMatchSim(team0,team1,rating0,rating1):
	score0 = math.floor(random.randint(3,75)*(1000/rating0))
	score1 = math.floor(random.randint(3,75)*(1000/rating1))
	if score0 == score1:
		score0 = score0 + 1
		return [team0,score0,team1,score1]
	elif score0 > score1:
		return [team0,score0,team1,score1]
	else:
		return [team1,score1,team0,score0]

westPlayoff = playoffMatchSim(thisSeasonsWinsWest[0],thisSeasonsWinsWest[1],thisSeasonsWinsWest[0]['rating'],thisSeasonsWinsWest[1]['rating'])
eastPlayoff = playoffMatchSim(thisSeasonsWinsEast[0],thisSeasonsWinsEast[1],thisSeasonsWinsEast[0]['rating'],thisSeasonsWinsEast[1]['rating'])
#print("The " + westPlayoff[0]['name'] + " win the west playoff")
#print("The " + eastPlayoff[0]['name'] + " win the east playoff")

seasonFinal = playoffMatchSim(westPlayoff[0],eastPlayoff[0],westPlayoff[0]['rating'],eastPlayoff[0]['rating'])

#print("The " + seasonFinal[0]['name'] + " win the finals! The score was " + seasonFinal[0]['name'] + ": " + str(seasonFinal[1]) + ", " + seasonFinal[2]['name'] + ": " + str(seasonFinal[3]))

westPlayoffTweet = ["The " + str(westPlayoff[0]['name']) + " win the western conference finals! " + str(westPlayoff[0]['name']) + ": " + str(westPlayoff[1]) + ", " + str(westPlayoff[2]['name']) + ": " + str(westPlayoff[3])]
eastPlayoffTweet = ["The " + str(eastPlayoff[0]['name']) + " win the eastern conference finals! " + str(eastPlayoff[0]['name']) + ": " + str(eastPlayoff[1]) + ", " + str(eastPlayoff[2]['name']) + ": " + str(eastPlayoff[3])]

seasonFinalTweet = ["The " + str(seasonFinal[0]['name']) + " win the XFL championship! " + str(seasonFinal[0]['name']) + ": " + str(seasonFinal[1]) + ", " + str(seasonFinal[2]['name']) + ": " + str(seasonFinal[3])]


f = open('fullSeasonTweets.csv','a',newline='')

with f:
	writer = csv.writer(f)
	writer.writerow(westPlayoffTweet)
	writer.writerow(eastPlayoffTweet)
	writer.writerow(seasonFinalTweet)





