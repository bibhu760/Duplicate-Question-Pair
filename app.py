import streamlit as st
from statsmodels.graphics.tukeyplot import results

import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')
page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Change to fixed if preferred */
        }}
        [data-testid="stHeader"] {{
        background: rgba(0,203,0,0);
        }}
    </style>
"""
q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

