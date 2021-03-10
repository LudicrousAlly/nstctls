import pandas as pd
import numpy as np
from math import sqrt


def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)


def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1
    n = len(si)
    if n == 0: return 0
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    if den == 0: return 0

    r = num/den
    return r


def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
    for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue

        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim
                simSums.setdefault(item, 0)
                simSums[item] += sim

    rankings=[(total/simSums[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    ra = []
    for i in range(len(rankings)):
        if rankings[i][0] >= 4.5:
            ra.append(rankings[i])

    return ra


def transformPrefs(prefs):
 result={}
 for person in prefs:
    for item in prefs[person]:
        result.setdefault(item,{})
        result[item][person]=prefs[person][item]
 return result

#Читаем БД с айди фильмов и их названиями
movnames = pd.read_csv("C:\\Users\\ilyat\\Desktop\\University\\recsystm\\aeiorhgbmaimvfdjkb\\ml-latest-small\\movies.csv")

id = movnames.to_numpy(dtype = str)[:, 0]   #Массив id фильмов
names = movnames.to_numpy(dtype = str)[:, 1]    #Массив имён фильмов

for i in range(len(names)):     #Убираем год выхода фильма из названия(для упрощения поиска рекомендаций по названию)
    names[i] = names[i][:-7]

names = names.tolist()  #Меняем массив names с ndarray на обычный list

namesid = dict()    #Создаем словарь, в котором будет храниться инфа о фильмах в виде {id:name, id:name,...}

namesid[id[0]] = str(names[0])


for i in range(1, len(id)):
    namesid[id[i]] = str(names[i])

#Читаем БД с айди юзеров, айди фильмов и оценкой фильма
data = pd.read_csv("C:\\Users\\ilyat\\Desktop\\University\\recsystm\\aeiorhgbmaimvfdjkb\\ml-latest-small\\ratings.csv")

users = data.to_numpy(dtype=int)[:,0]   #Айди юзеров запихиваем в users
movie = data.to_numpy(dtype=str)[:, 1]  #Айди фильмов запихиваем в movie
rating = data.to_numpy()[:, 2]          #Оценку запихиваем в rating
users, movies_for_user = np.unique(users, return_counts=True)   #Из списка юзеров убираем повторения, и создаём список movies_for_users, в
users = users.astype(str)              #котором будет храниться кол-во повторений юзеров в БД, т.е. инфа о том, сколько фильмов юзер оценил
movie = movie.tolist()


ratings = dict([( users[0], dict([( movie[0], 0 )]) )]) #Создаем вложенный словарь, в котором изначально храним инфу {user1:{movie1:0}}
for i in range(len(users)):
    ratings[users[i]] = dict([( movie[0], 0 )]) #Добавляем в словарь всех юзеров, с нулевой оценкой к первому фильму(потом обновиться при необходимости)

tmp = 0

for i in range(len(users)):
    for j in range(movies_for_user[i]):
        ratings[users[i]].update(dict([(movie[tmp], rating[tmp])])) #Заполняем словарь
        tmp += 1

#Определение схожести пользователей, на примере юзеров 3 и 15
print("Схожесть юзера 3 и юзера 15: ", sim_pearson(ratings, '3', '15'), "\n------------------------------------------")

rec_user = input("Введите id юзера, для которого вы хотите найти людей со схожими интересами,"
                 " и которому хотите порекомендовать фильмы для просмотра: ")

if rec_user in users:
    print("Юзеры, со схожими интересами, как у номера '{0}': {1}".format(rec_user, topMatches(ratings, rec_user, n = 7))) #Поиск n похожих юзеров
    print("Рекомендации по фильмам для юзера '{0}': {1}".format(rec_user, getRecommendations(ratings, rec_user))) #Поиск рекомендуемых фильмов
else:
    print("Юзера с таким айди нет!!")

movrec=transformPrefs(ratings)  #Создаем новый словарь из старого, приводя его к виду {movie:{user:rating, user:rating,..},..}

rec_movie = input("----------------------------------------\n"
                  "Введите название фильма, для которого хотите найти похожие,"
                 " и который хотите порекомендовать людям: ")
if rec_movie in names:
    print("\nФильмы, похожие на '{0}': {1}".format(rec_movie, topMatches(movrec, id[names.index(rec_movie)]))) #Поиск схожих фильмов
    print("Люди, которым может понравиться фильм '{0}': {1}".format(rec_movie, getRecommendations(movrec, id[names.index(rec_movie)]))) #Поиск юзеров, которым может понравиться фильм
else:
    print("Такого фильма нет(")
