import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('ice.csv')
# double rectangle!
# x is inputs
x = data[['temp', 'street']]
y = data['ice']

# 82 decision tree.
# This is magic number (by take fuji.) Why? He don't know.
# 最適な決定木の数がある
clf = RandomForestClassifier(n_estimators=82, min_samples_split=2)
# ML process is just here.
clf.fit(x, y)
print(clf.score(x, y))
print(clf.feature_importances_)
p = clf.predict(x)
t = np.arange(0.0, 31.0)
plt.plot(t, data['ice'], '--b')
plt.plot(t, p, '-b')
plt.legend(('real', 'randomF'))
plt.show()
