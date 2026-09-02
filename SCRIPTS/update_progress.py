from __future__ import annotations

import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
README_FILE = ROOT_DIR / "README.md"
TOPICS_DIR = ROOT_DIR / "TOPICS"

START = "<!-- PROGRESS-START -->"
END = "<!-- PROGRESS-END -->"


def main() -> None:
    problem_ids: set[int] = set()

    if TOPICS_DIR.exists():
        for solution in TOPICS_DIR.glob("*/*/*.py"):
            if solution.name.startswith("_"):
                continue
            match = re.match(r"^(\d+)", solution.parent.name)
            if match:
                problem_ids.add(int(match.group(1)))

    section = f"{START}\n✅ Solved: {len(problem_ids)}\n{END}"
    readme = README_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL
    )

    if pattern.search(readme):
        readme = pattern.sub(section, readme)
    else:
        readme = readme.rstrip() + "\n\n" + section + "\n"

    README_FILE.write_text(readme, encoding="utf-8")
    print(f"Updated progress: {len(problem_ids)} solved problem(s).")


if __name__ == "__main__":
    main()
