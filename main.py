import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
from datetime import datetime

#set path structure
today = datetime.today()
donations = Path.cwd() / 'data' / "donations.csv"

header = st.beta_container()
dataset1 = st.beta_container()
dataset2 = st.beta_container()
notes = st.beta_container()

with header:
    st.title("Paraclete Mission Group")
    st.header("Monthly Financials")

with dataset1:
    st.subheader('January 2021')
    st.text('Data Source: DonorPerfect')

    st.markdown('**YoY Donations**')

    #load donation data
    df = pd.read_csv(donations)
    
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', ascending=True)

    #format dates
    format = '%Y-%m-%d'
    df['Date'] = pd.to_datetime(df['date'], format=format)
    df = df.set_index(pd.DatetimeIndex(df['Date']))

    #set date begin date
    df = df[df['date'] >= '2018-01-01']

    df['year'] = df['date'].dt.year
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()

    #plot YoY chart 4-years
    fig = px.line(df, x="month_name", y="donations", color="year", hover_name='date',
             labels = {"month_name": "Month", "donations": "Donations", "year":"Year"},
             title = "Paraclete Mission Group - Monthly Donations"
             )
    st.plotly_chart(fig)

with dataset2:
    st.header('GF Balance : 3-Month Avg. Exp.')    