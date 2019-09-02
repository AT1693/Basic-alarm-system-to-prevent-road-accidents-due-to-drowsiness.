Project Description:-
OWL is a next-generation safety add-on feature for cars of all segments.
Drowsy driving is a major problem worldwide. The risk, danger, and often tragic results of drowsy driving are alarming. It is the dangerous combination of driving and sleepiness or fatigue. This usually happens when a driver has not slept enough, but it can also happen due to untreated sleep disorders, medications, drinking alcohol, or shift work.

OWL is reliable system built on a single processing unit that has a camera attached to it. The camera is placed on the dashboard of the car(the camera's height is adjustable). The algorithms(inside the software) fed in the CPU enables the camera to scan the eyes of the driver and check if he's feeling drowsy. If the results come out to be positive, the sharp lights directed straight towards the driver's eyes start blinking and a high frequency alarm is set off inside the car. This in turn, brings the driver back to full consciousness

Technologies Used:-

1. Rasbperry PI
2. Open CV and numpy
3. Dlib
4. Python 3.6
5. Raspbian coding
6. imutils
7. Haar Cascade

Challenges Faced:-

The following were some of the challenges faced by us in developing the OWL project:-

1. Installing the dlib library on pi and using it's functions
2. Reducing the time lag of Pi-cam and increasing it's frame rate.
3. Building logics for detecting drowsiness accurately.
4. Creating a virtual environment on PI for running the code.
5. Force default of PI cam over USB cam using modprobe.
6. Importing a working code from laptop and make it run in CV environment on PI.
7. Increasing the resolution of the captured frames so that drowsiness is detected even in the case of people wearing spectacles.
8. Working with the functions of cascade.
9. Working on Raspberry Pi pins and GPIO library.

Execution/Installation Guidelines :-

The PI (inside a  PI-case) would be placed somewhere beneath the steering wheel. The PI-cam would have a double-sided tape attached to its back along with a height-adjustable stand and the stand would be stuck on the Dashboard
The software will start running as soon as the car is started (when the PI board will get power, the algorithms (inside the software embedded in it) will get loaded in its RAM. Use of sunglasses is discouraged as the camera placed on the dashboard of the car would most likely would not be able to recognize drowsiness in that case. When drowsiness is detected, a software interrupt would be initialized which would cause the mini speakers (attached to the side of the PI) to emit a shrill voice and the sharp lights (stuck on both sides of the stand) directed towards the drive's eyes, to blink in short intervals.



Team:-

Sonali Mehta
Alarsh Tiwari

