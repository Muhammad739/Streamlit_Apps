import streamlit as st
import plotly.express as px
import pandas as pd



# Import dataset
st.title("Plotly or Streamlit koh mila Kay app banana")
df = px.data.gapminder()
df1 = df
st.write(df)

st.write(df.columns)

# Summary stats
st.write(df.describe())


# Data management
year_option = df["year"].unique().tolist()

year = st.selectbox("Which year should we plot", year_option, 0)

df = df[df["year"] == year]


# Plotting
st.title("Normal PLot")
fig = px.scatter(df,x= "gdpPercap", y= "lifeExp", size="pop", color= "continent", hover_name="country"
                  ,log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90])

st.write(fig)


st.title("Animated Plot")
animated_fig = px.scatter(df1, x= "gdpPercap", y= "lifeExp", size="pop", color= "continent", hover_name="country"
                    ,log_x=True, size_max=55, range_x=[100, 100000], range_y=[20,90],
                    animation_frame="year", animation_group="country")

st.write(animated_fig)