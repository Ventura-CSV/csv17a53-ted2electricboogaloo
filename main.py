from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    # Your code here
    duplicate = {}

    for x, y in mapping.items():
        if y in duplicate:
            return ( duplicate[y], x )
        duplicate[y] = x
    pass
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    # Your code here
    values = set( mapping.values() )

    for i in target:
        if i not in values:
            return i
        
    return None
    pass
    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    t = int(x)

    if x >= 0 or x == t:
        return t
    else:
        return t - 1
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
