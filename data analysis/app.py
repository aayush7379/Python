import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

years = list(map(str,range(1980,2014)))
# loading data 
@st.cache_data
def load_data():
   df = pd.read_excel('Canada.xlsx', sheet_name=1 ,skiprows=20 ,skipfooter=2)
   cols_to_rename = {
    'OdName':'country',
    'AreaName':'continent',
    'RegName' : 'region',
    'DevName'  : 'development'
    }
   df= df.rename(columns=cols_to_rename)
   cols_to_drop = ['AREA','Type','Coverage']
   df =df.drop(columns=cols_to_drop)
   df = df.set_index('country')
   df.columns = [str(name).lower() for name in df.columns.tolist()]
   df['total']= df[years].sum(axis=1)
   return df

# adding layout and widget
st.title("imagigration analysis")
with st.spinner("loading data...."):
 df = load_data()
 st.success("data loaded successfully")

 with st.expander("show data"):
   st.dataframe(df,use_container_width=True)

countries =df.index.tolist()
selected_country = st.selectbox("select a country",countries)
imm_data = df.loc[selected_country,years]
#st.write(imm_data)
fig = px.area(imm_data,
              x=imm_data.index,
              y=imm_data.values)
st.plotly_chart(fig,use_container_width=True)