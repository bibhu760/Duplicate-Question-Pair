import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')
<<<<<<< HEAD

# Custom CSS to set background color


=======
>>>>>>> c4dea4e64612f1a066fe19fadc36494978db0cf3
q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

