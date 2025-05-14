import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data=pd.read_excel('pandas28.xlsx')
st.sidebar.subheader('Filter')
branches=data['Branch'].unique()
s=st.sidebar.selectbox(label='Branchs',options=branches)
image=st.sidebar.image('profit.gif')
data=data[data['Branch']==s]
kpis,quantity,sales,target=st.tabs(['kpis','quantity','sales','target'])
with kpis:
    orders = data['Invoice ID'].count()
    total_sales = np.round(data['Total'].sum(), 1)
    total_quantity = data['Quantity'].sum()
    avg_rating=np.round(data['Rating'].mean(),1)
    col1,col2,col3,col4=st.columns([1,1,1,1])
    col1.metric(label='orders',value=orders)
    col2.metric(label='Total Sales', value=total_sales)
    col3.metric(label='Total Quantity', value=total_quantity)
    col4.metric(label='avg_Rating', value=avg_rating)
with quantity:
    v1 = data.groupby('Product line')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
    v2 = data.groupby('Gender')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)

    bar1=px.bar(v1,x='Product line',y='Quantity',text_auto='.2s')
    pie1=px.pie(v2,names='Gender',values='Quantity')
    st.plotly_chart(bar1)
    st.plotly_chart(pie1)

with sales:
    v1 = data.groupby('Product line')['Total'].sum().reset_index().sort_values(by='Total', ascending=False)
    v2 = data.groupby('Gender')['Total'].sum().reset_index().sort_values(by='Total', ascending=False)

    bar1=px.bar(v1,x='Product line',y='Total',text_auto='.2s')
    pie1=px.pie(v2,names='Gender',values='Total')
    st.plotly_chart(bar1)
    st.plotly_chart(pie1)

with target:
    target_sales=110000
    fig = go.Figure(
         go.Indicator(mode='number+gauge+delta', value=data['Total'].sum(), domain={'x': [0, 1], 'y': [0, 1]},
                     title={'text': 'Sales'}, delta={'reference': target_sales}, gauge={'axis': {'range': [0, target_sales]}}))
    target_quantity=1000
    fig1 = go.Figure(
        go.Indicator(mode='number+gauge+delta', value=data['Quantity'].sum(), domain={'x': [0, 1], 'y': [0, 1]},
                     title={'text': 'Quantity'}, delta={'reference': target_quantity},
                     gauge={'axis': {'range': [0, target_quantity]}}))
    target_rating=8
    fig2 = go.Figure(
        go.Indicator(mode='number+gauge+delta', value=data['Rating'].mean(), domain={'x': [0, 1], 'y': [0, 1]},
                     title={'text': 'Rating'}, delta={'reference': target_rating},
                     gauge={'axis': {'range': [0, target_rating]}}))
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
