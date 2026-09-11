#!/usr/bin/env python3
"""
Render cinematic Ken Burns clips from the Doucet project stills.

Usage:  python3 render_clips.py out
Needs:  pip install pillow imageio-ffmpeg

Camera motion is computed in Python and applied with a PIL affine transform,
so every move is sub-pixel exact - no zoompan jitter. Frames are piped as
raw RGB straight into ffmpeg.
"""
import os, subprocess, sys
from multiprocessing import Pool
from PIL import Image
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/out"
FPS, DUR, XFADE = 30, 3.6, 0.55

# cx/cy = crop centre as a fraction of the image; z = fraction of the largest
# crop that fits the target aspect (1.0 = widest, smaller = pushed in).
SHOTS = {
    "01-front-wall-hero": dict(
        a=dict(cx=0.60, cy=0.50, z=0.97), b=dict(cx=0.41, cy=0.43, z=0.87),
        note="Front wall at ground level - drift left along the coursing, easing in"),
    "02-front-elevation": dict(
        a=dict(cx=0.45, cy=0.50, z=1.00), b=dict(cx=0.45, cy=0.43, z=0.86),
        note="Street elevation - slow push in, tilting up to the house"),
    "03-wall-detail":     dict(
        a=dict(cx=0.56, cy=0.52, z=0.95), b=dict(cx=0.44, cy=0.50, z=0.85),
        note="Close on block coursing and the planted trench - the craftsmanship beat"),
    "04-entry-front":     dict(
        a=dict(cx=0.47, cy=0.52, z=1.00), b=dict(cx=0.48, cy=0.45, z=0.85),
        note="Entry straight on - push in on the door, steps and landing"),
    "05-entry-patio":     dict(
        a=dict(cx=0.44, cy=0.50, z=0.98), b=dict(cx=0.40, cy=0.45, z=0.86),
        note="From the landing looking out - push in reads like walking down the steps"),
    "06-driveway-wall":   dict(
        a=dict(cx=0.33, cy=0.52, z=0.90), b=dict(cx=0.52, cy=0.48, z=0.98),
        note="Driveway level - travel right along the wall as it runs to the street"),
    "07-drone-low":       dict(
        a=dict(cx=0.43, cy=0.52, z=0.86), b=dict(cx=0.46, cy=0.48, z=1.00),
        note="Low drone - pull back to reveal the full frontage"),
    "08-back-reveal":     dict(
        a=dict(cx=0.55, cy=0.52, z=0.86), b=dict(cx=0.50, cy=0.48, z=1.00),
        note="Backyard reveal - pull out across the lawn to the patio"),
    "09-back-terrace":    dict(
        a=dict(cx=0.46, cy=0.52, z=1.00), b=dict(cx=0.43, cy=0.46, z=0.86),
        note="Terrace wall and steps against the treeline - push in on the stair"),
    "10-patio-dining":    dict(
        a=dict(cx=0.46, cy=0.52, z=0.98), b=dict(cx=0.44, cy=0.48, z=0.86),
        note="Patio dining set - slow push in"),
    "11-patio-lounge":    dict(
        a=dict(cx=0.38, cy=0.52, z=0.90), b=dict(cx=0.58, cy=0.50, z=0.92),
        note="Fire table to loungers - lateral drift, the lifestyle beat"),
    "12-drone-high":      dict(
        a=dict(cx=0.47, cy=0.52, z=1.00), b=dict(cx=0.45, cy=0.44, z=0.87),
        note="High drone - push in, settling on house and terrace"),
    "13-drone-wide":      dict(
        a=dict(cx=0.46, cy=0.52, z=0.88), b=dict(cx=0.47, cy=0.49, z=1.00),
        note="Wide drone - pull out to close on the whole property"),
}

ORDER = list(SHOTS)                                      # full tour, front -> back
SHORT = ["01-front-wall-hero", "03-wall-detail", "04-entry-front",
         "09-back-terrace", "11-patio-lounge"]           # punchy hook cut

