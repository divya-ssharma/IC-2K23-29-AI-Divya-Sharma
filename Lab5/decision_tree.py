from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'ssc': [67, 75, 65, 80, 70, 85, 60, 78, 82, 68],
    'hsc': [70, 80, 60, 85, 72, 88, 55, 76, 84, 65],
    'degree': [65, 78, 62, 82, 68, 85, 58, 74, 80, 66],
    'placed': [1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[['ssc', 'hsc', 'degree']]
y = df['placed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# DecisionTreeClassifier() -> overfit

model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(model.feature_importances_)

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=['ssc', 'hsc', 'degree'], class_names=['No', 'Yes'], filled=True)
plt.savefig('tree.png')
plt.close()
