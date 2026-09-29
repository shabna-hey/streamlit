import streamlit as st
from libart_db import BookListCreateRetriveUpdateDelete
st.title("DELETE NEW RECORD")
i=st.number_input("ID",min_value=0)

btn=st.button("Delete")
if btn:
    book_instance = BookListCreateRetriveUpdateDelete()
    records= book_instance.Delete(i)
    print(records)
    if records:
        st.success("record delete successfully")

    else:
        st.info("no record found")