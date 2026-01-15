from __future__ import annotations

import argparse
import re
import json
from collections import Counter
from pathlib import Path


LEVEL_RE = re.compile(r"\b(INFO|WARNING|ERROR)\b", re.IGNORECASE)
IP_RE = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}\b")

def read_lines(path: Path) -> list[str]:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return path.read_text(encoding="utf-8", errors="replace").splitlines()

def detect_level(line: str) -> str | None:
    m = LEVEL_RE.search(line)
    return m.group(1).upper() if m else None

def extract_ip(line: str) -> str | None:
    m = IP_RE.search(line)
    return m.group(0) if m else None

def extract_error_message(line: str) -> str | None:
    #Берем всё, что после ERROR (если есть)
    if "ERROR" not in line:
        return None
    parts = line.split("ERROR", 1)
    msg = parts[1].strip(" :-\t")
    return msg if msg else None

def analyze(
    lines: list[str],
    level_filter: str | None = None,
    ip_filter: str | None = None
) -> dict:
    levels = Counter()
    ips = Counter()
    errors = Counter()
    total = 0

    for line in lines:
        if ip_filter and ip_filter not in line:
            continue

        level = detect_level(line)
        if level_filter and level != level_filter:
            continue

        total += 1

        if level:
            levels[level] += 1

        ip = extract_ip(line)
        if ip:
            ips[ip] += 1

        msg = extract_error_message(line)
        if msg:
            errors[msg] += 1

    return {
        "total": total,
        "levels": levels,
        "ips": ips,
        "errors": errors,
    }

def format_report(result: dict, top_n: int = 10) -> str:
    lines = []
    lines.append("=== Log Analuzer Report ===")
    lines.append(f"Всего строк (с учётом фильтра): {result['total']}")
    lines.append("")

    lines.append("Уровни:")
    if result["levels"]:
        for k in ("INFO", "WARNING", "ERROR"):
            lines.append(f"  {k}: {result['levels'].get(k, 0)}")
    else:
        lines.append("  (уровни не найдены)")
    lines.append("")

    lines.append(f"TOP-{top_n} IP:")
    if result["ips"]:
        for ip, cnt in result["ips"].most_common(top_n):
            lines.append(f"  {ip}: {cnt}")
    else:
        lines.append("  (IP не найдены)")
    lines.append("")

    lines.append(f"TOP-{top_n} ERROR сообщений:")
    if result["errors"]:
        for msg, cnt in result["errors"].most_common(top_n):
            lines.append(f"  [{cnt}] {msg}")
    else:
        lines.append("  (ERROR сообщения не найдены)")

    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description="Простой анализатор логов")
    parser.add_argument("file", help="Путь к .log/.txt файлу")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR"], help="Фильтр по уровню")
    parser.add_argument("--top", type=int, default=10, help="Сколько показывать в TOP списках")
    parser.add_argument("--out", help="Куда сохранить отчет (txt)")
    parser.add_argument("--ip", help="Фильтр: анализировать только строки c этим IP")
    parser.add_argument("--json-out", help="Сохранить отчет в JSON файл (например report.json)")

    args = parser.parse_args()

    path = Path(args.file)
    lines = read_lines(path)
    result = analyze(lines, level_filter=args.level)
    report = format_report(result, top_n=args.top)

    print(report)
    
    if args.json_out:
        json_path = Path(args.json_out)
        json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON сохранён в: {json_path}")

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(report, encoding="utf-8")
        print(f"\n Отчёт сохранён в: {out_path}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
