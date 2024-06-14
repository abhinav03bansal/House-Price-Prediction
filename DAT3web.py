import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('house.sav','rb'))
st.title("Welcome to House Price Prediction")
abc={
    "Yes":1,
    "No":2
}
new={
    "Furnished":1,
    "Semi Furnished":0.5,
    "unfurnished":0
}
area=st.number_input("Area")
bedrooms=st.slider("Bedrooms",min_value=0,max_value=8)
bathrooms=st.slider("Bathroom",min_value=0,max_value=8)
stories=st.slider("Stories",min_value=0,max_value=8)
mainroad=st.selectbox("Main Road",list(abc.keys()))
guestroom=st.selectbox("Guest Room",list(abc.keys()))
basement=st.selectbox("Basement",list(abc.keys()))
hotwaterheating=st.selectbox("Hot Water",list(abc.keys()))
airconditioning=st.selectbox("Air Conditioning",list(abc.keys()))
parking=st.slider("Parking",min_value=0,max_value=8)
prefarea=st.selectbox("Preferred area",list(abc.keys()))
furnishingstatus=st.selectbox("Hot Water",list(new.keys()))
mainroad=abc[mainroad]
guestroom=abc[guestroom]
hotwaterheating=abc[hotwaterheating]
airconditioning=abc[airconditioning]
basement=abc[basement]
prefarea=abc[prefarea]
furnishingstatus=new[furnishingstatus]
btn=st.button("Predict")
if btn:
    pred=model.predict([[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]])[0]
    print(pred)

    st.subheader(pred)