# what does this project do?
This project is a simple Python-based motion detector using a webcam (or smartphone IP camera).  
When motion is detected, the app takes a screenshot and sends it via email.
# How it works?
1. Accesses a video stream from a webcam or phone camera (via IP Webcam app).
2. Compares the current frame to the first frame (background).
3. Detects motion by looking at the difference.
4. Saves a snapshot of the frame with motion.
5. Sends an email alert with that image.
6. Deletes images to keep the folder clean.
# Requirements 
python 3.13 installed 
pip install opencv-python
# How to use with android?
1. install ip webcam app
2. start the server from the app
3. start the server from the app and use the video stream url
4. replace url with your actual ip in main.py
# Email
In emailing.py, edit the send_email() function to use your email and app password.
# Run the app