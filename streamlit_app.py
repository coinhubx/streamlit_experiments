import streamlit as st

### Snowflake connection
sn_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
sn_cur = sn_cnx.cursor()
sn_cur.execute("SELECT COUNT(1) FROM RAW.CHICAGO_CRIMES;")
data_row = sn_cur.fetchall()


### Set the title/header
st.set_page_config(layout='wide')
st.header('Welcome to my streamlit/snowflake experiments.')
st.subheader('Hope you enjoy my learning journey!')

##


## Layout
col1, col2, col3, col4 = st.columns((2,1,1,1))
with col1:
	st.write('first column')
	#st.write(f'there are {data_row} rows!')

with col2:
	st.write('2nd column')
	
with col3:
	st.write('3rd column')
	
with col4:
	st.write('4th column')
