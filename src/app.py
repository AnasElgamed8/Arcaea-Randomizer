import streamlit as st

from Sheet import Sheet

test_sheet = Sheet()
st.title("Arcaea random chart picker")
min_constant = st.number_input("Pick the minimum allowed constant:",step=0.1,min_value=1.0,)
max_constant = st.number_input("Pick the maximum allowed constant:",step=0.1,min_value=min_constant)
size = st.number_input("How many charts do you want?",1)
st.dataframe(test_sheet.true_random(min_constant,max_constant,size))
