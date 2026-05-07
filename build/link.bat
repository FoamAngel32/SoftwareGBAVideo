F:/devkitPro/msys2/opt/devkitpro/devkitARM/arm-none-eabi/bin/ar rcs frames.a img_T*.o
F:/devkitPro/msys2/opt/devkitpro/devkitARM/bin/arm-none-eabi-gcc -specs=gba.specs soundbank.bin.o palette.o main.o frames.a -o SoftwareGBAVideo.elf -LF:/devkitpro/msys2/opt/devkitpro/libgba/lib -lmm -lgba 
F:/devkitPro/msys2/opt/devkitpro/devkitARM/bin/arm-none-eabi-objcopy -O binary SoftwareGBAVideo.elf SoftwareGBAVideo.gba
F:/devkitPro/msys2/opt/devkitpro/tools/bin/gbafix SoftwareGBAVideo.gba -tno -c0000 -m00
