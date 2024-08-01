# PTCG-KR Watermark Remover

이 프로젝트는 지정된 마스크를 사용하여 이미지에서 워터마크를 제거하는 Python 스크립트를 제공합니다. 개별 이미지 또는 폴더 내의 모든 이미지를 처리할 수 있습니다.

## 요구 사항

- Python 3.6 이상
- OpenCV
- NumPy

## 설치 방법

1. 이 저장소를 클론합니다:

    ```sh
    git clone https://github.com/yourusername/ptcg-kr-watermark-remover.git
    cd ptcg-kr-watermark-remover
    ```

2. 필요한 패키지를 설치합니다:

    ```sh
    pip install -r requirements.txt
    ```

## 사용 방법

### 명령줄 인수

- `--mask`: 마스크 이미지의 경로 (필수).
- `--file`: 단일 이미지 파일의 경로 (선택).
- `--folder`: 이미지 파일이 있는 폴더의 경로 (선택).
- `--output`: 처리된 이미지를 저장할 출력 디렉토리 (선택, 기본값은 `Images/Processed`).

### 예시

- **단일 이미지에서 워터마크 제거:**

    ```sh
    python ptcg_kr_watermark_remover.py --mask "Images/Tools/Mask Large.png" --file "Images/Watermarks/sample.png" --output "Images/Processed"
    ```

- **폴더 내 모든 이미지에서 워터마크 제거:**

    ```sh
    python ptcg_kr_watermark_remover.py --mask "Images/Tools/Mask Large.png" --folder "Images/Watermarks" --output "Images/Processed"
    ```

## 참고 사항

- 마스크 이미지와 입력 이미지가 올바르게 정렬되어 있는지 확인하십시오. 그래야 워터마크 제거가 효과적으로 작동합니다.
- 이 스크립트는 알파 채널이 있는 이미지를 지원합니다 (예: PNG 파일).

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.
