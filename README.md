
* running directly on a bokeh-server
* embedded into a separate Flask application

You will need to first download some sample data, then follow the
instructions for running the example.

Sample Data
===========

To run the stocks applet example, you first need to download a sample data
file. The file is located at:

    http://quantquote.com/files/quantquote_daily_sp500_83986.zip

A python script is included in the applet's directory to collect and extract 
the data, which can be run directly from the directory:

    python stock_data.py

You can use a browser to download the file, or depending on your system you
may be able to use curl:

    curl -O http://quantquote.com/files/quantquote_daily_sp500_83986.zip

or wget:

    wget http://quantquote.com/files/quantquote_daily_sp500_83986.zip

from the command line. Once the file is downloaded you should move it
to this directory, and unzip it. You may be able to unzip the file by
clicking on it, or by executing this command from the command line:

    unzip quantquote_daily_sp500_83986.zip

This should leave a "quantquote_daily_sp500_83986" subdirectory in this directory.
Move the 'daily' directory by executing this command from the command line:

    mv quantquote_daily_sp500_83986/daily .

Now you can safely remove the empty "quantquote_daily_sp500_83986" directory.

Running
=======

Bokeh Server
------------

To view this applet directly from a bokeh server, you simply need to
run a bokeh-server and point it at the stock example script:

    bokeh-server --script stock_app.py

Now navigate to the following URL in a browser:

    http://localhost:5006/bokeh/stocks

Flask Application
-----------------

To embed this applet into a Flask application, first you need to run
a bokeh-server and point it at the stock example script. In this
directory, execute the command:

    bokeh-server --script stock_app.py

Next you need to run the flask server that embeds the stock applet:

    python flask_server.py

Now you can see the stock correlation applet by navigating to the following
URL in a browser:

    http://localhost:5050/

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
the ui is a fork from bokeh-server example .

extract the app in your home directory
 
for best result have the following packages running in your unix environment
-anconda distribution python 2.7(should have everything)
-bokeh-server may need to be added 

have not trained the full list of fortune five hundred companies 

only a few have been tarined and predicted .
feel free to train the reset using the algorithm in the ipython notebook testing stuff .

to train the next set of stock modify the lists in stoc_app.py and neural_net_train&store_data.py
execute neural_net_train&store_data.py to predict and sotre reuslts automaticly

have fun and feel free to extend it to your needs 

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
