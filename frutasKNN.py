#Classificando laranjas, macas e peras
from sklearn import neighbors
#Features: peso(g), laranja,vermelho,verde, textura(0=liso, 1=enrugado)
features =  [[120,0,1,0,0], [110,0,1,0,0], [125,0,1,0,0], #macas
             [150,1,0,0,1], [170,1,0,0,1], [145,1,0,0,1], #laranjas
             [80,0,0,1,0], [70,0,0,1,0], [90,0,0,1,0]]    #peras
labels = ['maca','maca','maca','laranja','laranja','laranja','pera','pera','pera']
clf = neighbors.KNeighborsClassifier(3)#numero de vizinhos
clf = clf.fit(features,labels)
print clf.predict([[90,0,0,1,0]])
