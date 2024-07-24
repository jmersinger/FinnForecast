# FinnForecast :money_with_wings:
<h2>Hello! :wave:</h2>
<h3>Thanks for checking out my project. </h3>

FinnForecast is a comprehensive stock forecasting tool developed as a final project for my Intro to Python class. This program integrates traditional time-series modeling with a recurrent neural network, with the goal of creating a more accurate model for forecasting stock prices. 

## :book: Table of Contents
1. [Project Overview](#computer-project-overview)
2. [Installation](#wrench-installation)
3. [Usage](#man_technologist-usage)
4. [Files and Directories](#file_folder-files-and-directories)
5. [How It Works](#memo-how-it-works)
6. [Results](#chart_with_upwards_trend-results)
7. [Languages, Frameworks, and Tools](computer-languages-frameworks-and-tools)

## :computer: Project Overview

FinnForecast leverages statistical and machine-learning techniques to forecast stock market behavior. The program is designed to be simple to use and robust to user error, allowing users to select between creating a forecast or running a test of the program's accuracy. For both of the options, the user is also able to select between a simple mode or advanced mode, with simple mode using default parameters for the models, and the advanced mode allowing the user more control over the performance and accuracy of the models. 
The model uses an Autoregressive Integrated Moving Average (ARIMA) model for the traditional forecast and a Long Short-Term Memory neural network for the machine learning forecast. To Integrate these models with each other, FinnForecast utilizes a dynamic weighted average, finding the optimal weights by creating sample models and forecasts from a section of the training data and using the weights that result in the smallest Absolute Mean Percent Error (aMPE) between the sample forecast and the actually values.

## :wrench: Installation

To set up the FinnForecast project on your local machine, follow these steps:

1. <b>Download the Project Files:</b>
   - Ensure you have received the project files. You can download them from the provided link or source.

2. <b>Extract the Files:</b>
   - If the project files are in a zip archive, extract them to your desired directory.

3. <b>Navigate to the Project Directory:</b>
   - Open your terminal or command prompt and navigate to the directory where you extracted the project files.
   ```bash
   cd path/to/FinnForecast
4. <b>Ensure You have the Necessary Libraries Installed</b>
   - This program uses the following libraries:
      - pmdarima
      - scikit-learn
      - pandas
      - numpy
      - tensorflow
      - yfinance
      - matplotlib
      - seaborn
   - Use the following command to install the libraries:
   ```bash
   pip install [library_name]

## :man_technologist: Usage
1. Run the Main Program:
   - Execute the 'main.py' file to begin running the program
   ```bash
   python main.py
2. Select a Mode:
   - The program gives the user 4 modes to select from.
   ```bash
   Hello! Welcome to FinnForecast! 
   =============Menu==============
   (1) Create a simple forecast
   (2) Create an advanced forecast
   (3) Run a simple test
   (4) Run an advanced test
   (5) Quit
   ===============================
   Please select an option (1-5): 
   ```
   - Modes (1) and (2) allow the user to input a stock ticker and forecast length (in months) and output the raw stock data, the ARIMA, LSTM, and Hybrid forecasts, and plots of each forecast
   - Modes (3) and (4) allow the user to test the accuracy of the forecasts by inputting a forecast length as well as selecting the amount of stock they wish to test with. The program then runs a test forecast of a slice from the end of the stock data equal to the forecast length. The program compares the test forecast to the actual values and outputs the results of the test in a file <i>test_output.txt</i>
   - To run a test on a specific set of stock tickers, simply paste a .csv containing the tickers in the root folder, and rename it 'stockTickers.csv'. Then, run a test through main.py as normal. The default stockTickers.csv file contains tickers for the stock components of the S&P 500 Index. 
   - The difference between the simple and advanced modes is that the simple mode runs the forecast with default LSTM and Hybrid parameters. The advanced mode allows the user to enter parameters for the LSTM and Hybrid model, including sequence_length, batch_size, epochs, and step.
  
## :file_folder: Files and Directories
The file structure of FinnForecast is as follows:

FinnForecast/<br>
├── data/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── get_top_stocks.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── russel1000_tickers.csv<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── sp500_tickers.csv<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Yahoo Ticker Symbols - September 2017.xlsx<br>
├── forecast/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── forecast.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── models/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── arima.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── lstm.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── hybrid.py<br>
├── ioprocessing/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── fetchStockData.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── plot.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── output.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── params.py<br>
├── tests/<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── testAvgMPE.py<br>
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── stockTickers.csv/<br>
├── output/<br>
├── venv/<br>
├── .git/<br>
├── __pycache__/<br>
├── README.md<br>
├── requirements.txt<br>
├── main.py<br>

## :memo: How It Works
<h3>Fetching, Preprocessing, and Cleaning the Data: fetchStockData.py</h3>
This program utilizes Yahoo Finance's <b>yfinance</b> library for making API calls to download stock data. When the user enters a stock ticker for the forecast, the program downloads the monthly stock data for the appropriate ticker. For cleaning and preprocessing, the program drops null values and converts the index to datetime using the <b>pandas</b> library. 

<h3>Traditional Time Series Modeling (ARIMA): arima.py</h3>
The traditional statistical time series model in this program is the Autoregressive Integrated Moving Average (ARIMA) model. The ARIMA model is used in field such as economics and finance for modeling and forecasting time series trends. It consists of three different components:
<h4>The Autoregressive (AR) Component</h4>
In an AR model, the current value of the series is expressed as a linear combination of its previous values. This assumes that past values have a direct impact on the present value. in other words, the series is regressed on its prior values, from the immediate prior value, <i>Y<sub>t-1</sub></i>, up to a set lag, <i>p</i>, for <i>Y<sub>t-p</sub></i>. For example, an Autoregressive Model with a lag <i>p</i> = 2, AR(2), of variable Y, would look like this:
<p></p>
<p align="center"><i>Y<sub>t</sub> = c + ϕ<sub>1</sub>Y<sub>t-1</sub> + ϕ<sub>2</sub>Y<sub>t-2</sub></i></p>
<p></p>
<h4>The Integrated (I) Component</h4>
A crucial property needed for data to be modeled in and ARIMA model is stationarity. When a series is stationary, properties such as mean and variance are constant over time. Modeling with non-stationary data can result in unreliable forecasts. The Integrated component of the ARIMA model addresses this issue with differencing. Differencing essentially subtracting the latest observation by the next latest. The Integrated component selects the order of differencing needed to achieve stationarity in the data. Here is an example of what a first and second-order differenced series, for series <i>Y</i>:
<p></p>
<p align="center">First order differencing (I = 1): <i>ΔY<sub>t</sub> = Y<sub>t</sub> - Y<sub>t-1</sub></i></p>
<p></p>
<p align="center">Second order differencing (I = 2): <i>Δ<sup>2</sup>Y<sub>t</sub> = Δ(ΔY<sub>t</sub>) = Y<sub>t</sub> - 2Y<sub>t-1</sub> + Y<sub>t-2</sub></i></p>
<p></p>
<h4>The Moving Average (MA) Component</h4>
The MA component models the relationship between the current observation and the error terms (residuals) of the model. This essentially corrects the model on potential short-term forecast errors. For example, if the model overestimates (the forecast is too high), the residual will be negative, and the MA component will adjust the forecast downward to correct the error. The parameter of the MA model, <i>q</i> represents the number of past residuals the MA component accounts for, where:
<p></p>
<p align="center">For residual, <i>ϵ</i>: <i>ϵ<sub>t</sub> = Y<sub>t</sub> - Y&#770;<sub>t</sub></i></p>
<p></p>
<p align="center">Second order MA model (MA(2)): <i>Y<sub>t</sub> = μ + (ϵ<sub>t</sub>) + θ<sub>1</sub>ϵ<sub>t-1</sub> + θ<sub>2</sub>ϵ<sub>t-2</sub></i></p>
<p></p>
<h4>arima.py</h4>
The arima.py file contains several function for use in the ARIMA model and other programs. The main use of this file is to pass stock data and a forecast length into it to get an ARIMA forecast for use in the hybrid model. This ARIMA forecast is achieved using the <i>pmdarima</i> library, specifically the auto_arima function, which automatically selects the best parameters for the AR lags, differencing, and the MA lags. 

<h3>Long Short-Term Memory (LSTM) Model: lstm.py</h3>
Long Short-Term Memory is a type of Recurrent Neural Network (RNN) that is particularly suited for sequences of data, especially where the model needs to remember information for extended periods, such as Time-Series data, among other subjects. For the sake of simplicity, I will not explain the full theory and mathematics behind LSTMs, but if you are interested in learning more, please check out the following links:
Wikipedia: https://en.wikipedia.org/wiki/Long_short-term_memory<br>
Machine Learning Mastery: https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks-experts/<br>
Towards Data Science: https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21<br>

<h3>The Hybrid Model: hybrid.py</h3>
The hybrid model in FinnForecast utilizes a weighted average approach toward integrating the ARIMA forecast with the LSTM forecast. In other words, the forecasts are combined with the following formula:
<p></p>
<p align="center">Let: <i>H = Hybrid Forecast,<br> A = ARIMA Forecast,<br> L = LSTM Forecast,<br> 0 <= x <= 1,<br> 0<= y <= 1, and<br> x + y = 1</i></p>
<p></p>
<p align="center">Weighted Average Model: <i>H = (x * A) + (y * L)</i></p>
<p></p>
<h4>Hybrid Weights</h4>
To select the hybrid weights, x and y, the model iterates through possible values from 0 to 1 for x and y, ensuring x + y = 1. The model then selects the optimal hybrid weight by the weight with the lowest Absolute Mean Percent Error, (aMPE), where, for forecast length <i>f</i>:
<p></p>
<p align="center"><i>aMPE = | (Σ(Y - Y&#770;) / Y)) / f |</i></p>
<p></p>
To find the actual values <i>Y</i> for the forecast, the model runs a test forecast. Essentially, the stock data is split into two series, <i>train</i> and <i>test</i>, where <i>train</i> represents the values used to train the test forecasts, and <i>test</i> represents the values for <i>Y</i> when calculating aMPE. The model then iterates through the weighted average formula for the test ARIMA and LSTM forecasts, checking the aMPE for each weight. The model then selects the weights with the smallest aMPE and applies them to the real forecast for a final Hybrid Forecast. 

<h3>Model Testing: testAvgMPE.py</h3>
FinnForecast also features the option to run a test of the model. For the model test, the program runs through a .csv of stocks, located in the root, 'stockTickers.csv', creating test forecasts and calculating the aMPE of each stock. These test forecasts are similar to the test forecasts used to calculate the optimal hybrid weights. After running through all the stocks the user selected, from stockTickers.csv, the program fins the average aMPE across all forecasts of the ARIMA, LSTM, and Hybrid models. The program also finds the frequency that each model had the lowest aMPE for each stock.<br>
It should be noted that the Hybrid model is designed to always return the weights with the lowest aMPE among ARIMA, LSTM, and Hybrid (represented in weights of 0 or 1 if ARIMA or LSTM return the lowest aMPE). The model test accounts for this by marking ARIMA or LSTM as the best forecast in the case that the Hybrid model has greater than or equal aMPE. 


## :chart_with_upwards_trend: Results
As a final test of the model, I ran simple, 36-month tests of all the stock components of the S&P 500 index and the Russel 1000 index. Here are the results:


## :computer: Languages, Frameworks, and Tools
<div>
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/tensorflow/tensorflow-original.svg" title="TensorFlow" alt="TensorFlow" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/keras/keras-original.svg" title="Keras" alt="Keras" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" title="Pandas" alt="Pandas" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/scikitlearn/scikitlearn-original.svg" title="Scikit-Learn" alt="Scikit-Learn" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg" title="Matplotlib" alt="Matplotlib" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/numpy/numpy-original.svg" title="Numpy" alt="Numpy" width="40" height="40"/>&nbsp;
    <img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" title="VSCode" alt="VSCode" width="40" height="40"/>&nbsp;
</div>

