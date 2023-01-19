# import the modules
import sys
import time
import logging
import watchdog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# if __name__ == "__main__":
#     # Set the format for logging info
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')

#     # Set format for displaying path
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'

#     # Initialize logging event handler
#     event_handler = LoggingEventHandler()

#     # Initialize Observer
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)

#     # Start the observer
#     observer.start()
#     try:
#         while True:
#             # Set the thread sleep time
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()








# import watchdog.events
# import watchdog.observers
# import time


# class Handler(watchdog.events.PatternMatchingEventHandler):
#     def __init__(self):
#         # Set the patterns for PatternMatchingEventHandler
#         watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
#                                                             ignore_directories=True, case_sensitive=False)

#     def on_created(self, event):
#         print("Watchdog received created event - % s." % event.src_path)
#         # Event is created, you can process it now

#     def on_modified(self, event):
#         print("Watchdog received modified event - % s." % event.src_path)
#         # Event is modified, you can process it now


# if __name__ == "__main__":
#     src_path = r"C:\Users\arnag\Desktop\test1_in"
#     event_handler = Handler()
#     observer = watchdog.observers.Observer()
#     observer.schedule(event_handler, path=src_path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

main.py file

# import watchdog
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# import os 
# import json
# import time
# class MyHandler(FileSystemEventHandler):
#     def on_modified(event):
#         dir1 = os.listdir(tracking_folder)
#         print(dir1)
#         for fname in dir1:
#             fname1=fname
#             fname2=fname
#             src = tracking_folder + "\\" + fname1
#             dest = dest_folder + "\\" + fname2
#             file_done = False
#             file_size = -1
#             while file_size != os.path.getsize(tracking_folder):
#                 file_size = os.path.getsize(dest_folder)
#                 time.sleep(1)
#             while not file_done:
#                 try:
#                     os.rename(src, dest)
#                     file_done = True
#                 except:
#                     return True        
# tracking_folder="D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder"  
# dest_folder="D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/dest_folder"     
# event_handler=MyHandler()
# event_handler.on_modified=on_modified
# observer=Observer()
# observer.schedule(event_handler,tracking_folder,recursive=True)
# observer.start()
# print("starting")
# try:
#     while True:
#         time.sleep(3)
# except KeyboardInterrupt:
#     observer.stop() 
# observer.join()     