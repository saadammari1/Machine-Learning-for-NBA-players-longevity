## NBA ROOKIE 5 YEARS LONGEVITY PREDICTION 

* notebook.iynb showcases the selected model with the best performance and presents the features on which I relied for making predictions. 


* app.py is the script that you run to start the server for the web service.
    steps : 
        - pip install flask
        - run the python file, and access to the link generated 
        - fill the inputs in the webservice with the required values, 
        here some random examples from the dataset (in the same order of the required inputs of webservice )

           'GP', 'MIN', 'PTS', 'FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV' 
            58    11.6   5.7    2.3   5.5   42.6  0.9   1.3   68.9   1.0    0.9   1.9    0.8  0.6   0.1   1.0 label = 1
            48    11.5   4.5    1.6   3.0   52.4  1.3   1.9   67.4   1.0    1.5   2.5    0.3  0.3   0.4   0.8 label = 1
            36    27.4   7.4    2.6   7.6   34.7  1.6   2.3   69.9   0.7    3.4   4.1    1.9  0.4   0.4   1.3 label = 0

        - get the prediction abt the rookie 