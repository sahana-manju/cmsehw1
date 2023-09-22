import streamlit as st
import seaborn as sns
import pandas as pd
import seaborn as sd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
 
st.title('Wisconsin Breast Cancer Insights')
st.caption('EDA by group 3')
st.text('Lan Jin, Sandhya Kilari, Sahana Manjunath, Kyllan Wunder')
st.divider()
#graph
#st.pyplot(sns.scatterplot(data=df_iris, x='sepal_length', y='sepal_width', hue='species').figure)

 
#new scatter plot able to select x and y axis with st.selectbox
df_cancer = pd.read_csv('data.csv')
st.subheader('Scatterplot with input widgets')
x_axis = st.selectbox('Select x axis', df_cancer.columns)
y_axis = st.selectbox('Select y axis', df_cancer.columns)
#based on the selection, filter the data and display the graph
plot1=st.pyplot(sns.scatterplot(data=df_cancer, x=x_axis, y=y_axis, hue='diagnosis').figure)
plt.savefig("seaborn_plot.png")
with open("seaborn_plot.png", "rb") as file:
    btn = st.download_button(
            label="Download plot",
            data=file,
            file_name="seaborn_plot.png",
            mime="image/png"
          )

#Distribution
st.subheader('Distribution plot')
plot2=st.pyplot(sns.displot(df_cancer, x="radius_mean", hue = "diagnosis", col="diagnosis", kind="kde", rug=True))

#Categorical
st.subheader('Categorical plot')
plot3=st.pyplot(sns.catplot(df_cancer, x="diagnosis", y="concavity_mean", kind="swarm"))

#Relational
st.subheader('Relational plot')
plot4=st.pyplot(sns.relplot(df_cancer, x="radius_mean", y="fractal_dimension_worst", hue="diagnosis"))


