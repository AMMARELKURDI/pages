import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px


@st.cache_data
def load_data(file):
    return pd.read_csv(file)
df=st.file_uploader("Upload your file",type=["csv"])
if df is not None:
    data=load_data(df)
    no_row=st.slider("Chosse Number of Rows",1,len(data),10,5)
    col_to_show=st.multiselect("Select columns in DataFrame", data.columns.to_list(),default=data.columns.to_list())
    numeric_col=data.select_dtypes(include=np.number).columns.to_list()
    st.write(data[:no_row][col_to_show])
    
    tab1,tab2=st.tabs(["Scatter Plot","Histogram Plot"])
    with tab1:
        c1,c2,c3=st.columns(3)
        with c1:
            x_col=st.selectbox("Choose X value",numeric_col)
        with c2:
            y_col=st.selectbox("Choose Y value",numeric_col)
        with c3:
            color_col=st.selectbox("Choose Coloring",data.columns.to_list())
        fig1=px.scatter(data,x=x_col,y=y_col,color=color_col)
        st.plotly_chart(fig1,use_container_width=True)
    with tab2:
        
        Hist_col=st.selectbox("Choose Histo Column",numeric_col)
        fig2=px.histogram(data,Hist_col)
        st.plotly_chart(fig2,use_container_width=True)