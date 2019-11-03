import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

divorce = pd.read_csv("divorce.csv", encoding="shift-jis", sep=";")

divorce_target = divorce["Class"]
divorce_data = divorce.drop(["Class"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    divorce_data,
    divorce_target,
    test_size=0.2,
    random_state=54,
    shuffle=True
)

clf = RandomForestClassifier(n_estimators=382, max_depth=None, min_samples_split=2, random_state=8)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
