import fetchStockData as fsd

def check_cancel(var1=0, var2=0, var3=0, var4=0, var5=0, var6=0, var7=0):
    try:
        if var1 == "cancel" or var2 == "cancel" or var3 == "cancel" or var4 == "cancel" or var5 == "cancel" or var6 == "cancel" or var7 == "cancel":
            return True
        else:
            return False
    except ValueError:
        return False
    
def get_simple_params():
    valid_input = False
    while valid_input == False:
        # Ticker Selection
        ticker = input("Please enter the stock ticker you want to forecast: ")
        try:
            if ticker.lower() == "cancel":
                ticker="cancel"
                stock_data="cancel"
                forecast_length="cancel"
                return ticker, stock_data, forecast_length
        except ValueError:
            valid_input = valid_input
                            
        # Fetch and Clean Data
        stock_data = fsd.fetch_and_clean(ticker)
        if stock_data.empty:
            print(f"[Error]: Ticker symbol '{ticker}' not found or invalid.")
        else:
            valid_input = True
    max_forecast_len = stock_data.shape[0]/2

    # Get forecast length and forecast
    valid_input = False
    while valid_input == False:
        forecast_length = input(f"How long (in months) do you want to forecast {ticker}: ")
        try:
            if forecast_length.lower() == "cancel":
                ticker="cancel"
                stock_data="cancel"
                forecast_length="cancel"
                return ticker, stock_data, forecast_length
        except ValueError:
            valid_input = valid_input
        try:
            forecast_length = int(forecast_length)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if forecast_length > max_forecast_len:
            print(f"[Error]: Not enough stock data for chosen forecast length. Please choose a forecast length between 0 and {max_forecast_len}.")
        elif forecast_length <= 0:
            print(f"[Error]: Invalid Input. Please choose a forecast length between 0 and {max_forecast_len}.")
        else:
            valid_input = True
            
    return ticker, stock_data, forecast_length

def get_advanced_params(stock_data):
    valid_input = False
    while valid_input == False:
        sequence_length = input("Please enter a sequence length: ")
        try:
            if sequence_length.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            sequence_length = int(sequence_length)
        except ValueError:
            print(f"[Error]: Invalid input. Please choose a sequence length between 0 and {max_sequence_len}.")
            continue
        max_sequence_len = stock_data.shape[0]
        if sequence_length > max_sequence_len:
            print(f"[Error]: Not enough stock data for chosen sequence length. Please choose a sequence length between 0 and {max_sequence_len}.")
        elif sequence_length <= 0:
            print(f"[Error]: Invlaid input. Please choose a sequence length between 0 and {max_sequence_len}.")
        else:
            valid_input = True                    
    valid_input = False
    while valid_input == False:
        batch_size = input("Please enter a batch size: ")
        try:
            if batch_size.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            batch_size = int(batch_size)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if batch_size <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
                
    valid_input = False
    while valid_input == False:
        epochs = input("Please enter an amount of epochs: ")
        try:
            if epochs.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            epochs = int(epochs)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if epochs <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
                        
    valid_input = False
    while valid_input == False:
                
        step = input("Please enter a weighted average step size: ")
        try:
            if step.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            step = int(step)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if step <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
    return sequence_length, batch_size, epochs, step

def get_simple_test_params():
    # Get forecast length and forecast
    valid_input = False
    while valid_input == False:
        forecast_length = input(f"How long (in months) do you want to forecast for this test?: ")
        try:
            if forecast_length.lower() == "cancel":
                forecast_length="cancel"
                test_range="cancel"
                return forecast_length, test_range
        except ValueError:
            valid_input = valid_input
        try:
            forecast_length = int(forecast_length)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if forecast_length <= 0:
            print(f"[Error]: Invalid Input. Please choose a forecast length greater than 0.")
        else:
            valid_input = True
            
    valid_input = False
    while valid_input == False:
                
        test_range = input("How many stocks would you like to test?: ")
        try:
            if test_range.lower() == "cancel":
                forecast_length="cancel"
                test_range="cancel"
                return forecast_length, test_range
        except ValueError:
            valid_input = valid_input
        try:
            test_range = int(test_range)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number between 0 and 50000.")
            continue
        if test_range <= 0 or test_range >= 50000:
            print("[Error]: Invlaid input. Please enter a number between 0 and 50000.")
        else:
            valid_input = True
    return forecast_length, test_range

def get_advanced_test_params():
    valid_input = False
    while valid_input == False:
        sequence_length = input("Please enter a sequence length: ")
        try:
            if sequence_length.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            sequence_length = int(sequence_length)
        except ValueError:
            print(f"[Error]: Invalid input. Please choose a sequence length greater than 0.")
            continue
        if sequence_length <= 0:
            print(f"[Error]: Invlaid input. Please choose a sequence length greater than 0.")
        else:
            valid_input = True                    
    valid_input = False
    while valid_input == False:
        batch_size = input("Please enter a batch size: ")
        try:
            if batch_size.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            batch_size = int(batch_size)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if batch_size <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
                
    valid_input = False
    while valid_input == False:
        epochs = input("Please enter an amount of epochs: ")
        try:
            if epochs.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            epochs = int(epochs)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if epochs <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
                        
    valid_input = False
    while valid_input == False:
                
        step = input("Please enter a weighted average step size: ")
        try:
            if step.lower() == "cancel":
                sequence_length="cancel"
                batch_size="cancel"
                epochs="cancel"
                step="cancel"
                return sequence_length, batch_size, epochs, step
        except ValueError:
            valid_input = valid_input
        try:
            step = int(step)
        except ValueError:
            print("[Error]: Invalid input. Please enter a number.")
            continue
        if step <= 0:
            print("[Error]: Invlaid input. Please enter a number greater than 0.")
        else:
            valid_input = True
    return sequence_length, batch_size, epochs, step
