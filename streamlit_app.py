import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
myfruitlist = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
myfruitlist = myfruitlist.set_index('Fruit')

fruitselected = streamlit.multiselect("Pick some fruits:",list(myfruitlist.index),['Avocado','Strawberries'])
fruittoshow = myfruitlist.loc[fruitselected]
streamlit.dataframe(fruittoshow)
# New section to display fruityvice api response
streamlit.header('FruityVice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you ilke information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) - Not required can be deleted

#Normalize the json output
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
