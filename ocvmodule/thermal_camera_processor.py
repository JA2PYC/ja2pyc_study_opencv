import cv2

class ThermalCameraProcessor:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index

    def start_feed(self):
        cap = cv2.VideoCapture(self.camera_index)

        if not cap.isOpened():
            print("카메라를 열 수 없습니다.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 열화상은 보통 흑백 또는 컬러맵 이미지로 출력
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 색상맵 적용 (예: JET 컬러맵 -> 빨간색이 고온)
            thermal = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

            cv2.imshow("Thermal Feed", thermal)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
