num_frames = abs(int(float((''.join(filter(str.isdigit, input("how many frame do you have?\n>>>")) or '0')))))
name = input("What name are they all start with?(must end with 4 digits of number index and start with 0)\n>>>")
with open("F:/project/GBA/SoftwareGBAVideo/src/frames.h", "w") as f:
    f.write("#ifndef FRAMES2_H\n#define FRAMES2_H\n\n")
    for i in range(num_frames):
        f.write(f'#include "{name}{i:04d}.h"\n')
    f.write("\n")
    f.write(f"const unsigned int* frames[{num_frames}] = {{\n")
    for i in range(num_frames):
        f.write(f"    {name}{i:04d}Bitmap")
        if i != num_frames-1:
            f.write(",\n")
        else:
            f.write("\n")
    f.write("};\n\n#endif // FRAMES2_H\n")
