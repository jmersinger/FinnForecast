import params
import testAvgMPE as test
import forecast


def main():
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print("Hello! Welcome to FinnForecast! ")
    
    end = False
    while end == False:
        
        ###Main Menu###
        end = "Invalid"
        print("=============Menu==============")
        print("(1) Create a simple forecast")
        print("(2) Create an advanced forecast")
        print("(3) Run a simple test")
        print("(4) Run an advanced test")
        print("(5) Quit")
        print("===============================")
        valid_input = False
        while valid_input == False:
            mode = input("Please select an option (1-5): ")
            try:
                mode = int(mode)
            except ValueError:
                print("[Error]: Invalid input. Please enter a number 1-5.")
                continue   
            
            ###Simple Forecast###
            if mode == 1:
                print("Okay, lets make a simple forecast.")
                print("If you change your mind, just enter 'cancel' at any time to return to the menu.")
                ticker, stock_data, forecast_length = params.get_simple_params()
                if params.check_cancel(ticker, stock_data, forecast_length): 
                    valid_input=True
                    end=False
                    continue
                forecast.forecast(ticker, stock_data, forecast_length)
                
            ###Advanced Forecast###
            elif mode == 2:            
                print("Okay, lets make an advanced forecast.")
                print("If you change your mind, just enter 'cancel' at any time to return to the menu.")
                ticker, stock_data, forecast_length = params.get_simple_params()
                if params.check_cancel(ticker, stock_data, forecast_length): 
                    valid_input=True
                    end=False
                    continue
                sequence_length, batch_size, epochs, step = params.get_advanced_params(stock_data)
                if params.check_cancel(sequence_length, batch_size, epochs, step): 
                    valid_input=True
                    end=False
                    continue
                forecast.forecast(ticker, stock_data, forecast_length, sequence_length, batch_size, epochs, step)
                
            ###Simple Test###
            elif mode == 3:
                print("Okay, lets run a simple test.")
                print("If you change your mind, just enter 'cancel' at any time to return to the menu.")
                forecast_length, test_range = params.get_simple_test_params()
                if params.check_cancel(forecast_length, test_range): 
                    valid_input=True
                    end=False
                    continue
                test.average_measure_fits(forecast_length, test_range)
                
            ###Advanced Test###
            elif mode == 4:
                print("Okay, lets run a simple test.")
                print("If you change your mind, just enter 'cancel' at any time to return to the menu.")
                forecast_length, test_range = params.get_simple_test_params()
                if params.check_cancel(forecast_length, test_range): 
                    valid_input=True
                    end=False
                    continue
                sequence_length, batch_size, epochs, step = params.get_advanced_test_params()
                if params.check_cancel(sequence_length, batch_size, epochs, step): 
                    valid_input=True
                    end=False
                    continue
                test.average_measure_fits(forecast_length, test_range, sequence_length, batch_size, epochs, step)
                
            elif mode == 5:
                quit()
                
            else:
                print("[Error]: Invaild selection. Please select and option (1-5).")
                continue
            valid_input = True

        while end == "Invalid":
            end = input("Would you like to return to the menu? (Y/N): ").upper()
            if end == "Y":
                end = False
            elif end == "N":
                end = True
            else:
                print('[Error]: Invalid input. Please enter "Y" or "N".')
                end = "Invalid"

    

if __name__ == "__main__":
    main()