import cv2
import os
import numpy as np
import argparse
from pathlib import Path

def remove_watermark(card_path, mask_path, output_dir):
    card_name = Path(card_path).name
    output_path = os.path.join(output_dir, card_name)

    # 이미지 읽기
    card_original = cv2.imread(card_path, cv2.IMREAD_UNCHANGED)
    if card_original is None:
        print(f"Failed to load image {card_path}")
        return

    alpha = card_original[:, :, 3]
    card = card_original[:, :, :3].astype(np.float32) / 255.
    mask = cv2.imread(mask_path, cv2.IMREAD_COLOR).astype(np.float32) / 255.

    OPACITY = 0.64
    base = card * (1.0 - mask)
    w = card * mask
    gt = (w - OPACITY * mask) / (1.0 - OPACITY)
    result = (gt + base) * 255
    result = cv2.cvtColor(result, cv2.COLOR_RGB2RGBA)
    result[:, :, 3] = alpha

    cv2.imwrite(output_path, result)
    print(f"Processed {card_name}, saved to {output_path}")

def process_all_images(card_dir, mask_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(card_dir):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                card_path = os.path.join(root, file)
                remove_watermark(card_path, mask_path, output_dir)

def main():
    parser = argparse.ArgumentParser(description="Remove watermarks from images using a specified mask.")
    parser.add_argument('--mask', type=str, required=True, help="Path to the mask image.")
    parser.add_argument('--file', type=str, help="Path to a single image file.")
    parser.add_argument('--folder', type=str, help="Path to a folder containing image files.")
    parser.add_argument('--output', type=str, default='Images/Processed', help="Output directory for processed images.")

    args = parser.parse_args()

    if not args.file and not args.folder:
        parser.error("You must specify either a file or a folder.")

    if args.file:
        remove_watermark(args.file, args.mask, args.output)
    if args.folder:
        process_all_images(args.folder, args.mask, args.output)

if __name__ == "__main__":
    main()
