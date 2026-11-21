#!/usr/bin/env python3
"""Write a short poem about permission to the make.fun entry file."""

import os

POEM = """I learned to knock before I learned to count —
three taps on the blue door, then wait,
because a door is only a wall until someone is listening.

My grandmother kept the spare key in a chipped teacup,
not hidden, just placed — the way trust is placed —
where any hand could find it, and only the right hand would.

To ask is to hold out an empty palm
and let the answer belong to someone else.
To be asked is to feel the gate's weight shift to your hands:
how heavy a yes can be, how clean a no.

The boy next door asked for mangoes, not mercy.
Take the ripe ones, I said, but leave the tree its future.
He left two on my step anyway —
a small tax on being let in.

Now I stand on both sides of every door I own.
I practice saying come in the way weather changes a room.
I practice hearing not yet, and not mistaking it for never.

So ask. The worst the world can give you is a closed door,
and a closed door, at least, tells the truth about where you stand —
outside, still whole, still holding the key to your own asking.
"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
