## **Toronto Climate Data With Shell Script**

In this project, we will use a shell script to run commands that will pull information in csv format from an internet data source, concatenate the data using python libraries and produce a log for any error and for our process in general. 


### **Requirements/Instructions for the Project**

- Download data from Canadian Climate

- We only need the data of **Station ID = 48549**

- The year range of the data we want is from 2020 to 2022.

- We only want the data in February

- Concatenate the downloaded files into one final csv file, called *all_years.csv*. This is the output of the project.

- Upload scripts and final csv file to a repository in GitHub.


### **Getting Started**

To get started, create a general folder for your project using `mkdir`. Within that folder create four additional folders:

+ ***INPUT_FOLDER*** :  This will hold all downloaded csv files 

+ ***OUTPUT_FOLDER***: THis will hold the final concatenated file

+ ***LOG_FOLDER*** : This will hold all your logs

+ ***SCRIPT_FOLDER***: This will hold your script files, in this case the `python_script.py` file and `shell_script.sh` file. 

### **Python Script**

Our python script is going to hold the commands to grab the downloaded csv files from our input folder, concatenate the files and save it as a single file name **all_year.csv** in our output folder.

Some of the libraries we will use to achieve this goal include `glob`, `pandas` and `os`.

***Glob*** is used to return all file paths that match a specific pattern. You use it to search for files where the filename matches a certain pattern by using wild card characters. The wild card characters are:

+ ***Asterisks*** (*) is used to match zero or more characters.

+ ***Question Mark*** (?) is used to match exactly one character.

In our case, we want to find all the csv in the input folder (`/*.csv`).

***Pandas***  is a fast , flexible and easy to use open source tool used for data analysis, data manipulation and machine learning tasks. 

***OS*** is a module in Python that provides functions for interacting with the operating system,  creating and removing a directory, and getting its content.

#### **Things to note in our python script**

All our files have the same column so we use append.
Set header = 0 so your system can read the csv files and assign the first row as column names.
Set index_col = None to indicate that you are not setting columns or unique ids for the dataframe.

Set ignore_index = True to ignore index when you concatenate.


### **Shell Script** 

We will be using bash scripting, so you need to start your file with:

    #!/bin/bash

The next step is to set your variables which means providing the paths to your folders. The first command would be to tell your system to go into your scripts folder `cd ${SCRIPTS_FOLDER}`.

The program is then given the command to download the data, move to our python script to run the code and if successful print ***PROGRAM SUCCEEDED** if not print ***PYTHON RUNNING FAILED** and move error code to the log. 


#### **Downloading Data**

To download the data we use `wget` and the command you include in your shell script to meet the above requirements of selecting specific year and station is: 


>for year in {2020..2022};
>
>do wget -N --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year=${year}&Month=2&Day=14&timeframe=1&submit= Download+Data" -O ${INPUT_FOLDER}/${year}.csv;
>
>done;



Finally in your terminal you run your shell script using 

    $ bash path/shell_script.sh 

See attached scripts for more details on the python and shell script used. 


Congratulations, you have successfully completed the project 
![](./images/congratulations.jpg)

