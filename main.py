# main.py
from config.settings import Settings
from ocvmodule import cv_loader, cv_processor, cv_utils
from utils.logger import Logger

def main():
    
    config = Settings()
    logger = Logger()
    
    logger.log("이미지 로딩 중...")
    img = cv_loader.load_image(config.SAMPLE_IMAGE_PATH)

    logger.log("이미지 처리 중 (흑백 + 블러)...")
    gray = cv_processor.to_grayscale(img)
    blurred = cv_processor.apply_blur(gray, ksize=7)

    logger.log("결과 저장 중...")
    result_path = cv_utils.save_image(blurred, "result.jpg", config.OUTPUT_PATH)

    logger.log(f"저장 완료: {result_path}")

if __name__ == "__main__":
    main()
