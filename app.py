import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st


#web page code
st.title("HEALTH INSURANCE PREDICTION")
img_url = "https://akm-img-a-in.tosshub.com/businesstoday/images/story/202408/66b1cf12a9284-many-people-focus-mainly-on-the-inclusions-and-premiums-of-the-policy-but-forget-to-pay-attention-to-062153553-16x9.jpeg?size=948:533"
st.image(img_url)

# LOAD DATA and ML MODEL PART
#step:2
url = "https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)

#step:3
df.drop("Customer_ID", axis=1, inplace = True)

df['Previous_Insurance'] = df['Previous_Insurance'].map({'No':0,"Yes":1})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'No':0,"Yes":1})

#step:4
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]

#step:5
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

#step:6
model = LogisticRegression()
model.fit(X_train,Y_train)

#show data sample
st.write(df.head())
#create side bar for user input form
st.sidebar.title("Fill Customer Details")
st.sidebar.image(img_url)

for index,col_name in enumerate(X.columns):
  min_v = X[col_name].min()
  max_v = X[col_name].max()
  if col_name != "Previous_Insurance":
    value = st.sidebar.slider(f"select value for {col_name}",
                              min_value = min_v,
                              max_value = max_v)
  else:
    value = st.sidebar.number_input(f"select value for{col_name}: ")

  all_ans.append(value)
  
ud = {j:all_ans[i] for i,j in enumerate(X.colunms)}
user_df = pd.DateFrame(ud,index = [1])
st.write(user_df)

#================================Prediction=========================

if st.button("Click to Predict: " ):
  with st.spinner("predicting.."):
    import time
    time.sleep(2)
final_ans= model.predict(all_ans)[0]
if final_ans == 0:
    print("❎Customer will not buy Insurance❎")
else:
    print("✔️Customer will buy Insurance✔️")

