from ioprocessing import fetchStockData as fsd, output
from forecast.models import arima, lstm, hybrid
import pandas as pd

def calculate_averages(mse_list, mpe_list):
        avg_mse = sum(mse_list) / len(mse_list)
        avg_mpe = sum(mpe_list) / len(mpe_list)
        abs_avg_mpe = sum([abs(mpe) for mpe in mpe_list]) / len(mpe_list)
        return avg_mse, avg_mpe, abs_avg_mpe

def average(list):
    avg = sum(list)/len(list)
    return avg

def average_measure_fits(forecast_length, test_range, sequence_length=12, batch_size=64, epochs=75, step=100):
    
    # Initalize Fit Lists
    mses_arima = []
    mses_lstm = []
    mses_hybrid = []
    
    mpes_arima = []
    mpes_lstm = []
    mpes_hybrid = []
    
    bffs_arima = []
    bffs_lstm = []
    bffs_hybrid = []
    
    hybrid_ratios = []

    # Import data, Select Ticker column
    yfin_stocks = pd.read_csv('stockTickers.csv')
    tickers = yfin_stocks['Ticker']
    
    # Iterate through test range in tickers, record measures for fit for each model
    index = 0
    for ticker in tickers.iloc:
        if (
            len(mses_arima) >= test_range and 
            len(mses_lstm) >= test_range and 
            len(mses_hybrid) >= test_range and 
            len(mpes_arima) >= test_range and 
            len(mpes_lstm) >= test_range and 
            len(mpes_hybrid) >= test_range and
            (len(bffs_arima)+len(bffs_lstm)+len(bffs_hybrid)) >= test_range
        ): break
        
        # Fetch stock ticker data
        stock_data = fsd.fetch_and_clean(ticker)
        if stock_data.empty:
            print(f"Deleting {ticker}...")
            fsd.delete_record(yfin_stocks, 'Ticker', ticker, 'stockTickers.csv')
            continue
        elif stock_data.shape[0] <= forecast_length*2:
            print(f"[Warning!]: {ticker} data too short for forecast. Skipping {ticker}...")
            continue
        
        # Split into training and testing data & construct ARIMA forecast
        train, test = arima.split_training_data(stock_data, forecast_length)
        arima_forecast = arima.arima_forecast(train, forecast_length)
        if (arima_forecast['Forecast'].isna().any()):
            fsd.delete_record(yfin_stocks, 'Ticker', ticker, 'stockTickers.csv')
            continue
        print(f"[{ticker}]: ARIMA Forecast complete...")

        # Constuct LSTM Forecast
        lstm_forecast = lstm.lstm_model_fit(train, forecast_length, sequence_length, batch_size, epochs)
        if lstm_forecast is None:
            fsd.delete_record(yfin_stocks, 'Ticker', ticker, 'stockTickers.csv')
            continue
        print(f"[{ticker}]: LSTM Forecast complete...")


        #Calculate minimzed mpe Hybrid Forecast
        hybrid_forecast, hybrid_ratio = hybrid.wa_hybrid_model_test(arima_forecast, lstm_forecast, test, step)
        
        #Calculate and validate Measures of fit
        mse_arima, mpe_arima = arima.test_fit(arima_forecast['Forecast'], test)
        mse_lstm, mpe_lstm = arima.test_fit(lstm_forecast, test)
        mse_hybrid, mpe_hybrid = arima.test_fit(hybrid_forecast, test)
        
        if (
            mse_arima is not None and 
            mpe_arima is not None and 
            mse_lstm is not None and 
            mpe_lstm is not None and 
            mse_hybrid is not None and 
            mpe_hybrid is not None
        ):
            if (abs(mpe_arima) < abs(mpe_lstm) and abs(mpe_arima) <= abs(mpe_hybrid)):
                bffs_arima.append(mpe_arima)
            elif (abs(mpe_lstm) < abs(mpe_arima) and abs(mpe_lstm) <= abs(mpe_hybrid)):
                bffs_lstm.append(mpe_lstm)
            elif (abs(mpe_hybrid) < abs(mpe_arima) and abs(mpe_hybrid) < abs(mpe_lstm)):
                bffs_hybrid.append(mpe_hybrid)
            else:
                print("Best Fit Frequency Error: Something went wrong!")
                fsd.delete_record(yfin_stocks, 'Ticker', ticker, 'stockTickers.csv')
                continue
            
            mses_arima.append(mse_arima)
            mpes_arima.append(mpe_arima)
            mses_lstm.append(mse_lstm)
            mpes_lstm.append(mpe_lstm)
            mses_hybrid.append(mse_hybrid)
            mpes_hybrid.append(mpe_hybrid)
            hybrid_ratios.append(hybrid_ratio)
            
        else:
            fsd.delete_record(yfin_stocks, 'Ticker', ticker, 'stockTickers.csv')
            continue

        # Iterate
        index += 1
        print(f"[{ticker}]: {index} Stocks Calculated...")
        
    #Calculate average fits for each model
    avg_mse_arima, avg_mpe_arima, abs_avg_mpe_arima = calculate_averages(mses_arima, mpes_arima)
    avg_mse_lstm, avg_mpe_lstm, abs_avg_mpe_lstm = calculate_averages(mses_lstm, mpes_lstm)
    avg_mse_hybrid, avg_mpe_hybrid, abs_avg_mpe_hybrid = calculate_averages(mses_hybrid, mpes_hybrid)
    
    avg_hybrid_ratio = average(hybrid_ratios)
    
    bff_arima = (len(bffs_arima)/(len(bffs_arima)+len(bffs_lstm)+len(bffs_hybrid))) * 100
    bff_lstm = (len(bffs_lstm)/(len(bffs_arima)+len(bffs_lstm)+len(bffs_hybrid))) * 100
    bff_hybrid = (len(bffs_hybrid)/(len(bffs_arima)+len(bffs_lstm)+len(bffs_hybrid))) * 100
    
    #print to file
    path = output.test_output(avg_mse_arima, avg_mpe_arima, abs_avg_mpe_arima, bff_arima, avg_mse_lstm, avg_mpe_lstm, abs_avg_mpe_lstm, bff_lstm, avg_hybrid_ratio, avg_mse_hybrid, avg_mpe_hybrid, abs_avg_mpe_hybrid, bff_hybrid)

    print(f'[Complete!]: Output printed to {path}')

    # print("\n")
    # print(f"{forecast_length}-Stock Fit Test Summary:")
    # print("ARIMA Model Fit:")
    # print(f"Mean Squared Error (MSE): {avg_mse_arima}")
    # print(f"Mean Percentage Error (MPE): {avg_mpe_arima}%")
    # print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_arima}%")
    # print(f"Best Fit Frequency: {bff_arima}%")
    
    # print("\n")
    # print("LSTM Model Fit:")
    # print(f"Mean Squared Error (MSE): {avg_mse_lstm}")
    # print(f"Mean Percentage Error (MPE): {avg_mpe_lstm}%")
    # print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_lstm}%")
    # print(f"Best Fit Frequency: {bff_lstm}%")
    # print("\n")
    # print("Hybrid Model Fit:")
    # print(f"Average Weighted Average Ratio: {avg_hybrid_ratio} to ARIMA")
    # print(f"Mean Squared Error (MSE): {avg_mse_hybrid}")
    # print(f"Mean Percentage Error (MPE): {avg_mpe_hybrid}%")
    # print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_hybrid}%")
    # print(f"Best Fit Frequency: {bff_hybrid}%")
    # print("\n")
    
