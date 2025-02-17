#1 файл 100мб командою лінукс з назвою поточного часу (subprocess),
#1 поток вичитування цього файлу, 2 поток на запис у новий файл інформації з першого файлу.

import subprocess
import threading
import queue

data_queue = queue.Queue()

# Running a command and capturing its output
completed_process1 = subprocess.run(["truncate", "-s", "100M", "g100M1.txt"], capture_output=True, text=True)
with open("g100M1.txt", "w") as file:
    completed_process2 = subprocess.run(["date"], stdout=file)

# Accessing the output
#print(completed_process1.stdout)
#print(completed_process2.stdout)

# Checking the return code
if completed_process1.returncode != 0:
    print("The command1 failed with return code", completed_process1.returncode)

if completed_process2.returncode != 0:
    print("The command2 failed with return code", completed_process2.returncode)

def f_t1():
    with open("g100M1.txt", "r") as file1:
        data1 = file1.read()
        print(f"Data from thread #1 in file g100M1.txt: {data1}")
        file1.close()
        data_queue.put(data1)

def f_t2():
    data2 = data_queue.get()
    with open("g100M2.txt", "w") as file2:
        file2.write(data2)
        print(f"Data from thread #2 in file g100M2.txt: {data2}")

thread1 = threading.Thread(target=f_t1)
thread2 = threading.Thread(target=f_t2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

