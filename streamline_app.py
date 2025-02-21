import streamlit as st
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

"""
# Lesson python
hi, this is our new super application, dajeee
"""

[1,2,3,4]

"""
# Birthday paradox
"""

def generate_class():
    return [randint(1,365) for _ in range(27)]
    
if "experiments" not in st.session_state:
    st.session_state["experiments"] = []

c = generate_class()

counter = 0

count = [c.count(i) for i in range(1, 366)]

countmap = [[0 for _ in range(31)] for _ in range(12)]

for i in range(12):
    for y in range(30):
        countmap[i][y] = count[y+30*i]

a = np.random.random((16,16))

plt.imshow(countmap, cmap = 'hot', interpolation = 'nearest')
st.pyplot(plt)

there_are_collisions = not len(set(c)) == len(c)

if there_are_collisions:
    st.write("there are collisions")
else: 
    st.write("there are no collisions")

st.session_state.experiments.append(there_are_collisions)

estimate_prob = st.session_state.experiments.count(True)/len(st.session_state.experiments)

st.write(estimate_prob)

st.write("number of experiments so far:", len(st.session_state.experiments))

st.button("generate another class")

reload = st.toggle("autoreload")

if st.button("reset"):
    st.session_state.experiments = []

st.write(reload)

if reload:
    sleep(0.1)
    st.rerun()

def p_at_time_t(t):
    exps = st.session_state.experiments[:t]
    return sum(exps)/t

estimates = [p_at_time_t(t) for t in range (1, len(st.session_state.experiments))]

if len(estimates):
    st.line_chart(estimates)

import matplotlib.pyplot as plt

labels = ["Collision", "Not Collision"]
sizes = [st.session_state.experiments.count(True),
         st.session_state.experiments.count(False)]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=(0.01,0))

st.pyplot(plt)
    
