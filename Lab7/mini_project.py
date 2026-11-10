from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = {
    'hours': [2, 4, 6, 8, 1, 3, 5, 7, 9, 2.5, 5.5, 7.5],
    'sleep': [6, 7, 8, 6, 5, 7, 8, 6, 7, 6, 7, 8],
    'pass': [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[['hours', 'sleep']]
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

print(accuracy_score(y_test, model.predict(X_test)))
print(model.feature_importances_)
