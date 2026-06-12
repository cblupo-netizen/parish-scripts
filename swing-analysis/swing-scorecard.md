# Rec-League Swing Scorecard (v0 — manual)

A hand-analysis checklist for adult rec-league hitters with no coach. You watch a
swing video against this list, mark what you see, and hand the hitter 1–3 things
to work on plus a drill for each.

This is deliberately **low-tech**. Use it by eye first. It also doubles as the
spec for a future automated tool: every "What you see" cue below is something a
pose-estimation model can eventually measure, and every threshold is a number we
can tune against real swings.

> Honest caveat: this is a starting point built from widely-taught swing
> fundamentals, not gospel. Some items have rival coaching camps (rotational vs.
> linear). Treat thresholds as rough. Sanity-check against your own eyes and,
> ideally, one knowledgeable hitter on the team. The goal is **catch the big,
> obvious swing-killers** — not optimize a 2-degree attack angle.

---

## Step 0 — Film it right (this is the most important step)

Bad footage = useless analysis. Shoot **two angles** if you can:

- **Face-on (open side):** phone ~15 ft away, lens at about waist/hip height,
  directly to the side the hitter faces (1st-base side for a righty). Whole body
  + bat in frame through the whole swing. Best angle for: stride, weight shift,
  posture, head movement, hip/shoulder sequence.
- **Behind (catcher's view):** phone directly behind the hitter, safely off to
  the side, same height. Best angle for: bat path, casting, swing plane,
  stepping in the bucket.
- **Slow-mo ON** if the phone has it (240fps ideal). Contact happens in
  milliseconds — at 30fps you get ~3 blurry frames and can't judge much.
- Same setup every time so swings are comparable week to week.

If the video doesn't clearly show the body and bat from one of these angles,
**don't analyze it** — refilm. Garbage in, garbage out.

---

## The 6 swing-killers

For each: what it is, the visual tell, the angle that shows it, a quick check,
the cue, and a drill or two. Score each **OK / Minor / Major**.

### 1. Lunging / drifting (weight goes forward too early)
- **What:** Head and weight slide toward the pitcher before/through the swing.
  Kills power and gets the hitter fooled by off-speed.
- **You see (face-on):** Head visibly travels toward the pitcher from load to
  contact. Back leg straightens early; front side collapses.
- **Quick check:** Mark head position at load and at contact. More than ~a
  head's-width of forward drift = problem.
- **Cue:** "Stay back — let it come to you. Turn, don't lunge."
- **Drills:** Fence/wall stride-and-hold (stride, pause, then swing without
  drifting); hit off a tee with weight held back; one-handed top-hand tee work.

### 2. Casting / bat drag (hands get away from the body)
- **What:** Hands push out and away instead of staying tight, making a long,
  late, loopy swing. Classic "I'm always late on the fastball."
- **You see (behind):** Barrel and hands sweep out wide away from the body early;
  the path to the ball is long, not direct.
- **Quick check:** Does the knob lead down toward the ball with hands close to
  the body, or do the hands cast out first? Cast-first = problem.
- **Cue:** "Knob to the ball. Keep your hands inside."
- **Drills:** Towel/connection-ball under the lead armpit (keep it pinned through
  contact); inside-pitch tee work; two-tee drill (don't clip the outer tee).

### 3. Pulling off / flying open (front shoulder bails out)
- **What:** Front shoulder and head pull toward the dugout early, opening the
  body too soon. Causes rollover grounders to the pull side and weak contact away.
- **You see (face-on):** Front shoulder flies open before contact; head pulls
  off the ball; chest faces the pitcher way too early.
- **Quick check:** Is the front shoulder still pointed roughly at the pitcher at
  launch, or already rotated open? Early open = problem.
- **Cue:** "Stay closed, see it deep, hit it back up the middle."
- **Drills:** Opposite-field tee/soft-toss (drive everything to the off-field
  gap); ball-on-tee at contact point set back deeper; "show the logo" — keep
  chest closed until the hands go.

### 4. No load / no separation (no coil, no rhythm)
- **What:** Hitter starts dead-still and just arms the ball. No gather, no
  hip-shoulder separation = no stored power, everything is upper body.
- **You see (face-on):** No small "negative move" / hands going back as the
  stride goes forward; no separation between hips firing and shoulders following.
- **Quick check:** Is there a visible gather/coil before the swing, with hands
  back as the front foot goes down? If hitter is statue-still → problem.
- **Cue:** "Get a rhythm, gather, then go. Hips lead, hands follow."
- **Drills:** Toe-tap or small leg-kick timing drill; "hands back as foot goes
  down" rhythm reps; hip-turn-first dry swings feeling the stretch.

### 5. Stepping in the bucket (stride foot lands open / away from plate)
- **What:** Front foot strides toward the dugout instead of the pitcher, pulling
  the body off the plate. Can't cover the outside pitch; chronic pull-side weak
  contact.
- **You see (behind or face-on):** Stride foot lands clearly toward 3rd-base
  dugout (for a righty), not at the pitcher.
- **Quick check:** Draw the stride direction. Pointing toward the pitcher = OK.
  Pointing toward the dugout = problem.
- **Cue:** "Stride to the pitcher, not away from it."
- **Drills:** Stride into a bat/object laid on the ground as a guide; closed-toe
  stride drill against a wall; slow walk-up swings landing toward the mound.

### 6. Steep / long bat path (chopping or uppercutting badly)
- **What:** Bat comes in too steep (chopping down) or way too uphill (big
  uppercut), instead of working on-plane to the pitch. Lots of swing-and-miss or
  weak pop-ups / topped balls.
- **You see (behind):** Barrel drops way under and loops up, or chops steeply
  down across the plane, instead of matching the pitch path.
- **Quick check:** Does the barrel get on-plane behind the ball and stay through
  the zone, or is it one steep angle? Steep either way = problem.
- **Cue:** "Match the plane. Stay through the zone, not down or up at it."
- **Drills:** Two-tee path drill (low back tee, higher front tee — swing through
  both); high-tee/low-tee mix; bottom-hand-only path reps.

---

## How to use it (the Wizard-of-Oz workflow)

1. Get 1–2 clean clips from a teammate (Step 0 angles).
2. Watch each killer one at a time, scrubbing slow. Mark **OK / Minor / Major**.
3. Pick the **top 1–3 Majors** only. Do not dump all six on someone — they'll
   quit. One thing at a time.
4. Send them: what you saw (plain language) + the cue + one drill.
5. Refilm in 2–3 weeks. Did the score move? That's your proof the advice works —
   or your signal a rule/threshold is wrong.

If your handwritten notes don't help your own teammates get better, no amount of
AI will. If they do help, you now have validated rules to encode — and proof the
thing is worth building.

---

## Scorecard (copy per hitter / per session)

| Swing-killer            | Angle    | Score (OK/Minor/Major) | Notes |
|-------------------------|----------|------------------------|-------|
| 1. Lunging / drifting   | Face-on  |                        |       |
| 2. Casting / bat drag   | Behind   |                        |       |
| 3. Pulling off / open   | Face-on  |                        |       |
| 4. No load / separation | Face-on  |                        |       |
| 5. Stepping in bucket   | Behind   |                        |       |
| 6. Steep / long path    | Behind   |                        |       |

**Top 1–3 to work on:** ______________________________________________

**Drills assigned:** ________________________________________________

**Refilm by:** _____________
