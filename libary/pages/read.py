import streamlit as st
from libart_db import BookListCreateRetriveUpdateDelete

st.title("READ NEW RECORD")
book_instance=BookListCreateRetriveUpdateDelete()
records=book_instance.List()
print(records)
if records:

    st.table(records)
else:
    st.info("no records")