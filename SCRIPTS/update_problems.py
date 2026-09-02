from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT_DIR = Path(__file__).resolve().parent.parent
README_FILE = ROOT_DIR / "README.md"
TOPICS_DIR = ROOT_DIR / "TOPICS"

START = "<!-- PROBLEMS-START -->"
END = "<!-- PROBLEMS-END -->"


def parse_problem_name(name: str) -> tuple[int, str] | None:
    """Parse names such as 100_The_3n_plus_1_problem."""
    match = re.match(r"^(\d+)(?:[_ -]+(.+))?$", name)
    if not match:
        return None

    problem_id = int(match.group(1))
    raw_title = match.group(2) or f"Problem {problem_id}"
    title = re.sub(r"[_-]+", " ", raw_title).strip()
    return problem_id, title


def markdown_link(label: str, path: Path) -> str:
    relative_path = path.relative_to(ROOT_DIR).as_posix()
    return f"[{label}]({quote(relative_path, safe='/')})"


def is_solution_file(path: Path) -> bool:
    """Accept normal .py files and existing extensionless UVa solution files."""
    return path.is_file() and not path.name.startswith(".") and path.suffix in {"", ".py"}


def replace_section(readme: str, section: str) -> str:
    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL
    )
    if pattern.search(readme):
        return pattern.sub(section, readme)
    return readme.rstrip() + "\n\n" + section + "\n"


def main() -> None:
    problems: dict[int, list[tuple[str, str, Path]]] = defaultdict(list)
    titles: dict[int, str] = {}

    if TOPICS_DIR.exists():
        for topic_dir in sorted(path for path in TOPICS_DIR.iterdir() if path.is_dir()):
            for item in sorted(topic_dir.iterdir()):
                parsed = parse_problem_name(item.stem if item.is_file() else item.name)
                if not parsed:
                    continue

                problem_id, title = parsed
                titles.setdefault(problem_id, title)

                if is_solution_file(item):
                    problems[problem_id].append((topic_dir.name, "Python", item))
                elif item.is_dir():
                    for solution in sorted(item.iterdir()):
                        if not is_solution_file(solution) or solution.name.startswith("_"):
                            continue
                        method = solution.stem.replace("_", " ")
                        problems[problem_id].append((topic_dir.name, method, solution))

    lines = [
        START,
        "| # | Title | Volume | Topics | Solution |",
        "|---:|---|---|---|---|",
    ]

    for problem_id in sorted(problems):
        entries = problems[problem_id]
        topics = sorted({entry[0] for entry in entries})
        topic_links = " / ".join(
            markdown_link(topic, TOPICS_DIR / topic) for topic in topics
        )

        solutions: list[str] = []
        seen: set[Path] = set()
        for _, method, path in entries:
            if path in seen:
                continue
            seen.add(path)
            solutions.append(markdown_link(method, path))

        title = titles[problem_id]
        statement_url = (
            f"https://onlinejudge.org/external/{problem_id // 100}/{problem_id}.pdf"
        )
        volume = f"Volume {problem_id // 100}"
        lines.append(
            f"| {problem_id} | [{title}]({statement_url}) | {volume} | "
            f"{topic_links} | {' / '.join(solutions)} |"
        )

    lines.append(END)
    section = "\n".join(lines)

    readme = README_FILE.read_text(encoding="utf-8")
    README_FILE.write_text(replace_section(readme, section), encoding="utf-8")
    print(f"Updated problem list: {len(problems)} solved problem(s).")


if __name__ == "__main__":
    main()
