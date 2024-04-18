# How to use 
## Set up
If you're on a windows machine go to your device manager and look for hte relevant COM port that the device is using. Then modify the variable "port_name" in the python script.
This project is default using 115200 as the baudrate but you can change that value to whatever you wish. This value is located on line 4 of the code. \n

If you're on a Mac open a terminal and run "ls /dev/tty.*" to find the correct port. Then modify the variable "port_name" \n

Edit the  variable "filename" to change which file you want to store the data to. \n

## How to run
Open a terminal in the same directory as the python script and type "python3 serial_logger.py" into the terminal. This should start the script and you should see messages in your console.
To stop recording data simply type Ctrl+C to stop the script 

## Viewing data
In the same directory as the python script there should be a file with the same name as the "filename" variable. Go ahead and open it to see your data.

