# 预测模型
# 根据城市、学历、工作经验预测薪资

import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# 从文件加载数据
file_path = 'jobData.csv'
df = pd.read_csv(file_path)

# 选择需要的特征和目标值
# 我们假设 minSalary 和 maxSalary 的平均值作为目标薪资
X = df[['city', 'education', 'workExperience']]
df['avgSalary'] = (df['minSalary'] + df['maxSalary']) / 2
y = df['avgSalary']

#对分类变量进行编码
label_encodes = {}
for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    label_encodes[column] = le

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建简单的神经网络模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# 定义预测函数
def pred_salary(city, workExp, education):
    input_data = pd.DataFrame([[city, workExp, education]],
                              columns=['city', 'workExperience', 'education'])
    for column in input_data.columns:
        input_data[column] = label_encodes[column].transform(input_data[column])

    prediction= model.predict(input_data)
    return prediction[0][0]

# 示例预测
predicted_salary = pred_salary('北京', '经验5-10年', '本科')
print(f'预测结果: {predicted_salary:.2f}')



