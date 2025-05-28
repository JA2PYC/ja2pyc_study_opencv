from ocvmodule import VideoProcessor

vp = VideoProcessor()

# 1. 주석을 풀고 필요한 기능만 테스트하세요
# vp.annotate_video("data/sample.mp4", "data/output/annotated.mp4")
vp.convert_to_grayscale("data/input/sample.mp4", "data/output/gray.mp4")
# vp.detect_motion("data/sample.mp4")
# vp.detect_faces_from_camera()
# vp.record_from_camera("data/output/recorded.mp4", duration=5)


# from ocvmodule import ImageProcessor, VideoProcessor

# img_proc = ImageProcessor()
# video_proc = VideoProcessor()

# img = img_proc.load("data/input/sample.jpg")
# gray = img_proc.to_gray(img)
# img_proc.save(gray, "data/output/gray_sample.jpg")

# video_proc.capture_from_camera()
