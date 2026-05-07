arm-none-eabi/bin/ar rcs frames.a img_T*.o
arm-none-eabi-gcc -specs=gba.specs soundbank.bin.o bad_apple_palette.o main.o frames.a -o SoftwareGBAVideo.elf -LF:/devkitpro/msys2/opt/devkitpro/libgba/lib -lmm -lgba 
arm-none-eabi-objcopy -O binary SoftwareGBAVideo.elf SoftwareGBAVideo.gba
gbafix SoftwareGBAVideo.gba -tno -c0000 -m00
