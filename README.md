# Heart Rate Monitor 

This project uses an LED and a light sensor on a finger clip to measure heart rate. The voltage from the LED goes through a comparator to create a square wave representing heart rate. This square wave's period       is measured by using the microcontroller's built in timer and measuring the voltage of a pin where the wave is being fed into. 
  
From this, the period is converted into heart rate in beats per minute and displayed on the LED and sent to serial. Using the BPM sent to the serial, our python program provides to monitoring options: serious mode and game mode.
- Serious mode:
  -  Using a settable moving average of the BPM's received, displays and graphs both actual and averaged heart rate
  -  Filters out extreme values that occur from noise/sensor movement (>250BPM)
- Game Mode:
  - Using a "flappy bird" style gameplay, the heart rate is graphs and the user tries to avoid beams by changing their heart rate
  - The game is built using the matplot library which allows for easy manipulation and display of data receved
  - The number of "lives" is settable
  - When the game is lost, by losing all lives, a game recap window displays the users score and average BPM during the game
 
The controller also accounts for sensor not being placed on finger. If heartrate is not detected after ~5 seconds, an error message will display and the program will terminate.
  


