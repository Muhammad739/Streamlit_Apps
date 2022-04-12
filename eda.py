import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# Webapp ka title

st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by Muhammad Bin Saqib Ali Called **EDA App**
''')

# How to upload a file from pc

with st.sidebar.header(" Upload your dataset (.csv"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=["csv"])
    df = sns.load_dataset("titanic")
    st.sidebar.markdown("[Exapmle CSV file](df)")


# Profiling report for pandas

if uploaded_file is not None:

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    
    df = load_csv()
    pr = ProfileReport(df, explorative = True)
    st.header("**Input DF**")
    st.write(df)
    st.write("---")
    st.header("**Profiling report with Pandas**")
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file, Upload kar bhi do abb ya kaam nahi karna")
    if st.button("Press to use example data"):

        #example dataset
        @st.cache
        def load_data():
            a= pd.DataFrame( np.random.rand(100,5),
            columns= ["age", "banana", "codanics", "Karachi", "Ear"])
            sns.barplot("age", "Karachi", data=a)
            return a

        df = load_data()
        pr = ProfileReport(df, explorative = True)
        st.header("**Input DataFrame**")
        st.write(df)
        st.write("---")
        st.header("**Profiling report with Pandas**")
        st_profile_report(pr)