# Synopsis
Script sends a mail with a daily quote.

# Description
The script is used to send a mail with a custom quote from a book. The quotes needs to be inputted manually. Protocol for sending mail is SMTP SSL. 

# How to use
1. Download the project..
2. Run *scripts\createVenv.ps1* to create a virtual envirnment.
3. Run *scripts\installRequirements.ps1* to install all necessary packages.
4. Rename *all_quotes_template.csv* to *all_quotes.csv*. File is located in *data* folder.
5. Rename *secrets_template.py* to *secrets.py*. File is located in *src* folder.
6. Fill *all_quotes.csv* with all your quotes.
7. Fill *secrets.py* with necessary values.

# Directory struture
*config* - contains only config files. The default that is automatically read is named *config.ini*.  
*logs* - all log files will be stored here.  
*scripts* - contains "helper" scripts to build virutal environment and install requirements.  
*src* - *.py* files should be stored here.

More at [martinautomates.com](https://www.martinautomates.com)