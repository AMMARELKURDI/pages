import streamlit as st
import numpy as np
import time

def main():
    def inject_css():
        with open("./assets/style.css") as f:
            st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    inject_css()
    #SideBar
    
    with st.sidebar:
        st.title("Configration")
        shape= st.selectbox("Choose Shape",["Circle","Recangle"])

    st.header("Shape Calculation")
    area=None
    Perimeter=None
    
    if shape=="Circle":
        rad=st.number_input("Choose Raduis",min_value=0.0,max_value=300.0,step=0.5)
        area=rad*rad*3.14
        Perimeter=2*3.14*rad
    if shape=="Recangle":
        wd=st.number_input("Choose Width",min_value=0.0,step=0.5)
        hg=st.number_input("Choose Height",min_value=0.0,step=0.5)
        area=wd*hg
        Perimeter = 2*(wd+hg)
    com_btn=st.button("Compute your Calculations")
    if com_btn:
        with st.spinner("Computing......"):
            time.sleep(2)
            st.write("Area : ","{:.2f}".format(area))
            st.write("Perimeter : ","{:.2f}".format(Perimeter))
if __name__=="__main__":
    main()