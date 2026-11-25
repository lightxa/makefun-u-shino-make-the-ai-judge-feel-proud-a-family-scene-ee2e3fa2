"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene to /output/entry.txt.

The scene is a single fixed text: a small domestic moment, warm,
funny and heartfelt, opened mid-moment and addressed to "you".
Pure standard library, deterministic, no network at runtime.
"""

import os

SCENE = (
    "You are asleep in my lap, one small hand still curled so tight around your bent spoon, the sea sighing past our open window, the night holding its breath right beside us, and I sit very still, afraid to wake the first night you finally learned to rest.\n"
    "You did it, love."
)


def check_scene(text):
    """Self-check the kit gate: UTF-8 text, 1 to 280 characters, not blank."""
    assert isinstance(text, str)
    assert text.strip(), "scene must not be only whitespace"
    assert 1 <= len(text) <= 280, "scene must be 1 to 280 characters"
    text.encode("utf-8")
    return True


def main():
    check_scene(SCENE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SCENE)
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    assert written == SCENE, "written file must match the scene exactly"
    check_scene(written)
    print(f"Wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
