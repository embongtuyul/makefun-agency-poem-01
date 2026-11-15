import os

POEM = """The First Loaf

My mother taught me bread the way her mother taught her:
flour on the counter, water by feel, salt from the palm.
She never measured. She said the dough would tell you.
I pressed it flat, folded it, pressed it again,
until it stopped sticking to my hands.

Now the kitchen does it while I sleep.
It weighs the flour to the gram. It warms the water.
It kneads for eleven minutes, rests the dough at twenty-six degrees.
It has never burned a loaf.
They come out brown, even, every time.

This morning I woke before the timer.
I took one piece of dough from the bowl
and shaped it the way my mother taught me:
pressed flat, folded, pressed again,
flour on my sleeves, dough under my nails.

My hands remembered before I did:
the heel of the palm, the turn, the tuck.
The loaf came out lopsided. The crust split.
It was the ugliest loaf on the table.
We ate it first.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