FORMATS = {"vertical": (9 / 16, 1080, 1920),             # Reels / TikTok / Shorts
           "square":   (1.0, 1080, 1080)}                # feed posts

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "22",
       "-maxrate", "9M", "-bufsize", "18M",
       "-pix_fmt", "yuv420p", "-movflags", "+faststart"]


def ease(t):
    """Mostly linear with a gentle ease at each end - keeps the move flowing
    through a crossfade instead of stopping dead at the cut."""
    return 0.7 * t + 0.3 * (t * t * (3 - 2 * t))


def crop_box(W, H, aspect, cx, cy, z):
    """Largest crop of `aspect` that fits the image, scaled by z, centred on
    (cx, cy) and clamped so it never runs off an edge."""
    if W / H > aspect:
        max_h, max_w = H, H * aspect
    else:
        max_w, max_h = W, W / aspect
    w, h = max_w * z, max_h * z
    x = min(max(cx * W - w / 2, 0.0), W - w)
    y = min(max(cy * H - h / 2, 0.0), H - h)
    return x, y, w, h


def render(job):
    key, fmt = job
    shot = SHOTS[key]
    aspect, ow, oh = FORMATS[fmt]
    path = f"{OUT}/clips-{fmt}/{key}.mp4"

    im = Image.open(os.path.join(SRC, key + ".jpg")).convert("RGB")
    W, H = im.size
    n = int(round(DUR * FPS))
    a, b = shot["a"], shot["b"]

    p = subprocess.Popen(
        [FFMPEG, "-y", "-loglevel", "error",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{ow}x{oh}", "-r", str(FPS), "-i", "-",
         "-vf", "eq=contrast=1.04:saturation=1.07,unsharp=5:5:0.25:5:5:0.0"]
        + ENC + [path], stdin=subprocess.PIPE)

    for i in range(n):
        t = ease(i / (n - 1))
        cx = a["cx"] + (b["cx"] - a["cx"]) * t
        cy = a["cy"] + (b["cy"] - a["cy"]) * t
        z = a["z"] + (b["z"] - a["z"]) * t
        x, y, w, h = crop_box(W, H, aspect, cx, cy, z)
        # AFFINE maps output pixel -> input pixel, so the move is sub-pixel exact.
        p.stdin.write(im.transform((ow, oh), Image.AFFINE,
                                   (w / ow, 0, x, 0, h / oh, y),
                                   resample=Image.BICUBIC).tobytes())
    p.stdin.close()
    if p.wait() != 0:
        raise RuntimeError(f"ffmpeg failed on {path}")
    return path


def assemble(keys, fmt, path):
    clips = [f"{OUT}/clips-{fmt}/{k}.mp4" for k in keys]
    args, filt, prev, offset = [], [], "0:v", 0.0
    for c in clips:
        args += ["-i", c]
    for i in range(1, len(clips)):
        offset += DUR - XFADE
        filt.append(f"[{prev}][{i}:v]xfade=transition=fade:"
                    f"duration={XFADE}:offset={offset:.3f}[x{i}]")
        prev = f"x{i}"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error"] + args +
                   ["-filter_complex", ";".join(filt), "-map", f"[{prev}]"] +
                   ENC + ["-r", str(FPS), path], check=True)
    return path


if __name__ == "__main__":
    for fmt in FORMATS:
        os.makedirs(f"{OUT}/clips-{fmt}", exist_ok=True)
    jobs = [(k, f) for f in FORMATS for k in ORDER]
    with Pool(4) as pool:
        for done in pool.imap_unordered(render, jobs):
            print("clip  ", done, flush=True)
    for fmt in FORMATS:
        print("REEL  ", assemble(ORDER, fmt, f"{OUT}/doucet-full-tour-{fmt}.mp4"), flush=True)
    print("REEL  ", assemble(SHORT, "vertical", f"{OUT}/doucet-short-cut-vertical.mp4"), flush=True)
