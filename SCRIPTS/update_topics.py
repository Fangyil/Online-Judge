from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote


ROOT_DIR = Path(__file__).resolve().parent.parent
README_FILE = ROOT_DIR / "README.md"
TOPICS_DIR = ROOT_DIR / "TOPICS"

START = "<!-- TOPICS-START -->"
END = "<!-- TOPICS-END -->"


def main() -> None:
    topic_counts: list[tuple[str, int]] = []

    if TOPICS_DIR.exists():
        for topic_dir in sorted(path for path in TOPICS_DIR.iterdir() if path.is_dir()):
            problem_ids: set[int] = set()
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
            topic_counts.append((topic_dir.name, len(problem_ids)))

    lines = [START, "| Topic | Solved |", "|---|---:|"]
    for topic, count in topic_counts:
        label = topic.replace("_", " ")
        if count:
            path = quote(f"TOPICS/{topic}", safe="/")
            lines.append(f"| [{label}]({path}) | {count} |")
        else:
            lines.append(f"| {label} | {count} |")
    lines.append(END)

    section = "\n".join(lines)
    readme = README_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL
    )

    if pattern.search(readme):
        readme = pattern.sub(section, readme)
    else:
        readme = readme.rstrip() + "\n\n" + section + "\n"

    README_FILE.write_text(readme, encoding="utf-8")
    print(f"Updated topics: {len(topic_counts)} topic(s).")


if __name__ == "__main__":
    main()
