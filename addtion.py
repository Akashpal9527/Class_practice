import streamlit as st
st.set_page_config(page_title="number addtion",page_icon="🎬",layout="centered")
st.title("Hello Akash Bhai")
st.caption("Enter Two nmber and it will return addtion of them")
form=st.form("Add_form")
num1=form.number_input("enter first number")
num2=form.number_input("enter second number")
submit=form.form_submit_button("Calculated Sum")
submit1=form.form_submit_button("Calculated sub")
if submit:
    result=num1+num2
    st.divider()
    st.metric(label="Result",value=result)
if submit1:
    result2=num1-num2
    st.divider()
    st.metric(label="Result2",value=result2)

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df