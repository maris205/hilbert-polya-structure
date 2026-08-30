#!/usr/bin/env python3
"""Run the two independent exact controls shipped with P122."""

import fibre_verify
import image_automaton


def main():
    fibre_verify.main()
    image_automaton.main()
    print(
        "combined_assertions="
        f"{fibre_verify.ASSERTIONS + image_automaton.ASSERTIONS}"
    )


if __name__ == "__main__":
    main()
