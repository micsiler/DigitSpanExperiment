# DigitSpanExperiment

Note: This code is for an experiment project conducted for Q370 assignment

## Overview

This was an experiment used to test the reliance of phones given a digit span memory test. 

The paper including results can be found at: [paper link](https://docs.google.com/document/d/1udLIG-rgELkK387SGfSi_BFEi5V5slYpYx0IWYJMVkY/edit?usp=sharing)

The survey was conducted with [qualtrics survey link](https//iu.co1.qualtrics.com/jfe/form/SV_6g6iUUmcIIo769E)


### experimentTest.py

This is the main file to conduct the experiment using Tkinter. This is a standard digit span memory test ranging from 3 digit sequences to 8 digit sequences
The outputed accuracy is to recorded in score_data.txt. (note input_data.txt was used to check if the program was working, but also collects input and generated sequences from the user)

### experimentAnalysis.r

R script used to analyze the data from the experiment and survey results.
The survey results are found in phone_reliance_assessment.csv
Reorganized score data mainly used for the analysis is found in main_data.txt

