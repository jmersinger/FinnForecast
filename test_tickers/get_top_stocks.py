import pandas as pd

def fetch_wikipedia_tickers(url, table_index):
    tables = pd.read_html(url, header=0)
    tickers_df = tables[table_index]
    return tickers_df['Symbol'].tolist()

def save_tickers_to_csv(tickers, filename):
    df = pd.DataFrame(tickers, columns=['Ticker'])
    df.to_csv(filename, index=False)
    print(f'{filename} saved successfully!')
    
# Fetching S&P 500 tickers
sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_tickers = fetch_wikipedia_tickers(sp500_url, 0)
save_tickers_to_csv(sp500_tickers, 'sp500_tickers.csv')

# Fetching Russell 1000 tickers
russell1000_url = 'https://en.wikipedia.org/wiki/Russell_1000_Index'
russell1000_tickers = fetch_wikipedia_tickers(russell1000_url, 2)
save_tickers_to_csv(russell1000_tickers, 'russell1000_tickers.csv')

