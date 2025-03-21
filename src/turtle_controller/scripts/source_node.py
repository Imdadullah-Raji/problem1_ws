#!/usr/bin/env python3

import speech_recognition as sr
import rospy 
from std_msgs.msg import String

def get_message():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
            print("Listening...")
            audio = recognizer.listen(source, timeout=3)
            print("Audio received, processing...")
            
            text = recognizer.recognize_google(audio).lower()
            print("You said: ", text)
            message ='none'
            if "forward 5" in text:
                message= 'f5'
            elif "forward" in text:
                message= 'f'
            elif 'left' in text:
                message= 'l'
            elif 'right' in text:
                message= 'r'
            elif 'heal' or 'kaboom' in text:
                message= 'H'

        except sr.UnknownValueError:
            print("Could-not-Understand.")
            message= 'none'
            
        except sr.WaitTimeoutError:
            print("Timed out.")
            message='none'
    return message

if __name__== '__main__':

    rospy.init_node('source_node')
    pub= rospy.Publisher("/src_to_control", String, queue_size=10)

    rate= rospy.Rate(0.5)
    while not rospy.is_shutdown():
        message= String()
        message.data= get_message()
        pub.publish(message)
        print(message)

        rate.sleep()

