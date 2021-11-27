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

file_csv = st.file_uploader("Upload a CSV file", type=([".csv"]))

if file_csv:

    file_csv_bytes = st.file_reader(file_csv)
    data_csv = file_csv_bytes.decode('utf-8').splitlines()
    reader = csv.reader(data_csv, quoting=csv.QUOTE_MINIMAL)

    results = []
    for row in reader: # each row is a list
        results.append(row)

    st.dataframe(results)


file_png = st.file_uploader("Upload a PNG image", type=([".png"]))

if file_png:
    file_png_bytes = st.file_reader(file_png)
    st.image(file_png_bytes)