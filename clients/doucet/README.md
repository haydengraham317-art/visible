# Doucet — 41 [street] hardscape project · social video pack

Thirteen stills from the completed front-and-back hardscape build, cut into
motion clips for Reels / TikTok / Shorts and feed posts.

Everything here is **clean** — no text, no logo, no music burned in. Add those
in CapCut so one render serves every platform and can be re-cut later.

---

## What's in the pack

Run `python3 render_clips.py out` to build (~4 min). Output lands in `out/`:

| File | Format | Length | Use |
|---|---|---|---|
| `doucet-short-cut-vertical.mp4` | 1080×1920 | 0:16 | **Lead with this.** Reels / TikTok / Shorts |
| `doucet-full-tour-vertical.mp4` | 1080×1920 | 0:40 | Full property tour — Reels, Stories, YouTube Shorts |
| `doucet-full-tour-square.mp4` | 1080×1080 | 0:40 | Feed post, LinkedIn |
| `clips-vertical/*.mp4` | 1080×1920 | 3.6s ×13 | **The CapCut building blocks** — re-order, trim, drop |
| `clips-square/*.mp4` | 1080×1080 | 3.6s ×13 | Same, square |

Each clip is one photo with a real camera move on it — a dolly in, a lateral
track along the wall, a drone-style pull-back. The moves are computed at
sub-pixel precision, so there's none of the stepping you get from a stock
"Ken Burns" preset.

## The edit

Front kerb appeal → craftsmanship detail → entry → backyard reveal → lifestyle
→ drone pull-out. It ends wide on purpose: the last thing a viewer sees is the
whole property, which is the thing that gets shared.

| # | Clip | In (full tour) | Move |
|---|---|---|---|
| 1 | `01-front-wall-hero` | 0:00 | Drift left along the wall coursing — **the hook** |
| 2 | `02-front-elevation` | 0:03 | Push in from the street, tilting up |
| 3 | `03-wall-detail` | 0:06 | Close on block coursing + planted trench |
| 4 | `04-entry-front` | 0:09 | Push in on door, steps, landing |
| 5 | `05-entry-patio` | 0:12 | Forward down the steps, as if walking out |
| 6 | `06-driveway-wall` | 0:15 | Travel right along the wall to the street |
| 7 | `07-drone-low` | 0:18 | Pull back, full frontage |
| 8 | `08-back-reveal` | 0:21 | **Front-to-back turn** — pull out across the lawn |
| 9 | `09-back-terrace` | 0:24 | Push in on the terrace wall and stair |
| 10 | `10-patio-dining` | 0:27 | Push in on the dining set |
| 11 | `11-patio-lounge` | 0:30 | Fire table → loungers, lateral drift |
| 12 | `12-drone-high` | 0:33 | Push in, house and terrace |
| 13 | `13-drone-wide` | 0:36 | Pull out, whole property — **the close** |

The 16s short cut is clips 1, 3, 4, 9, 11 — wall, detail, entry, terrace,
lifestyle. That's the sequence to test first; if it performs, post the full
tour as the follow-up.

## In CapCut

1. Import `clips-vertical/` — they're already 1080×1920, no reframing needed.
2. Drop music **from CapCut's own library**. This is a business account, so
   trending audio ripped from another post is a copyright strike risk on
   Facebook and a monetisation block on YouTube. CapCut's licensed tracks are
   cleared for commercial use.
3. Beat-match the cuts. Each clip is 3.6s; trim to land on the beat — around
   2.0–2.5s per clip is the pace that performs on Reels.
4. Text: one hook in the first 1.5s, one CTA at the end. Keep both inside the
   middle 80% of the frame or the UI will cover them.
5. Export 1080×1920, 30fps, "Higher" quality.

Don't add a filter — the clips already carry a light contrast and saturation
lift. Stacking a CapCut filter on top will clip the sky and blow out the
paving.

## Higgsfield

Worth it for **two shots**, not thirteen.

AI image-to-video warps straight lines, and this entire project is straight
lines — block coursing, step nosings, siding, rooflines. On most of these
photos it will bend the wall and you'll spend more time regenerating than the
shot is worth. The rendered clips are safer everywhere the geometry is the
subject.

Where it genuinely beats a camera move:

- **`11-patio-lounge`** — animating the fire table flame. That's motion a still
  can't fake and a Ken Burns move can't add.
- **`13-drone-wide`** / **`12-drone-high`** — a true drone pull-back with
  parallax, where the trees separate from the house. Slow moves only.

Feed the photo as the first frame, keep the clip at 5s, and generate 2–3 takes
— expect to bin one. Prompts:

> **11-patio-lounge** — Slow lateral glide left to right across the patio, past
> the fire table toward the loungers. Flames in the fire table flicker and dance
> realistically. All furniture, paving and siding remain perfectly rigid and
> unchanged. Subtle breeze in the umbrella fabric. No people, no camera shake.

> **13-drone-wide** — Slow aerial drone pull back and rise, revealing the whole
> property. Smooth steady motion, no rotation. Houses, roofs, driveway and
> retaining wall remain perfectly rigid with no warping or morphing. Trees sway
> gently in a light breeze, clouds drift slowly. No people, no moving vehicles.

> **09-back-terrace** — Slow dolly forward across the lawn toward the stone
> steps in the retaining wall. Treeline behind sways gently in the breeze. Wall
> and steps perfectly rigid, block coursing does not morph. No people.

The "remains perfectly rigid / no warping" clause is the important part — it's
what keeps the masonry from breathing. If your plan exposes camera presets, map
these to a slow **Dolly In**, a lateral **Robo Arm**, and a **Crane Up** /
drone reveal respectively.

Cut any Higgsfield take in as a straight replacement for the matching clip —
same slot, same length.

## Caption copy

Written out in [`captions.md`](captions.md) — Instagram and TikTok versions,
alternate hooks to rotate, which video goes to which platform, and the standing
contact block that runs under every post.

If there are **before** photos of this property, get them. A before/after on the
first frame will outperform everything here, and the wall shots make an
unusually strong pair.

## Regenerating

```bash
pip install pillow imageio-ffmpeg
python3 render_clips.py out
```

Camera moves live in the `SHOTS` dict in `render_clips.py` — `cx`/`cy` is where
the frame is centred (fraction of the image), `z` is how tight (1.0 widest).
`ORDER` is the full tour, `SHORT` is the 16s cut. Change `FORMATS` to add a
16:9 version for the website.

`out/` is gitignored — the renders are reproducible, so only the photos and the
script are tracked.
