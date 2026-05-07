#include <gba.h>
#include <maxmod.h>
#include <fade.h>
#include "frames.h"
#include "soundbank.h"
#include "soundbank_bin.h"

#define VIDEO_WIDTH 240
#define VIDEO_HEIGHT 160
#define FRAME_SIZE (VIDEO_WIDTH * VIDEO_HEIGHT)

int current_frame __attribute__((section(".ewram"))) = 0;
u8 frame_buffer_0[FRAME_SIZE] __attribute__((section(".ewram"))) __attribute__((aligned(4)));
// u8 palette_buffer[512] __attribute__((section(".ewram"))) __attribute__((aligned(4)));

void VBLank()
{
    SetMode(MODE_4 | BG2_ENABLE | BACKBUFFER * !(current_frame % 2));
    dmaCopy(frame_buffer_0, (void *)VRAM + 0xA000 * (current_frame % 2), FRAME_SIZE);
    // dmaCopy(palette_buffer, &BG_PALETTE[0], 512);
    mmVBlank();
    mmFrame();
}

int main(void)
{
    irqInit();
    irqSet(IRQ_VBLANK, VBLank);
    irqEnable(IRQ_VBLANK);

    mmInitDefault((mm_addr)&soundbank_bin, 8);

    BGCTRL[0] = BG_16_COLOR | BG_SIZE_0 | (0 << 2) | (25 << 8);
    BGCTRL[1] = BG_16_COLOR | BG_SIZE_0 | (1 << 2) | (26 << 8);
    BGCTRL[2] = BG_16_COLOR | BG_SIZE_0 | (2 << 2) | (27 << 8);
    BGCTRL[3] = BG_16_COLOR | BG_SIZE_0 | (3 << 2) | (28 << 8);

    dmaCopy(paletteSharedPal, &BG_PALETTE[0], paletteSharedPalLen);
    BG_PALETTE[0xFC] = BG_PALETTE[0xFD] = BG_PALETTE[0xFE] = BG_PALETTE[0xFF] = RGB8(255, 255, 255);
    // This line is only for bad apple demo which only have 252 colors
    // mmEffect(SFX_VIDEO_TRACK);
    while (1)
    {
        current_frame++;
        if (current_frame > VIDEO_LENGTH)
            current_frame = 0;

        LZ77UnCompWram(frames[current_frame], frame_buffer_0);

        VBlankIntrWait();
    }

    return 0;
}
