import pandas as pd
import numpy as np
df=pd.read_excel('marks.xlsx')
x=df[['Hours']]
y=df['Scores']
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x,y)
hours=5.1
X_test=np.array(hours)
X_test=X_test.reshape(1,-1)
predictions = lm.predict(X_test)
print(predictions)

