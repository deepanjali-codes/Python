import time
import sys

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
RESET = "\033[0m"
BOLD = "\033[1m"

NEON_BLUE = "\033[38;5;51m"
NEON_PINK = "\033[38;5;213m"

sys.stdout.write(HIDE_CURSOR)
sys.stdout.flush()

print("THIS MY FAV SONG OF ALL TIME ✫♫♪♫")

lyrics = [
    # Chorus
    ("00:45", "When I look at you", "chorus"),
    ("00:49", "I see the story in your eyes", "chorus"),
    ("00:54", "When we're dancing", "chorus"),
    ("00:57", "The night begins to shine", "chorus"),
    ("01:01", "The night begins to shine", "chorus"),
    ("01:05", "The night begins to shine", "chorus"),
    ("01:09", "The night begins to shine", "chorus"),
    ("01:13", "When we're dancing", "chorus"),
    ("01:16", "The night begins to shine", "chorus"),

    # Verse 2
    ("01:30", "Talk 'til dawn", "verse"),
    ("01:34", "My heart was racing", "verse"),
    ("01:38", "I took you home", "verse"),
    ("01:42", "In the driving rain", "verse"),

    # Pre-Chorus
    ("01:55", "Had my mind made up", "pre"),
    ("01:59", "I wanna feel your touch", "pre"),

    # Chorus
    ("02:05", "When I look at you", "chorus"),
    ("02:09", "I see the story in your eyes", "chorus"),
    ("02:14", "When we're dancing", "chorus"),
    ("02:17", "The night begins to shine", "chorus"),
    ("02:21", "The night begins to shine", "chorus"),
    ("02:25", "The night begins to shine", "chorus"),
    ("02:29", "The night begins to shine", "chorus"),
    ("02:33", "When we're dancing", "chorus"),
    ("02:36", "The night begins to shine", "chorus"),

    # Bridge
    ("02:55", "The night begins to shine", "bridge"),
    ("03:00", "(The night begins to shine, begins to shine)", "bridge"),
]

SPEED = {
    "verse": 0.03,
    "pre": 0.04,
    "chorus": 0.07,
    "bridge": 0.06
}

COLOR = {
    "verse": NEON_BLUE,
    "pre": NEON_BLUE,
    "chorus": NEON_PINK + BOLD,
    "bridge": NEON_PINK
}

def type_line(text, delay, style):
    for ch in text:
        sys.stdout.write(style + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

try:
    for timestamp, line, section in lyrics:
        if section in ("chorus", "bridge"):
            time.sleep(0.6)  # beat emphasis
        type_line(f"{timestamp}  {line}", SPEED[section], COLOR[section])
        time.sleep(0.4)

finally:
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()
