import streamlit as st
import pandas as pd
import time

st.title('Ralfs Comeback')

st.write('This is a simple example of a Streamlit app.')

st.write('You can easily add interactivity to your app by using Streamlit widgets.')

countdown_days = 20

st.write(f"Countdown: {countdown_days} days")

if st.button("Another day started"):
    countdown_days -= 1
    st.write(f"Countdown: {countdown_days} days")