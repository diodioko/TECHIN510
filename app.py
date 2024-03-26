import streamlit as st
from annotated_text import annotated_text

annotated_text(
    "This ",
    ("is", "Verb"),
    " some ",
    ("annotated", "Adj"),
    ("text", "Noun"),
    " for those of ",
    ("you", "Pronoun"),
    " who ",
    ("like", "Verb"),
    " this sort of ",
    ("thing", "Noun"),
    ". ",
    "And here's a ",
    ("word", ""),
    " with a fancy background but no label.",
)

st.image('./images/profile3.png', width=400)