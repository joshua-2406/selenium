import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
from sqlalchemy import text
import psycopg2
import pandas as pd
# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query9
df = pd.DataFrame(conn.query("SELECT * FROM redbus"))

st.title("Auto Filter Dataframes in Streamlit")
st.write(
    """This app accomodates the blog [here](<https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/>)
    and walks you through one example of how the Streamlit
    Data Science Team builds add-on functions to Streamlit.
    """
)


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    modify = st.checkbox("Add filters")
    if not modify:
        return df
         

st.dataframe(filter_dataframe(df))











# import streamlit as st
# from sqlalchemy import text
# import psycopg2
# import pandas as pd
# # Initialize connection.
# conn = st.connection("postgresql", type="sql")

# # Perform query9
# df = pd.DataFrame(conn.query("SELECT * FROM redbus"))
# st.write(df)
