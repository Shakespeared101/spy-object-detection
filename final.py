import subprocess
from pathos.multiprocessing import ProcessingPool as Pool
import os
import datetime
oss = 2 #0 for windows 1 for linux 2 for mac

def det_phone(video_path):
    print("Hi")
    with open('phone_count.txt', 'w') as f:
        f.write('0')
# Construct the command to run the Python file with the video path as an argument
    command = f"python3 yolov7/detect.py --weights wts/phone_small_best.pt --conf 0.5 --source {video_path} --name exp1 --exist-ok"
    # Run the command using subprocess
    subprocess.run(command, shell=True)
    return 0

def det_camera(video_path):
    with open('camera_count.txt', 'w') as f:
        f.write('0')
    # Construct the command to run the Python file with the video path as an argument
    command = f"python3 yolov7/detect2.py --weights wts/final_camera_best.pt --conf 0.5 --source {video_path} --name exp2 --exist-ok"
    # Run the command using subprocess
    subprocess.run(command, shell=True)
    return 0

def det_mirror(video_path):
    with open('mirror_count.txt', 'w') as f:
        f.write('0')
    # Construct the command to run the Python file with the video path as an argument
    command = f"python3 yolov7/detect3.py --weights wts/mirror_best.pt --conf 0.5 --source {video_path} --name exp3 --exist-ok"
    # Run the command using subprocess
    subprocess.run(command, shell=True)
    return 0

def run_parallel_detections(video_path):
    print('Starting')
    # Create a pool of worker processes
    pool = Pool(processes=3)  # Adjust the number of processes as needed
    # List of functions to run in parallel
    functions = [det_phone, det_camera, det_mirror]

    # Run the functions in parallel
    results = [pool.apipe(func, video_path) for func in functions]

    # Wait for all processes to complete and collect results
    for result in results:
        result.get()

    print('Completed')

if __name__ == '__main__':
    video_path = 'output.mp4'  # Replace with your actual video path
    run_parallel_detections(video_path)

    with open('mirror_count.txt', 'r') as file:
        mirror = file.read()
    with open('phone_count.txt', 'r') as file:
        phone = file.read()
    with open('camera_count.txt', 'r') as file:
        camera = file.read()
    with open('/Users/shakthibala/Documents/VIT/BeauRoi/Mod1_FaceRec/flag.txt', 'r') as file:
        face = file.read()

    print(mirror,phone,camera,face)

    if mirror == '1' or phone == '1' or camera == '1' or face == '1' :
        if oss == 0 :
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif oss == 1 :
            os.system("xdg-screensaver lock")
        
        elif oss == 2:
            os.system("osascript -e 'tell application \"System Events\" to keystroke \"q\" using {control down, command down}'")
            print('locking pc')
        
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('log.txt', 'a') as file:
            file.write(formatted_time+'_'+mirror+phone+camera+face+'\n')

        os.rename('output.mp4', 'problem{formatted_time}.mp4')

        
        