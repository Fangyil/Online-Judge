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
        for topic_dir in (path for path in TOPICS_DIR.iterdir() if path.is_dir()):
            for item in topic_dir.iterdir():
                if item.is_file() and item.suffix in {"", ".py"}:
                    match = re.match(r"^(\d+)", item.stem)
                    if match:
                        problem_ids.add(int(match.group(1)))
                elif item.is_dir() and any(
                    child.is_file()
                    and not child.name.startswith("_")
                    and child.suffix in {"", ".py"}
                    for child in item.iterdir()
                ):
                    match = re.match(r"^(\d+)", item.name)
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
