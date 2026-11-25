"""Entry for make.fun: Two Lines to Your Past Self."""
import os

# Entry text: 239 characters (limit 280), 2 line(s), no trailing newline.
ENTRY = 'Do not skip the audition on the rainy Tuesday in March — the room is half empty and the judges are actually listening.\nThat one yes would have put you on stage a year earlier, and every late start since traces back to that one missed door.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
