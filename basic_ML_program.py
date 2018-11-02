import sklearn import tree
features = [[140, 'smooth'],[130, 'smooth'],[150, 'bumpy'], [170, 'bumpy']]
labels = [0, 0, 1, 1]
## 0 for apple
## 1 for orange

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150,0]])
