import streamlit as st
import pandas as pd
import numpy as np

st.title("안녕하세요")
st.write("잠온다")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['A', 'B', 'C']
)

st.line_chart(data)