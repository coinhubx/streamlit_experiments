import streamlit as st
import snowflake.connector
#import pandas as pd
import requests

### Snowflake connection
sn_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
sn_cur = sn_cnx.cursor()

#total count
sn_cur.execute("SELECT COUNT(1) FROM RAW.CHICAGO_CRIMES;")
total_cnt = sn_cur.fetchall()

#Group by 


### Set the title/header
st.set_page_config(layout='wide')
st.header('Welcome to my streamlit/snowflake experiments.')
st.subheader('Hope you enjoy my learning journey!')

## Layout
col1, col2, col3, col4 = st.columns((2,1,1,1))
with col1:
	st.write('Dataset general information')
	st.write(f'there are {total_cnt[0]} rows!')
	
with col2:
	st.write('Bar chart group by primary_type')
	sn_cur.execute("select Primary_Type, count(1) from RAW.CHICAGO_CRIMES group by Primary_Type order by Primary_Type;")
	fetch_ptg = sn_cur.fetchall()
	prim_type_grp = st.dataframe(fetch_ptg)
	#st.bar_chart(prim_type_grp)
	
with col3:
	st.write('3rd column')
	
with col4:
	st.write('4th column')
