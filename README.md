# FinnForecast
Hello! Thanks for checking out my project. 

This purpose of this program is to forecast stock prices using a combination of traditional time-series forecasting methods and AI.
I used a weighted average hybrid model to combine these methods. 

To run this program, first run the two following commands in the command prompt.
source venv/bin/activate
pip install -r requirements.txt

This will install all the libraries necessary for this program. 

Next you can run main.py to start the program. It should (hopefully) be pretty robust, and should't crash from user input. 
You have 4 modes to choose from, the first two actually make forecasts, the second two will runn tests of the accuracy of the models.

Depending on you knowledge of AI and Long Short-Term memory models, there are two modes for both forecasting and testin:
Simple:
Runs a forecast/test using default parameters for the LSTM forecast.

Advanced:
Allows you to choose LSTM parameters such as sequence length, batch size, # of epochs, etc.

I think I've covered everything you need to use this program, so have fun!.
