import streamlit as st

from Sheet import Sheet


@st.cache_resource
def load_sheet():
    return Sheet()

test_sheet = load_sheet()

st.title("Arcaea random chart picker")
st.sidebar.title("Options")

left_column, right_column = st.columns(2)
if st.sidebar.checkbox("Single Value Mode"):
    max_constant = min_constant = left_column.number_input("Pick the constant:",step=0.1,min_value=1.0,max_value=12.0,value=1.0,key="mini")
    size = right_column.number_input("How many charts do you want?",1)

else:
    min_constant = left_column.number_input("Pick the minimum allowed constant:",step=0.1,min_value=1.0,max_value=12.0,value=1.0,key="mini") 
    max_constant = right_column.number_input("Pick the maximum allowed constant:",step=0.1,min_value=min_constant,max_value=12.0,value=12.0,key="maxi")
    size = st.number_input("How many charts do you want?",1)
if st.button("Randomize!",width="stretch",type='primary'):
    st.dataframe(test_sheet.true_random(min_constant,max_constant,size),hide_index=True)
