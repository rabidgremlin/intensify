import os
import sys
import time
import logging
import time  
import subprocess
from subprocess import CalledProcessError
from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler  


class MyHandler(FileSystemEventHandler):
   
    def process(self, event):       
        action_script = self.find_action_script(event)
        
        if action_script is not None:
            self.execute_action_script(action_script, event)
        else:
            print "No action script for action %s " % str(event)
        
    def execute_action_script(self,action_script,event):
        try:
            print subprocess.check_output([sys.executable, os.path.abspath(action_script),os.path.abspath(event.src_path)])
        except CalledProcessError as e:
            print "FAILED: %s " % str(e)
            
        
    def find_action_script(self, event):
        if os.path.isfile(event.src_path):
            script_type = "file"
            action_script = os.path.join(os.path.dirname(event.src_path),".actions", "_" + script_type + "_" + event.event_type +".py")
        else:
            script_type = "dir"
            action_script = os.path.join(event.src_path,".actions", "_" + script_type + "_" + event.event_type +".py")        
        
        
        print "looking for action script %s..." % action_script
        
        if os.path.exists(action_script):
            return action_script
        else:
            return None        

    def on_any_event(self, event):
        self.process(event)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()