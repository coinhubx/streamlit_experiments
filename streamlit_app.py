import streamlit as st
import snowflake.connector
import pandas as pd
import requests
import datetime

### Snowflake connection
sn_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
sn_cur = sn_cnx.cursor()

### Set the title/header
st.set_page_config(layout='wide')

st.title(':blue[Chicago Crime] Database :cop:')
st.caption('streamlit experiments')
st.divider()

st.header('Summary', divider = 'rainbow')
#read the materialized view
sn_cur.execute("select * FROM RAW.SUMMARY_CRIME_COUNTS;")
data = sn_cur.fetchall() #fetch_pandas_all() doesn't work here.
df_columns = list(map(lambda x :x[0], sn_cur.description))
ptg_pd = pd.DataFrame(data, columns = df_columns) #a pandas dataframe with column names
ptg_pd = ptg_pd.set_index('PRIMARY_TYPE') #set column name

## Layout
col1, col2, col3 = st.columns((1,2,2))
with col1:
	'Dataset general information'
	f"there are {ptg_pd['COUNT'].sum()} rows in the table!"
	
with col2:
	'Bar chart group by primary_type'
	ptg_pd
	
	'st.text_input demo - max_chars sets max characters allowed. if exceed, copy/paste disabled'
	selected_in_text = st.text_input('Insert the primary type.', value = 'ROBBERY')#, max_chars = 30)
	
	'st.button demo - 2 buttons'
	st.button("Reset", type="primary")
	if st.button('Submit'):
		sit_text_list = list(map(lambda y: y.strip().upper(), selected_in_text.split(',')))
		try:
			df_sit = ptg_pd.loc[sit_text_list]
			df_sit
		except KeyError as e:
			':red[**Error occurs**] - please check your spelling.'
	

	'st.multiselect : select from the list provided.'
	options = st.multiselect('Select the primary type(s)', ptg_pd.index)
	#st.write(options) # for debug
	df_to_show = ptg_pd.loc[options]
	df_to_show
	
	
with col3:
	'input widget - slider'
	num_selected = st.slider('What number', 0, 500, 100)
	df3_to_show = ptg_pd[ptg_pd['COUNT']< num_selected]
	df3_to_show

	'bar chart'
	# pick color for the bar
	color_picked = st.color_picker('pick a color for the bar chart', '#f774d8')
	st.bar_chart(ptg_pd, color = color_picked)
	
st.divider()

st.header('REPORT AREA', divider = 'rainbow')

start_date = st.date_input("START_DATE", datetime.date(2023, 7, 1), format="YYYY-MM-DD")
end_date = st.date_input("END_DATE", datetime.date(2023, 7, 31), format="YYYY-MM-DD")
	
'st.button demo - 2 buttons'
st.button("Reset", key = 'resetrptreset')
if st.button('Submit', key = 'resetrptsubmit'):
	
	try:

		sn_cur.execute(f"select top 10 * FROM RAW.CHICAGO_CRIMES where to_date(date) between {start_date.strftime('%Y-%m-%d')} and {end_date.strftime('%Y-%m-%d')};")
		data_rpt = sn_cur.fetchall() #fetch_pandas_all() doesn't work here.
		df_columns_rpt = list(map(lambda x :x[0], sn_cur.description))
		ptg_pd_rpt = pd.DataFrame(data_rpt, columns = df_columns_rpt) #a pandas dataframe with column names
		ptg_pd_rpt = ptg_pd_rpt.set_index('ID') #set column name

	except KeyError as e:
		':red[**Error occurs**] - please check your spelling.'

