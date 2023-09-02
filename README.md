# Streamlit Experiments and Study #

The main purpose of this github is to study streamlit, make connection with Snowflake and make apps.
Reference link from streamlit: [https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake]
Reference link from snowflake: [https://learn.snowflake.com/courses/course-v1:snowflake+ESS-DABW+A/courseware/5d40c281b43b49b2acdc619174faeaca/74594ee530bb4b19bd9dd4c5045cdf0c/]

## Accounts Requirements ##
- Github/Gitlab
- Streamlit Account
- Snowflake Account

$$ Tools Requirements
- Python
- Snowpark

### Set up ###
- Python 3.11
1. pip install "snowflake-snowpark-python[pandas]"

- Github
1. Create a repo.
2. 

2.1 Requirements.txt for python connection.
'''
#requirements.txt
snowflake-connector-python
'''

2.2 streamlit_app.py

- Snowflake
1. Create a database
2. Create WH, schema and table.

- Streamlit 
1. Click  "New App"
2. put the repo you've just created. the branch you would deploy the app. The streamlit_app.py to main file path.
3. Deploy the app. Click the 3 dot on the app in the main page, set up streamlit.secret with the following format

'''
# .streamlit/secrets.toml

[connections.snowpark]
account = "xxx"
user = "xxx"
password = "xxx"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
client_session_keep_alive = true
'''
