import sched
import time
import cv2
import os

def my_function():
    print("Running my function...")
    #Capture video from webcam

    # Define the duration for the capture
    capture_duration = 5  # seconds

    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 is usually the default ID for the built-in webcam

    # Get the default frame width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Initialize variables for frame counting
    frame_count = 0
    start_time = time.time()

    # List to hold captured frames
    frames = []

    # Capture frames for the specified duration
    while int(time.time() - start_time) < capture_duration:
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
            frame_count += 1
            # cv2.imshow('frame', frame)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Calculate the actual frame rate
    end_time = time.time()
    actual_duration = end_time - start_time
    frame_rate = 5

    # Define the codec and create VideoWriter object to save the video
    out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

    # Write the captured frames to the video file
    for frame in frames:
        out.write(frame)

    # Release the webcam and file
    cap.release()
    out.release()
    cv2.destroyAllWindows()  # Ensure all windows are closed

    print(f"Video capture complete. Saved as output.mp4 at {frame_rate:.2f} FPS")
    
    print("Calling final.py")
    os.system("python3 final.py")


def schedule_function(scheduler):
    scheduler.enter(600, 1, schedule_function, (scheduler,))
    my_function()

# os.system("python3 ../Mod1_FaceRec/StreamFace.py")
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(0, 1, schedule_function, (my_scheduler,))
my_scheduler.run()
