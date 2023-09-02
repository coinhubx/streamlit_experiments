import streamlit as st

st.set_page_config(layout='wide')

st.header('Welcome to my streamlit/snowflake experiments.')
st.subheader('Hope you enjoy my learning journey!')

col1, col2, col3, col4 = st.beta_columns((2,1,1,1))

with col1:
	st.line_chart('first column')

with col2:
	st.area_chart('2nd column')
	
with col3:
	st.bar_chart('3rd column')
	
with col4:
	st.altair_chart('4th column')
