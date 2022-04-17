import streamlit as st

from api_wrapper import PokeApi

"""
This is a little test to see how Streamlit works
"""


poke_number = st.slider("Number of the Pokemon to find", 1, 1, 151)

poke_data = PokeApi().find_pokemon_by_number(poke_number)
col1, col2 = st.columns(2)
col1.write("Pokemon Name: ")
col1.write(poke_data["name"])
col2.write("Pokemon Abilities: ")
col2.json(poke_data["abilities"])
