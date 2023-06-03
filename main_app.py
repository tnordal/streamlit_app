"""main_app.py
"""

import streamlit as st
import pandas as pd

table = pd.DataFrame(
    {
        'Column 1': [1,2,3,4,5,6],
        'Column 2': [7,8,9,10,11,12]
    }
)

# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

hide_footer = """
    <style>
    .css-cio0dv.e1g8pov61
    {visibility: hidden;}
    </style>
    """

st.markdown(hide_footer, unsafe_allow_html=True)

st.title("Tom's Streamlit App")
st.header("Tom's Streamlit App")
st.subheader("Made for fun and education")
st.text("Plain text")
st.markdown("# Markdown top heading")
st.markdown("---")
st.latex(r"\left(\LARGE{AB}\right)")
json = {
    'Contry': 'Norway',
    'People': 5_3_00_000
}
st.json(json)

my_py = """
def sum(x, y):
    return x + y
"""

st.code(my_py, language='python')
st.write("# Write any thing... # Top Heading")
st.metric(label='Power Usage', value='2800kwh', delta='-300kwh', delta_color='inverse')
st.table(table)
st.dataframe(table)
st.image('IMAG0163_small.jpg')

# Video not working
# with open('Viaplay_4.wmv', 'rb') as v:
#     st.video(v)

stat = st.checkbox('Sey hi')
if stat:
    st.write('Hello Tom, you are the best!')

def change():
    print(st.session_state.buy)

st.checkbox('Buy?', value=True, on_change=change, key='buy')
