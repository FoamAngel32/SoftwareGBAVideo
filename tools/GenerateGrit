import os
import sys

DEFAULT_GRIT_CONFIG = """# grit config for GBA sprite frame
# 8 bit bitmap 256 color limits
-gB8

# bitmap format
-gb

# use lz77 compression
-gzlz77
-p!
"""

def generate_grit_file(input_image_path, output_grit_path=None, overwrite=False):
    if output_grit_path is None:
        base = os.path.splitext(input_image_path)[0]
    if os.path.exists(output_grit_path) and not overwrite:
        print(f"Skip existing: {output_grit_path} (use --overwrite to.. you know, overwrite)")
        return False
    with open(output_grit_path, 'w', encoding='utf-8') as f:
        f.write(DEFAULT_GRIT_CONFIG)
    
    print(f"生成: {output_grit_path}")
    return True

def batch_generate_grit(input_folder, output_folder=None, overwrite=False, recursive=False):
    extensions = ('.png', '.bmp', '.jpg', '.jpeg', '.gif', '.tiff', '.webp')
    
    image_files = []
    if recursive:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.lower().endswith(extensions):
                    image_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(input_folder):
            if file.lower().endswith(extensions):
                image_files.append(os.path.join(input_folder, file))
    
    if not image_files:
        print(f"no image found in {input_folder}")
        return
    
    print(f"find {len(image_files)} image(s)")
    
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"create output dir: {output_folder}")
    
    success_count = 0
    for img_path in image_files:
        if output_folder:
            rel_path = os.path.relpath(img_path, input_folder)
            base = os.path.splitext(rel_path)[0]
            grit_path = os.path.join(output_folder, base + ".grit")
            os.makedirs(os.path.dirname(grit_path), exist_ok=True)
        else:
            base = os.path.splitext(img_path)[0]
            grit_path = base + ".grit"
        
        if generate_grit_file(img_path, grit_path, overwrite):
            success_count += 1
    
    print(f"\nDone, Create {success_count}/{len(image_files)} .grit(s)")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='.grit generator')
    parser.add_argument('input', help='input image path')
    parser.add_argument('-o', '--output', help='intput output path')
    parser.add_argument('--overwrite', action='store_true', help='overwrite .grit')
    parser.add_argument('-r', '--recursive', action='store_true', help='with sub dirs')
    parser.add_argument('--single', action='store_true', help='single file meode')
    
    args = parser.parse_args()
    
    if args.single or os.path.isfile(args.input):
        generate_grit_file(args.input, overwrite=args.overwrite)
    else:
        batch_generate_grit(args.input, args.output, args.overwrite, args.recursive)

if __name__ == "__main__":
    main()
