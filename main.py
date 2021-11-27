import streamlit as st
import pandas as pd
data={
	"series_1":[1,2,30,4,50],
	"series_2":[10,30,30,10,50]
}
df=pd.DataFrame(data)
st.title('first streamlit app')
st.subheader('add subheader')
st.write('''multiline \n
            text 
             goes here''')

st.write(df)
st.line_chart(df)
st.area_chart(df)
mySlider=st.slider('Celsius')
st.write(mySlider,' in Fahrenheit  ',mySlider*9/5+32)