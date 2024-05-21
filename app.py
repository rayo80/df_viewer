import streamlit as st
import pandas as pd
import streamlit_pandas as sp

file = "./data/P_OLT_C600_SAN_JUAN_1-1-1.csv"

@st.cache_data
def load_data():
    dfr = pd.read_csv(file)
    return dfr


df = load_data()

create_data = {
    "STATUS_ONT": "select",
    "LINE_ID": "text",
    "VNO_CODE": "text",
    "DIVICAU": "multiselect",
    "CTO": "multiselect"
}

all_widgets = sp.create_widgets(df, create_data, ignore_columns=['LastOff', 'SN', 'ONU_ID'])

res = sp.filter_df(df, all_widgets)
st.title("SAN JUAN")

st.header("Original")
st.write(df)

st.header("Filtrados")
st.write(res)
