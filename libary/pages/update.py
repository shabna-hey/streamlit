import streamlit as st

from libart_db import BookListCreateRetriveUpdateDelete

st.title("UPDATE NEW RECORD")
id=st.number_input("ID",min_value=0)
title=st.text_input("TITLE")
author=st.text_input("AUTHOR")
price=st.number_input("PRICE",min_value=0)
langauge=st.text_input("LANGauge")
pages=st.text_input("PAGES")

btn=st.button("update")
if btn:
    book_instance=BookListCreateRetriveUpdateDelete()
    records =book_instance.Update(title,author,price,langauge,pages,id)

    print(records)
    if records:
        st.success("updated record successfully")
    else:
        st.info("no record found")
