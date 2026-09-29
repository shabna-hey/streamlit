
import streamlit as st
from blood_db import DonorListCreateRetriveUpdateDelete
st.title("DELETE NEW RECORD")
i=st.number_input("ID",min_value=0)

btn=st.button("Delete")
if btn:
    do = DonorListCreateRetriveUpdateDelete()
    records= do.Delete(i)
    print(records)
    if records:
        st.success("record delete successfully")

    else:
        st.info("no record found")