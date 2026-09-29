import streamlit as st
from blood_db import DonorListCreateRetriveUpdateDelete
st.title("read NEW RECORDS")


do=DonorListCreateRetriveUpdateDelete()
records=do.List()
print(records)
if records:
    st.table(records)
else:
    st.info("no records")