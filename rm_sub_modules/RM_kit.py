import pandas as pd 
import numpy as np
from pandas.core.arrays import boolean
import yfinance as yf


def import_data (start_date,end_date,*Ticker) :
    """
    Get prices from https://finance.yahoo.com/ 

    start : the start date 
    end : the end date 
    ticker* : list of tickers to work on...

    The function returns the price dataframe of all tickers passed as params 
    
    """

    Ticker_prices = pd.DataFrame()
    data_Ticker1 = yf.Ticker(Ticker[0]).history(start=start_date,end=end_date)[['Close']]
    data_Tiker2 = yf.Ticker(Ticker[1]).history(start=start_date,end=end_date)[['Close']]
    data_Tiker3 = yf.Ticker(Ticker[2]).history(start=start_date,end=end_date)[['Close']]
    Ticker_prices = pd.merge(data_Ticker1, data_Tiker2, on='Date',)
    Ticker_prices = pd.merge(Ticker_prices, data_Tiker3, on='Date')

    Ticker_prices.columns = Ticker

    return pd.DataFrame (Ticker_prices)


def get_return (data : pd.DataFrame()) :
    
    """
    Data : closed prices - dataframe 
    output : return series

    """
    returns = data.pct_change()
    returns = returns.dropna() # delete NAN values (first row)
    #returns = returns.resample('1M').mean()
    

    return pd.DataFrame (returns)
 


    
def get_volatility (returns: pd.DataFrame()):

    """
    Input : return series
    Output : volatilty & annualized_volatility
    """
    nb_obs = returns.shape[0]
    deviations = returns - returns.mean()
    sq_deviations = deviations**2
    #variance = sq_deviations.mean() - didn't work because it devides by n = number of observations, we need n - 1
    variance = sq_deviations.sum()/(nb_obs - 1)
    volatility = np.sqrt(variance)
    annualized_volatility = (volatility*np.sqrt(252)) #252 Trading days
    # tested with the predifined function .std()
    return pd.DataFrame ({"volatility" : volatility, "annualized_volatility" : annualized_volatility})




def return_analysis (returns: pd.DataFrame()) :

    """
    Input : return serie 
    OutPut : total return over all the given period | return per period (Day - month - year) | excess return . for all assets.
        
    """

    Total_return = (returns+1).prod() #total return over the given period 
    n_months = returns.shape[0]
    return_per_month = (returns +1).prod()**(1/n_months) -1
    #Annualized_return = (returns+1).prod()**(252/n_days) -1
    Annualized_return = (return_per_month+1)**254 -1 
    #rf : risk free rate value (just an exemple 0.03) 
    excess_return = Annualized_return - 0.03
    return pd.DataFrame ({"total_return" : Total_return,"return_per_day" : return_per_month,"Annualized_return" : Annualized_return, "excess_return ( rf = 0.03)" : excess_return})

def get_sharpe_ratio(returns_tab:pd.DataFrame,volatility:pd.DataFrame) :

    Sharpe_Ratio = returns_tab["excess_return ( rf = 0.03)"]/volatility["annualized_volatility"]

    return pd.DataFrame({"Sharpe_Ratio" :Sharpe_Ratio })



