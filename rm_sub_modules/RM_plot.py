#import necessary modules
import csv
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def Return_series_plot ():
  Return_series = pd.read_csv('results/Return_series.csv',header=0,index_col=0)  
  return_fig=px.line(Return_series,x=Return_series.index,y=Return_series.columns,labels={"variable":"Assets"})
  #ra_fig=px.bar(returns_tab,x=returns_tab.index,y='Annualized_return',labels={"value":"Annualized_return","index":"assets"},text='Annualized_return')
  #ra_fig.update_traces(texttemplate='%{text:.2f%}%',textposition='outside')
  return_fig.update_layout(
  width=1000, height=500,
  xaxis_title="assets",
  paper_bgcolor="LightSteelBlue",
  yaxis_title="Daily return (%)",
  margin=dict(l=20, r=20, t=40, b=20),
  title="Daily Return Series : Cryptocurrencies ",
  xaxis_tickangle=-45,)
  return_fig.show()
  return
  
def Return_vol_plot():
  returns_tab = pd.read_csv('results/Return_Analysis.csv',header=0,index_col=0)
  volatility =  pd.read_csv('results/Volatility_Analysis.csv',header=0,index_col=0) 

  fig= go.Figure()
  fig.add_trace(go.Bar(
  x=returns_tab.index,
  y=returns_tab.Annualized_return,
  name="Annualized_return",
  text=returns_tab.Annualized_return,
  marker_color="green"
  ))
  fig.add_trace(go.Bar(
  x=volatility.index,
  y=volatility.annualized_volatility,
  text=volatility.annualized_volatility,
  name="Annualized_vol",
  marker_color="red"
  ))

  fig.update_traces(texttemplate='%{text:.2f%} (%)',textposition='outside')
  fig.update_layout(
  width=800, height=500,
  xaxis_title="assets",
  paper_bgcolor="LightSteelBlue",
  yaxis_title="Annualized Return & Volatility (%)",
  margin=dict(l=20, r=20, t=40, b=20),
  barmode='group',
  title="Risk-Return measures : Cryptocurrencies ",
  xaxis_tickangle=-45,
  )
  fig.show()

  return 


def Sharpe_Ratio():
  
  Sharpe_Ratio = pd.read_csv('results/Sharpe_Ratio.csv',header=0,index_col=0)
  fig= go.Figure()
  fig.add_trace(go.Bar(
  x=Sharpe_Ratio.index,
  y=Sharpe_Ratio.Sharpe_Ratio,
  text=Sharpe_Ratio.Sharpe_Ratio,
  name="Sharpe_Ratio",
  
    marker_color="green"
  ))

  fig.update_traces(texttemplate='%{text:.2f%} (rf=.03)',textposition='outside')
  fig.update_layout(
  width=800, height=500,
  xaxis_title="assets",
  paper_bgcolor="LightSteelBlue",
  yaxis_title="Sharpe_Ratio",
  margin=dict(l=20, r=20, t=40, b=20),
  barmode='group',
  title="Risk-Return measures : Sharpe_Ratio  ",
  xaxis_tickangle=-45,
  )
  fig.show()




  return 

