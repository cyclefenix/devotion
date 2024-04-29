import streamlit as st

def hello_page(md=None):
    # Define the JavaScript code
    javascript_code = """
    <script>
        function greet() {
            alert("Hello, Streamlit!");
        }
    </script>
    """

    # Display the JavaScript code using st.markdown
    st.markdown(javascript_code, unsafe_allow_html=True)

    # Add a button that triggers the JavaScript function
    if st.button("Say Hello"):
        st.markdown('<script>greet();</script>', unsafe_allow_html=True)



def main_page(md=None):
    st.markdown('# Welcome to Devotion Page')
    st.markdown('### By cyclefenix')

def render_page(md=None):
    with open(md, "r") as f:
        reader = f.read()
    st.markdown(reader)

pages = {
    "Main" : main_page,
    "Daily Office" : render_page,
    "Jonah" : render_page,
    "Psalm" : render_page,
    # "Hello world" : hello_page,
}

md_loader = {
    "Main" : None,
    "Daily Office" : "assets/dailyoffice.md",
    "Jonah" : "assets/jonah.md", 
    "Psalm" : "assets/psalm.md",
    # "Hello world" : None,
}

selected_page = st.sidebar.radio("Navigation", list(pages.keys()))
md = md_loader[selected_page]
pages[selected_page](md=md)

if md is not None:
    st.write("All Glory to God!")