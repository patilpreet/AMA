from sklearn.model_selection import train_test_split
import pandas as pd

data = {'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df[['X']], df['Y'], test_size=0.3)

print("Train Set:")
print(pd.concat([X_train, y_train], axis=1))

print("\nTest Set:")
print(pd.concat([X_test, y_test], axis=1))