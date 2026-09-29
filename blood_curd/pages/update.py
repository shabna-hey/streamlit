import streamlit as st

from blood_db import DonorListCreateRetriveUpdateDelete
st.title("UPDATE NEW RECORD")

id=st.number_input("ID",min_value=0)
name=st.text_input("NAME")
blood_group=st.text_input("BLOOD GROUP")
phone=st.number_input("PHONE NO",min_value=0)
city=st.text_input("CITY")
last_donation=st.date_input("DATE OF LAST DONATION")

btn=st.button("update")
if btn:
    do=DonorListCreateRetriveUpdateDelete()
    records =do.Update(id,name,blood_group,city,phone,last_donation)

    print(records)
    if records:
        st.success("updated record successfully")
    else:
        st.info("no record found")