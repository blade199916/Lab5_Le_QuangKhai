Name: Quang Khai Le
SJSU ID:012508275
Class: EE 104 
Professor: Christopher Pham 


Github link:https://github.com/blade199916/Lab5_Le_QuangKhai.git

Video link:
Software part: https://youtu.be/UoACuFd7-no
Hardware part: https://youtu.be/DMzpAyXFuE8



README
Introduction
This Python program is composed of three parts: a heartbeat rate monitor, a COVID-19 modeling tool, and a red alert game program. Here are the instructions on how to run and understand each part of the program.


Requirements
Before running the program, make sure that you have the following installed:
_ Python 3.7 or later
_ Required Python modules (if any) that are mentioned in each part of the program
_ The board and ethernet cable to make sure you can do the EMS hardware
Installation
To install the program, follow these steps:
1. Clone or download the program files to your local machine.
2. Open a command prompt or terminal window.
3. Navigate to the directory where you saved the program files.
4. Run each part of the program using the following commands:
Copy code
python heartbeat_rate.py
Copy code
python covid19_modeling.py
Copy code
python red_alert_game.py


Usage
Once you have installed the program, you can use each part of it by following these steps:


Part 1) Heartbeat Rate Monitor
1. Open a command prompt or terminal window.
2. Download random heartbeat wav file from the website 
3. Use the convert wav to csv
4. In the excel file generated only keep one column of the result/1000
5. Navigate to the directory where you saved the program files.
6. Run the program using the following command:
Copy code: 
  

  

Once you have entered the required information, the program will calculate your maximum heart rate and target heart rate zone from the heart rate of your choice after the last step required you to divided you range of data for 18
  
  



Part 2) COVID-19 Modeling Tool
1. Open a command prompt or terminal window.
2. Navigate to the directory where you saved the program files.
3. Run the program using the following command:
4. Copy code
  

python covid19_modeling.py
  

The program will prompt you to enter the required information about the COVID-19 scenario you want to model Epidemiology. Pick random 5 functions of your choice in order to generate the plot to compare(Model States S, I, and two states of your choice from the SIDARTHE mathematical model). Once you have entered the required information, the program will display a graph of the modeled scenario.
  

Part 3) EMS software with Python Hardware Programming: 
Make sure you install PYNQ
Connect to the board by the ethernet cable, then use the provided guideline in the lab5.doc to follow professor instruction about how to connect wifi and board. 
Finish your circuit 
Go the website directory to check the code
https://github.com/cathalmccabe/PYNQ_tutorials/blob/master/ps_gpio/kria_kv260_example/ps_gpio_kv260.ipynb
Follow the code to see the each situation of LED combinations on and off
  

Part 4) Red Alert Game Program
1. Open a command prompt or terminal window.
2. Navigate to the directory where you saved the program files.
3. Run the program using the following command:
4. Copy code
  



python red_alert_game.py
The program will open the game window.
Use the arrow keys to avoid the obstacles( the other color starts) and only choose red stars.  


Troubleshooting. 
If you encounter any issues while running the program, try the following troubleshooting steps:
Make sure that you have installed all the required dependencies and modules.
Check that you have entered the correct inputs or selected the correct options.
Try running the program again with different inputs or options.


Conclusion
This program is a collection of tools that can help you monitor your heart rate, model COVID-19 scenarios, and play a game. If you have any questions or feedback, feel free to reach out to the program's author.


