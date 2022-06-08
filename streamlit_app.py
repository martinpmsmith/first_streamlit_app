import streamlit
import pandas

streamlit.title("My Parents Healtyh New Diner")

streamlit.header("Breakfast Menu")
streamlit.text(" 🥑Omega 3  & Blueberry Oatmeal")
streamlit.text("🥣Kale, Spinach, and Rocket Smoothie")
streamlit.text("Hard Boiled from Free Range , Egg")
streamlit.text("🥑🍞 Avocado toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('fruit')

streamlit.multiselect('Pick a fruit', list(my_fruit_list.index))