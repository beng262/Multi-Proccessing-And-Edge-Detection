import cv2
import time
import threading

rtsp_link = 'rtsp://admin:cozum234567@192.168.2.240:554/Streaming/channels/1001'

class ProcessThread(threading.Thread):
    def __init__(self, frame):
        threading.Thread.__init__(self)
        self.frame = frame
    def run(self):
        self.frame = process_frame(self.frame)

def process_frame(frame):
    frame = cv2.resize(frame, (600, 400))
    return frame

if __name__ == "__main__":
    time_start = time.time()
    count = 0
    cap = cv2.VideoCapture(rtsp_link)
    pre_timeframe = 0
    new_timeframe = 0
    av = 0

    while(cap.isOpened()):
        new_timeframe = time.time()
        success, frame = cap.read()
        if not success:
            break

        process_thread = ProcessThread(frame)
        process_thread.start()
        process_thread.join()
        frame = process_thread.frame

        fps = 1 / (new_timeframe - pre_timeframe)
        pre_timeframe = new_timeframe
        fps = int(fps)

        count += 1
        av += fps
        average_fps = av / count

        cv2.putText(frame, str(average_fps), (8, 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (88, 68, 66), 2)
        cv2.imshow("vid", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
