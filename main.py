import streamlit as st 
import plotly.express as px
from backend import get_data

st.set_page_config(layout='wide')
heading1 = 'Wether Forecast for next few days'
st.title(heading1)

# Enter place
place = st.text_input(label='Place:')

# Select Number of days
days = st.slider(min_value=1,max_value=5,
                 label='Set Forecast Days:',
                 help='Select the number of days for which you want the data.')

# Select data to view
option = st.selectbox(label='Select data to view:',
                      options=['Temperature','Sky'])

# Displaying the subheader
st.subheader(f'{option} for next {days} days in {place}')

# Calling the function from backend
d,t = get_data()
figure = px.line(x=d,y=t,label={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(figure)