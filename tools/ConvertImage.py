import os
import sys
try:
    from PIL import Image 
except Exception as e:
    os.system("pip install pillow")

def process_images(input_folder, output_folder, target_width=240, target_height=160, background_color=(0, 0, 0)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"create output dir: {output_folder}")
    
    extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    image_files = []
    for file in os.listdir(input_folder):
        if file.lower().endswith(extensions):
            image_files.append(file)
    
    if not image_files:
        print(f"No image is found in{input_folder}")
        return
    
    print(f"find {len(image_files)} images")
    print(f"目标分辨率: {target_width}x{target_height}")
    
    for idx, filename in enumerate(image_files, 1):
        input_path = os.path.join(input_folder, filename)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}{ext}")
        
        try:
            with Image.open(input_path) as img:
                if img.mode not in ('RGB', 'L'):
                    img = img.convert('RGB')
                
                original_width, original_height = img.size
                print(f"[{idx}/{len(image_files)}] to: {filename} ({original_width}x{original_height})")
                
                scale_ratio = target_height / original_height
                new_width = int(original_width * scale_ratio)
                new_height = target_height
                
                if new_width > target_width:
                    scale_ratio = target_width / original_width
                    new_width = target_width
                    new_height = int(original_height * scale_ratio)
                
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                canvas = Image.new('RGB', (target_width, target_height), background_color)
                
                x_offset = (target_width - new_width) // 2
                y_offset = (target_height - new_height) // 2
                
                canvas.paste(resized_img, (x_offset, y_offset))
                
                # 保存图片
                canvas.save(output_path)
                print(f"    output: {new_width}x{new_height} → scale to {target_width}x{target_height}")
                
        except Exception as e:
            print(f"    when {filename} is produced, there is an error: {e}")
    
    print(f"Done! {len(image_files)} is produced to: {output_folder}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python resize_images.py <into dir> [output dir]")
        print("Example: python resize_images.py ./frames ./frames_resized")
        print("Resulotion: 240x160 (GBA Mode 4)")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_folder = sys.argv[2]
    else:
        output_folder = input_folder.rstrip('/\\') + "_resized"
    
    if not os.path.exists(input_folder):
        print(f"error: folder {input_folder} does not exist")
        sys.exit(1)
    
    process_images(input_folder, output_folder)

if __name__ == "__main__":
    main()
