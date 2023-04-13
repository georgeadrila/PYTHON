import subprocess
import time

# The name of the Oracle DBMS kernel process in Task Manager
process_name = "oracle.exe"

# Wait for Task Manager to start up
time.sleep(10)

# Check if the process is running
result = subprocess.run(["tasklist", "/fi", "imagename eq {}".format(process_name)], capture_output=True, text=True)
if process_name in result.stdout:
    # End the process
    subprocess.run(["taskkill", "/f", "/im", process_name])
    print("Oracle DBMS kernel process has been terminated.")
else:
    print("Oracle DBMS kernel process is not running.")
