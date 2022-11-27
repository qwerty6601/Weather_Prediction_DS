# Weather_Prediction_DS
We built neural networks to forecast the min, max, mean temperature of Budapest based on different timeframes

26.11.2022 (Erzsébet)
Firstly, I scaled the whole dataset and saved the respective .csv files using Sarah's scripts to a folder named 'preprocessed'. File names contain how many days we examine, what features we use and which temperature we want to predict (e.g. 3daysprev_onlytempfeatures_Min_temp.csv has the scaled data from 3 previous days, target is min temp and uses only temperature features for prediction). See Data_Processing_preproc_to_csv.ipynb for details


Also I wrote a simple script for running and comparing models using crossvalidation. I included linreg, Random Forest and Multilayer Perceptron, but feel free to add other models and use my code to help automatize tasks. With the code in Modeling.ipynb you could easily iterate through every possible combination of days, targets features and models to test and later evaluate the results.

28.11.2022 (Gábor)
I modified the existing code for Modeling and generated all data to a csv file under output folder.
