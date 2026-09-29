import streamlit as st

from libart_db import BookListCreateRetriveUpdateDelete
st.title("BOOK DETAILS")
i=st.number_input("ID",min_value=0)

btn=st.button("Retrive")
if btn:
    book_instance = BookListCreateRetriveUpdateDelete()
    records= book_instance.Retrive(i)
    print(records)
    if records:

        st.write("title", records[1])
        st.write("author", records[2])
        st.write("price", records[3])
        st.write("language", records[4])
        st.write("pages", records[5])
    else:
        print("no record found")