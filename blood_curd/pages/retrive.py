import streamlit as st

from blood_db import DonorListCreateRetriveUpdateDelete
st.title("donor DETAILS")
i=st.number_input("ID",min_value=0)

btn=st.button("Retrive")
if btn:
    do = DonorListCreateRetriveUpdateDelete()
    records= do.Retrive(i)
    print(records)
    if records:

        st.write("name:", records[1])
        st.write("blood group:", records[2])
        st.write("phone:", records[3])
        st.write("city:", records[4])
        st.write("last donation:", records[5])
    else:
        print("no record found")