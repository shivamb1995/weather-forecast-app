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

if place:
    try:
        # Get temperature/sky data
        filtered_data = get_data(place=place,days=days)

        if option == 'Temperature':
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates,y=temperatures,labels={'x':'Date','y':'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images_path = {'Clear':'images/clear.png',
                    'Clouds':'images/cloud.png',
                    'Rain':'images/rain.png',
                    'Snow':'images/snow.png'}
            sky_conditions = filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
            images = [images_path[condition] for condition in sky_conditions]
            # print(sky_conditions)
            st.image(images,width=100)
    except KeyError:
        st.write('That place does not exist.')