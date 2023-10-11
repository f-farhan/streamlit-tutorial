# More Streamlit Functions
#Basic Text Elements
import streamlit as st
st.title("I am Streamlit Web App")
#MARKDOWN
st.markdown("**Hello** *World*")
st.markdown("## HEADING") #check more in documentation(https://www.youtube.com/redirect?event=comments&redir_token=QUFFLUhqbFZGWHNjZXVnVGRpUmhuVEVpQXczQUhLeXl6UXxBQ3Jtc0ttb3FiRjE2dk90WlZxZ0p2NnZXN1RyS1N6Q242blNsbUEwTmVZQUJSbl91YTlGaTlqcC1vOWdVYzFqZDZTbGxzZWhVWkVBNXVqWEVHaHRVdlM4X2FMbzJ4OWdtUnFOLWc4MUdkNjRnNlFUcWhPVTRyTQ&q=https%3A%2F%2Fwww.markdownguide.org%2Fcheat-sheet%2F&stzid=UgyDgrA-TD_F5mj7GN14AaABAg.9rTecMtsye89rUKSWfBHPM)
st.markdown("[Google](https://www.google.com)")
#Caption
st.caption("This is a caption")
#Mathematical Expressions
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") #check more in https://katex.org/docs/supported.html

#Json Function
json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)

#CODE
code = """
print("This is a code snippet")
def nothing():
    pass"""
st.code(code,language="python")




