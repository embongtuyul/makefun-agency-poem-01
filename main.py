import os

POEM = """The Bargain

My grandmother buys her chilies from Ibu Sari,
at the third stall past the fish,
where the floor is always wet,
and the air smells of lime and rain.

She holds each chili up to the light,
presses the stem with her thumb,
asks the price she already knows,
and shakes her head like it is news.

Then she offers half, and Ibu Sari laughs,
and they haggle over nothing,
two old women who have done this
every Saturday for forty years.

The agent does it better now. It orders
the same chilies at the lowest price,
never speaks, never waits, never gets it wrong.
It was perfect. That was the problem.

So on Saturdays I walk with her to the stall.
She offers half. Ibu Sari laughs, refuses,
then slips three extra chilies into the bag,
not for the price. For the asking.
My grandmother counts her change twice.

The agent waits in my pocket, silent.
It could have done this in a second.
I let it wait.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
