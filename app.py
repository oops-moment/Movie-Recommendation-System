import streamlit as st
st.title('Movie Recommender System')

# we need text box where user will type
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)