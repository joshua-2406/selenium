import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
import warnings 

from sqlalchemy import text
import psycopg2
import pandas as pd
warnings.filterwarnings('ignore') 
conn = st.connection("postgresql", type="sql")


df = pd.DataFrame(conn.query("SELECT * FROM redbus"))
df['price'] =df['price'].replace('',0).astype(int)


df['star_rating'] = df['star_rating'].replace({'':0,'New':0}).astype(float) 
df['star_rating'] = df['star_rating'].fillna(0)

st.title("Redbus Data Scraping Project")
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    
    modify = st.checkbox("Add filters")
    if not modify:
        return df
    df = df.copy()
 
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime('%H:%M')

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
   
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            # elif is_datetime64_any_dtype(df[column]):
            #     user_date_input = right.date_input(
            #         f"Values for {column}",
            #         value=(
            #             df[column].min(),
            #             df[column].max(),
            #         ),
            #     )
            #     if len(user_date_input) == 2:
            #         user_date_input = tuple(map(pd.to_datetime, user_date_input))
            #         start_date, end_date = user_date_input
            #         df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]
          
                    

    return df 

st.dataframe(filter_dataframe(df))





