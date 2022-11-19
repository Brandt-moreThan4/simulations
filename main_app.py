import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import params as P
import streamlit.components.v1 as components

plt.style.use('ggplot')


components.html('<h1>LOLOO<h1>')

st.title('Simulating Retirement')

with open('markdown_stuff.md') as f:
    mk_text = f.read()
st.write(mk_text)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

def run_simulations():
    x = range(age)
    y = np.power(x,2)

    return (x,y)

x, y = run_simulations()

df = pd.DataFrame()
df['x'] = x
df['y'] = y

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_title(f'$f(x) = x^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')

# st.line_chart(df)

st.pyplot(fig)
