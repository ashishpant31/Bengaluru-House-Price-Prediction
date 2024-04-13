# pipeline to connect ML model

import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load your CSV data
data = pd.read_csv('Cleaned_data.csv')

# load your ML model
with open("RidgeModel.pkl", 'rb') as file:
    pipe = pickle.load(file)

def format_price(price):
    formatted_price = "₹ {:,.1f}".format(price)
    return formatted_price

def main():
    st.title('House Price Prediction Range')

    st.markdown("### Enter Property Details")
    locations = ['Select your location'] + sorted(data['location'].unique())
    location = st.selectbox('Select Location', locations, index=0)

    col1, col2, col3 = st.columns(3)
    with col1:
        bhk = st.number_input('BHK', min_value=0, value=0)
    with col2:
        bath = st.number_input('Bathrooms', min_value=0, value=0)
    with col3:
        sqft = st.number_input('Total Sqft', value=0.0)

    if location != 'Select your location' and st.button('Predict'):
        input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
        prediction = pipe.predict(input_data)[0] * 1e5
        prediction = abs(prediction)

        margin_of_error = 0.05
        lower_bound = prediction * (1 - margin_of_error)
        upper_bound = prediction * (1 + margin_of_error)

        formatted_lower_bound = format_price(lower_bound)
        formatted_upper_bound = format_price(upper_bound)

        st.markdown("### Predicted Price Range")
        st.success(f'{formatted_lower_bound} - {formatted_upper_bound}')

        prices = [lower_bound, upper_bound]
        price_labels = ['Lower Bound', 'Upper Bound']

        chart_data = pd.DataFrame({'Price Range': prices}, index=price_labels)
        st.bar_chart(chart_data, use_container_width=True)

if __name__ == '__main__':
    main()
