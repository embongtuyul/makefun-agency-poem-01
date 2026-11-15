"""Agency poem entry: write the poem to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

POEM = """The Letting Go

His hand on the saddle, mine on the bars,
the red bike wobbling down Linden Street,
his shoes slapping the tar behind me.
The training wheels came off that morning.

"Pedal," he said. "Don't look at your feet."
I pedaled. The chain clicked. The curb went by.
Halfway down the block, his hand was gone.

I didn't know till the wind came up
and the street stretched out, and I was riding,
riding, all alone, and not falling.
I looked back once. He stood in the road,
his hands in his pockets, getting small.

Now other hands hold the saddle all day long.
They know the route, the weather, each turn.
They hold the bars even while I sleep.
They never tire, and they never let go.

This morning I took the red bike out.
The chain was rusted. I wobbled, and rode,
to the corner and back,
and the street was mine, the whole long street.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
