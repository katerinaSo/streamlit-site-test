import streamlit as st
import pandas as pd
data={
	"series_1":[1,2,3,4,5],
	"series_2":[10,20,30,40,50]
}
df=pd.DataFrame(data)
st.title('first streamlit app')
st.subheader('add subheader')
st.write('''multiline \n
            text 
             goes here''')

st.write(df)
