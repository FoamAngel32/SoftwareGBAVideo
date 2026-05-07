# SoftwareGBAVideo – GBA Pure Software Video Player
Both playback and conversion toolchain included
(actually there is no decode at all, just lz77 need to decompress)
# Build Require
 - `Python 3` (Third Party Modules will auto install by scripts)
 - `devkitpro` (or `devkitarm` + `libgba` + `libmm` + `grit` + `mmutil`)
 - `git` (optional, for cloning the repository)
# How to build
 - 1.make sure every image is using the same 256 color palette(see `palette.md` for how to create one)
 - 2.if your image is already scaled into 240x160, put it into `res/gfx`, and jump to step 6
 - 3.put your unscaled image into `res/og`
 - 4.run `tools/ConvertImage.py`, this will make sure your video is 160 scanlines and add border to reach 240x160
 - 5.check the `res/gfx` folder to make sure that your images are there
 - 6.run `tools/GenerateGrit.py` to generate an `.grit` for each images
 - 7.Put your video palette(256 colors limits) into the folder named `palette.png`, and DO NOT delete the `palette.grit`
 - 8.run `tools/FrameTool.py`
 - 9.run the `build.bat`(For WINDOWS only) or do it manually in your command line
And now you should have `SoftwareGBAVideo.gba` in the `build` folder
You can run it on any GBA emulator (`Mesen` recommended) or flashcart.
