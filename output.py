import os

def output_to_folder(ticker, stock_data, arima, lstm, hybrid, plot_all, plot_arima, plot_lstm, plot_hybrid):
    #Create output directory
    path = "./output"
    output_folder_name = os.path.join(path, f"{ticker}_forecast")
    i = 1
    while os.path.exists(output_folder_name):
        output_folder_name = os.path.join(path, f"{ticker}_forecast_{i}")
        i += 1
    os.makedirs(output_folder_name)
    
    #Create plots directory
    plot_folder_name = os.path.join(output_folder_name, f"{ticker}_plots")
    while os.path.exists(plot_folder_name):
        plot_folder_name = os.path.join(path, f"{ticker}_plots_{i}")
        i += 1
    os.makedirs(plot_folder_name)
    
    #Save outputs to folder
    stock_data.to_csv(f'{output_folder_name}/{ticker}_raw_data.csv')
    arima.to_csv(f'{output_folder_name}/{ticker}_arima_forecast.csv')
    lstm.to_csv(f'{output_folder_name}/{ticker}_lstm_forecast.csv')
    hybrid.to_csv(f'{output_folder_name}/{ticker}_hybrid_forecast.csv')
    plot_all.savefig(f'{plot_folder_name}/{ticker}_forecast_plot_all.png')
    plot_arima.savefig(f'{plot_folder_name}/{ticker}_forecast_plot_arima.png')
    plot_lstm.savefig(f'{plot_folder_name}/{ticker}_forecast_plot_lstm.png')
    plot_hybrid.savefig(f'{plot_folder_name}/{ticker}_forecast_plot_hybrid.png')
    
    return output_folder_name

def test_output(avg_mse_arima, avg_mpe_arima, abs_avg_mpe_arima, bff_arima, avg_mse_lstm, avg_mpe_lstm, abs_avg_mpe_lstm, bff_lstm, avg_hybrid_ratio, avg_mse_hybrid, avg_mpe_hybrid, abs_avg_mpe_hybrid, bff_hybrid):
    #Create output directory
    path = "./output"
    output_folder_name = os.path.join(path, "test_output")
    i = 1
    while os.path.exists(output_folder_name):
        output_folder_name = os.path.join(path, f"test_output{i}")
        i += 1
    os.makedirs(output_folder_name)
    
    #Save output to folder
    with open(f'{output_folder_name}/test_output.txt', 'w') as file:
        print("ARIMA Model Fit:", file=file)
        print(f"Mean Squared Error (MSE): {avg_mse_arima}", file=file)
        print(f"Mean Percentage Error (MPE): {avg_mpe_arima}%", file=file)
        print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_arima}%", file=file)
        print(f"Best Fit Frequency: {bff_arima}%", file=file)
        print("\n", file=file)
        print("LSTM Model Fit:", file=file)
        print(f"Mean Squared Error (MSE): {avg_mse_lstm}", file=file)
        print(f"Mean Percentage Error (MPE): {avg_mpe_lstm}%", file=file)
        print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_lstm}%", file=file)
        print(f"Best Fit Frequency: {bff_lstm}%", file=file)
        print("\n", file=file)
        print("Hybrid Model Fit:", file=file)
        print(f"Average Weighted Average Ratio: {avg_hybrid_ratio} to ARIMA", file=file)
        print(f"Mean Squared Error (MSE): {avg_mse_hybrid}", file=file)
        print(f"Mean Percentage Error (MPE): {avg_mpe_hybrid}%", file=file)
        print(f"Absolute Mean Percentage Error (MPE): {abs_avg_mpe_hybrid}%", file=file)
        print(f"Best Fit Frequency: {bff_hybrid}%", file=file)
    return output_folder_name