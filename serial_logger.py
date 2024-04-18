import serial
port_name = "/dev/tty.usbmodem143401"

ser = serial.Serial(port_name, 115200)

filename = "serial_data.txt"
   
with open(filename, "w") as file:
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode()
            
            # Print the received data
            print(line)
            
            # Write the received data to the file
            file.write(line + "\n") 
            file.flush()

    except KeyboardInterrupt:
        # Close the serial connection and the file when the program is terminated
        ser.close()
        file.close()
