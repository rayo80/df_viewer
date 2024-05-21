import streamlit as st
import pandas as pd
import streamlit_pandas as sp

file = "./data/titanic.csv"


@st.cache_data
def load_data():
    dfr = pd.read_csv(file)
    return dfr


df = load_data()

create_data = {
    "Name": "text",
    "Sex": "multiselect",
}

all_widgets = sp.create_widgets(df, create_data)
res = sp.filter_df(df, all_widgets)
st.title("SAN JUAN")
st.header("Original")
st.write(df)

st.header("Filtrados")
st.write(res)