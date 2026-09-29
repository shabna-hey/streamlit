import streamlit as st
from libart_db import BookListCreateRetriveUpdateDelete

st.title("ADD NEW RECORD")


id=st.number_input("ID",min_value=0)
title=st.text_input("TITLE")
author=st.text_input("AUTHOR")
price=st.number_input("PRICE",min_value=0)
langauge=st.text_input("LANGauge")
pages=st.text_input("PAGES")

btn=st.button("click")
if btn:
    book_instance=BookListCreateRetriveUpdateDelete()
    book_instance.Create(id,title,author,price,langauge,pages)

    st.success("create record successfully")


