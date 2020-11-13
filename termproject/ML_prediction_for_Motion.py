import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

cur_path = os.getcwd()
data_dir = os.path.join(cur_path, 'references/iot_telemetry_data.csv')

iot_data = pd.read_csv(data_dir)

print(iot_data.info())

iot_data['time_stamp'] = pd.to_datetime(iot_data['ts'], unit='s')
iot_data.drop(columns=['ts'], inplace=True) 
print(iot_data.head())

sns.heatmap(iot_data.corr()) 
plt.show()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder #데이터 셋 전처리를 위한 모듈
labelencoder=LabelEncoder()
Devices = labelencoder.fit_transform(iot_data['device'])
Light = labelencoder.fit_transform(iot_data['light'])
Motion = labelencoder.fit_transform(iot_data['motion'])

onehotencoder=OneHotEncoder()

iot_data['device'] = Devices
iot_data['light'] = Light
iot_data['motion'] = Motion

iot_data_df = pd.DataFrame(iot_data)

iot_data_df['temp'] = (iot_data_df['temp'] * 1.8) + 32

iot_data_df.drop('time_stamp', axis=1, inplace=True)


# 데이터셋을 train과 test로 분리

x = iot_data_df.drop('motion', axis= 1)
y = iot_data_df['motion'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=0)

from sklearn.linear_model import LogisticRegression #선형회귀모델
reg = LogisticRegression()
reg.fit(X_train, y_train)

prediction = reg.predict(X_test)

print(prediction)

from sklearn import metrics
from sklearn.metrics import confusion_matrix
cnf_matrix = metrics.confusion_matrix(y_test, prediction)
#cnf_matrix
sns.heatmap(cnf_matrix, annot=True, cmap="Spectral" ,fmt='g', linewidth = 3)
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

print("Accuracy:",metrics.accuracy_score(y_test, prediction))
print("Precision:",metrics.precision_score(y_test, prediction))
print("Recall:",metrics.recall_score(y_test, prediction))