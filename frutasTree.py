from sklearn import tree

feature_names = ['peso','cor','textura']
target_names = ['maca', 'laranja', 'pera']
features = [[120,1,0], [110,1,0], [125,1,0], [150,0,1], [170,0,1], [145,0,1], [80,2,0], [70,2,0], [90,2,0]]
labels = ['maca','maca','maca','laranja','laranja','laranja','pera','pera','pera']


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print clf.predict([[95,2,0]])



#Visualizacao por pdf
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
out_file=dot_data,
feature_names=feature_names,
class_names=target_names,
filled=True, rounded=True,
impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("frutas.pdf")
