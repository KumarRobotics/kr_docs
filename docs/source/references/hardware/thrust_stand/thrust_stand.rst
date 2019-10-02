Thrust Stand Testing
====================

There comes a time in every engineer's life, when they must measure thrust coefficients and efficiency from propeller-motor combinations. This is that.

=====================================================
RC Benchmark Series 1580 Thrust Stand and Dynamometer
=====================================================

**Necessary hardware:**

- RC Benchmark 1580 Board
- RC Benchmark structure (including two 2kg load cells and one 5kg load cell)
- Calibration hardware (200g mass, beam, and screws)
- Mini USB Type-B Cable
- Computer with RC Benchmark software installed
- Motor and Propeller

- ESC (appropriately spec'd for motor/prop combo)
- Power Supply (with appropriate voltage/current/power ratings)
- Power Cables (stripped on one end)
- Non-reflective tape
- Reflective tape
- Optical Sensor and cable
- 4x motor mounting screws
- Corresponding screw driver
- 2x C-clamps


**Performing a Thrust Test:**

1. Assuming the thrust stand has already been assembled, clamp down the bottom of the structure to a flat surface.
2. Download the RC Benchmark Software here: https://rcbenchmark.gitlab.io/docs/en/dynamometer/software/dynamometer-software-download.html
3. Connect the RC Benchmark board to your computer via the Mini-USB Type B cable and press the "Connect" button on the left side of the RC Benchmark software.
4. Under the "Utilities" tab, perform a thrust calibration and, if necessary, a torque calibration. When you are done, reclamp the thrust stand to your work surface.
5. Connect the power cables from your ESC to the respective positive and negative screw terminals labeled, "ESC", on top of the PCB.
6. Connect the signal cables from your ESC to the header pins labeled, "ESC". (Note: Colors may vary, but Black will "always" be ground/negative.)
7. Connect the power cables from your power supply to the respective positive and negative screw terminals labeled, "Power Input" and "Ground", respectively.
8. Tape the motor's side with non-reflective tape. Usually, the motor's metal housing will already be reflective, so you may or may not need to tape an additional small strip of reflective tape on the motor.
9. Mount the propeller/motor combination to the thrust stand. (Note: for small motors, you may need to create an mounting adapter.)
10. Mount the optical RPM sensor relatively close the the motor. Connect the sensor cables to one of the headers labeled, "S1", "S2", or "S3". (Note: The board does not by default provide power to sensor. You will need to provide an external 5V source from your ESC, power supply, or with a wire bridge from one of the board's 5V sources.)
11. Optional: To use the electrical RPM sensor, connect a jumper cable from the pin labeled, "RPM probe", to one of the ESC leads. Then, under "Utilities", adjust the value for the "Number of Poles" setting to match your motor.
12. Connect the motor leads to the ESC.
13. Turn on your power supply and adjust the voltage and current limit accordingly.
14. Under the "Setup" tab, set working units to the system you prefer, select a folder to be your working directory, and flash the latest firmware if it is not up-to-date.
15. Under the "Safety Cutoffs" tab, adjust the cutoffs to values appropriate to your prop/motor combination.
16. Under the "Manual Control" tab, navigate to the "ESC" scrollbar, where you can adjust the duty cycle to check the direction the motor is spinning. If the motor is spinning the wrong way, switch the order of two of the three motor cables.
17. Under the "Automatic Control" tab, click the "Script" drop box and select "Sweep - continuous". Here, you can adjust the minimum and maximum PWM values, and total time, among other things. When you are ready, zero the load cells by pressing "Tare Load Cells", then press the "Run" button followed by the "Start" button to begin the test.

**Important:** Make sure that the propeller is either pointed toward or away from you in case the propeller breaks. For larger propellers, you will want to use the caged enclosure located in the motion capture space at PERCH. Lastly, always wear safety glasses when doing thrust tests.

**Tips & Troubleshooting:**

- Make sure to fasten your ESC and power cabling securely with cable ties. Dangling power cables can affect the readings.
- For testing multiple motors, it may be a good idea to solder screw terminals to your ESC to avoid repeatedly soldering connectors to the motor leads.
- It is a good idea to periodically perform a calibration on the ESC. First, remove the propeller from the motor and, under "Manual Control", uncheck the box under the ESC scrollbar. Set the scrollbar to its maximum and check the box. The ESC should audibly indicate via the motor that it is in calibration mode. Uncheck and recheck the box, then set the scrollbar to its minimum position. The ESC will cause the motor to emit a tone if the calibration was successfull. You can check this by adjusting the scroll bar.
- To obtain a thrust/rpm curve, the voltage supplied to the ESC is not extremely important, and you can just use the nominal battery voltage of your system. If you would like map the duty cycle(therefore voltage) to thrust more accurately, you can run tests at your maximum and minimum voltages and interpolate.
- For further details beyond this quick-start guide, RCBenchmark's online documentation can be found here: https://rcbenchmark.gitlab.io/docs/en/series-1580.html