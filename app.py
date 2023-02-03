# this is first streamlit app
import streamlit as st
import pandas as pd
import numpy as np


st.title('My first app')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

# add a line chart
st.line_chart(df)

# add a checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# add a selectbox
option = st.selectbox(
    'Which number do you like best?',
        df['first column'])

'You selected: ', option

# add a slider
option = st.slider('Select a value', 0, 10, 5)
'You selected:', option