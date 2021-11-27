import streamlit as st
import pandas as pd
from streamlit_cropper import st_cropper
from PIL import Image
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

# file_csv = st.file_uploader("Upload a CSV file", type=([".csv"]))

# if file_csv:

#     file_csv_bytes = st.file_reader(file_csv)
#     data_csv = file_csv_bytes.decode('utf-8').splitlines()
#     reader = csv.reader(data_csv, quoting=csv.QUOTE_MINIMAL)

#     results = []
#     for row in reader: # each row is a list
#         results.append(row)

#     st.dataframe(results)


# file_png = st.file_uploader("Upload a PNG image", type=([".png"]))

# if file_png:
#     file_png_bytes = st.file_reader(file_png)
#     st.image(file_png_bytes)


st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload an image and set some options for demo purposes
st.header("Cropper Demo")
# img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
# realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
# box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
# aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
# aspect_dict = {"1:1": (1,1),
#                 "16:9": (16,9),
#                 "4:3": (4,3),
#                 "2:3": (2,3),
#                 "Free": None}
# aspect_ratio = aspect_dict[aspect_choice]
img_file='car1.gif'
if img_file:
    img = Image.open(img_file)
    # if not realtime_update:
    #     st.write("Double click to save crop")
    # Get a cropped image from the frontend
    # cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
    #                             aspect_ratio=aspect_ratio)
    
    # Manipulate cropped image at will
    st.write("Preview")
    img.thumbnail((150,150))
    st.image(img)

custom_img = st.file_uploader(
    "You can upload a custom background image to replace the default black one with 640x1280 dimensions (otherwise it is resized)", 
    type=["png", "jpg"]
)
if custom_img:
	st.image(custom_img)