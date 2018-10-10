# Location Entropy
File Information
----------------
### data/Nuclear power stations worldwide.csv:
  
  Download Link: https://fusiontables.google.com/DataSource?dsrcid=579353#rows:id=1
  
  These are the locations of Nuclear power stations worldwide.

### data/IN.zip:
  
  Unzip and extract the IN.csv file to the data folder after cloning the repository for the test case to work smoothly.
  
  Download Link: http://download.geonames.org/export/dump/
  
  This data is the location data for places of interest in India. The IN.zip file was downloaded from the link, extracted, column names were added and saved as a csv file. The IN.csv was zipped for upload.

### src/location_entropy.py

  Contains the main function for computing location entropy.

### src/test_case.py

  Contains the code to execute the location entropy function and test it on the two datasets. Entropies are calculated for all the columns of both the datasets, while the data1 (IN.csv) has remove_missing parameter (see below) set to False, data2 (Nuclear power stations worldwide.csv) has it set to True. Both data sets have numerical and string columns.
  
Function Details
--------
Computes entropy of a data series.

The function takes in a data series in the form of list or pandas series or numpy 1d array and computes the entropy.
All values are treated as categorical, even if they are continous numericals.

entropy = sum (-p(i)*log2(p(i))) for all i
where, p(i) is the probability of the value i or count of i / length of data series

### Parameters
data_series: list or numpy 1d array or pandas series
    
    The main data series

remove_missing: bool, optional default=True
    
    If True, removes all the missing values from data and proceeds to computing entropy
    If False, treats missing values (nan) as a separate class and computes entropy
    If not boolean, defaults to True

### Returns
  Entropy of the data series
