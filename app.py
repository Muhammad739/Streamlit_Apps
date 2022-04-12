import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Make Containers

header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:

    st.title("Kashti ki app")
    st.text ("In this project we will work on kashti data")

with data_sets:
    st.header("Kashti doop gaye, Hawww!")
    st.text ("We will work with Titanic dataset")

    # Import data
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head(10))

    st.subheader("Sambha, Are ooh sambha, kitnay aadmi thay?")
    st.bar_chart(df["sex"].value_counts())

    # Other Plots
    st.subheader("Class kay hisaab se faraq")
    st.bar_chart(df["class"].value_counts())

    # Barplot
    st.bar_chart(df["age"].sample(10))



with features:
    st.header("These are our app feature")
    st.text ("Awen bohut saray feature add kartay hain, asaan he hai")
    
    st.markdown("1. **Fature 1:** This will teell us pata nahi kya")
    st.markdown("2. **Fature 2:** This will teell us pata nahi kya")


with model_training:
    st.header("Kashti walon ka kia bana?-Model Training")
    st.text ("Is may hum apnay parameters koh kum yah ziada karaingay")

    #Making Columns

    input, display = st.columns(2)


    #First column main app kay selection points hun
    max_depth = input.slider("How many people do you know?", min_value=10, max_value= 100, value = 20, step=5)


#n_estimators
n_estimators = input.selectbox ("How many tree should be there in a RF", options= [50, 100, 200, 300, "No limit"])


# Adding list of feature
input.write(df.columns)



# Input features from user
input_features = input.text_input("Which feature should we use?")

#  Machine Learning Model
model = RandomForestRegressor(max_depth = max_depth, n_estimators=n_estimators)
# Yahan per hum aik condition lagayen gay
if n_estimators == "No limit":
    model == RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)


# Define X and y

X = df[[input_features]]
y = df[["fare"]]

model.fit(X, y)
pred = model.predict(y)

#Display Metrices

display.subheader("Mean absolute error of the model is: ")
display.write(mean_absolute_error(y, pred))
display.subheader("Mean squared error of the model is: ")
display.write(mean_squared_error(y, pred))
display.subheader("R squared score of the model is: ")
display.write(r2_score(y,pred))