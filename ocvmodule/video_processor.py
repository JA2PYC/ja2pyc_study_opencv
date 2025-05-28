import cv2

class VideoProcessor:
    def capture_from_camera(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Live", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def extract_frames(self, video_path, every_n=30):
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        saved = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % every_n == 0:
                filename = f"frame_{frame_count}.jpg"
                cv2.imwrite(filename, frame)
                saved.append(filename)
            frame_count += 1
        cap.release()
        return saved


    def annotate_video(self, input_path, output_path):
        cap = cv2.VideoCapture(input_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.putText(frame, f'Frame: {frame_number}', (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            out.write(frame)
            frame_number += 1

        cap.release()
        out.release()
        
    def convert_to_grayscale(self, input_path, output_path):
        cap = cv2.VideoCapture(input_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(gray)

        cap.release()
        out.release()

