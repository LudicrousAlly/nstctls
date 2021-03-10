from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

X, y = datasets.load_iris(return_X_y=True)
iris = datasets.load_iris()
x = iris.target_names


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100, test_size=0.3)

dtc = DecisionTreeClassifier()
dtc = dtc.fit(X_train, y_train)

print("Точность деревьев равна: ", dtc.score(X_test, y_test))

derevo = []

pred = dtc.predict([[3.2, 2.5, 2, 0]])
derevo.append(x[int(pred[0])])

pred = dtc.predict([[1.2, 4.5, 2, 1]])
derevo.append(x[int(pred[0])])

pred = dtc.predict([[1.2, 3.2, 4, 6]])
derevo.append(x[int(pred[0])])

pred = dtc.predict([[4.2, 1.2, 4, 6]])
derevo.append(x[int(pred[0])])

pred = dtc.predict([[3.2, 1.2, 1, 2]])
derevo.append(x[int(pred[0])])

knb = KNeighborsClassifier()
knb = knb.fit(X_train, y_train)

print("Точность соседей равна: ", knb.score(X_test, y_test))

sosedi = []

pred = knb.predict([[3.2, 2.5, 2, 0]])
sosedi.append(x[int(pred[0])])

pred = knb.predict([[1.2, 4.5, 2, 1]])
sosedi.append(x[int(pred[0])])

pred = knb.predict([[1.2, 3.2, 4, 6]])
sosedi.append(x[int(pred[0])])

pred = knb.predict([[4.2, 1.2, 4, 6]])
sosedi.append(x[int(pred[0])])

pred = knb.predict([[3.2, 1.2, 1, 2]])
sosedi.append(x[int(pred[0])])

drevo = ''

for i in range(len(derevo)):
    drevo += derevo[i] + "  "

sosed = ''

for i in range(len(sosedi)):
    sosed += sosedi[i] + "  "

print("Распознавания деревьев: ", drevo)
print("Распознавания соседей: ", sosed)

import pydot

(graph,) = pydot.graph_from_dot_file('C:\\Users\\ilyat\\Desktop\\University\\Python\\Laba7\\tree.dot')
graph.write_png('tree.png')