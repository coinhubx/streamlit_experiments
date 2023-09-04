import streamlit as st
import snowflake.connector
import pandas as pd
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
col1, col2, col3, col4 = st.columns((1,2,1,1))
with col1:
	st.write('Dataset general information')
	st.write(f'there are {total_cnt[0][0]} rows in the table!')
	
with col2:
	st.write('Bar chart group by primary_type')
	sn_cur.execute("select * FROM RAW.SUMMARY_CRIME_COUNTS;")
	ptg = sn_cur.fetchall()
	#st.write(ptg.columns)
	st.dataframe(ptg)
	
	st.write('------------')
	st.write('st.text_input demo - max_chars sets max characters allowed. if exceed, copy/paste disabled')
	text = st.text_input('Insert the primary type.', value = 'ROBBERY', max_chars = 30)
	
	sn_cur.execute(f"select * FROM RAW.SUMMARY_CRIME_COUNTS WHERE PRIMARY_TYPE = '{text}';")
	
	st.write('st.button demo - 2 buttons')
	st.button("Reset", type="primary")
	if st.button('Submit'):
		ptg = sn_cur.fetchall()
		st.dataframe(ptg)
	
	st.write('------------')
	st.write('st.multiselect : select from the list provided.')
	sn_cur.execute(f"select distinct PRIMARY_TYPE FROM RAW.SUMMARY_CRIME_COUNTS;")
	ptg_list = sn_cur.fetchall()
	options = st.multiselect('Select the primary type(s)', list(map(lambda x: x[0], ptg_list)))
	
	

	
with col3:
	st.write('3rd column')
	
with col4:
	st.write('4th column')
