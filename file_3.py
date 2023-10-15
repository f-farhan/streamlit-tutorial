# Display Elements of Streamlit
import streamlit as st
import pandas as pd
st.title("I am Streamlit Web App")
#Write Function
st.write("## H2") #See documentation
#Metrics
st.metric(label="Wind Speed",value="120ms⁻¹",delta="140ms⁻¹")
#Table
table = pd.DataFrame({"Col 1": [1,2,3,4,5,6],"Col 2": [10,20,30,40,50,60]})
st.table(table)
#DataFrame
st.dataframe(table)
