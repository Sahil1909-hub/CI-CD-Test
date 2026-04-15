import streamlit as st

st.title('Power Calculator')
st.write('Enter any number to get the cube, square and fifth power')

user_input = st.number_input('Enter any number: ', value=1, step=1)

square = user_input ** 2
cube = user_input ** 3
fifth = user_input ** 5

st.write(f'The square for {user_input} is {square}')
st.write(f'The cube for {user_input} is {cube}')
st.write(f'The fifth for {user_input} is {fifth}')

