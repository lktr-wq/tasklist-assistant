#!/usr/bin/env python3
"""Day2 learning task list assistant."""

from __future__ import annotations

import argparse
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path


STATE_FILE = Path(__file__).with_name(".submitted_tasks.txt")


@dataclass(frozen=True)
class Task:
    name: str
    description: str
    acceptance: tuple[str, ...]
    suggestions: tuple[str, ...]


TASKS: tuple[Task, ...] = (
    Task(
        name="spec.md",
        description="说明工具目标、非目标、边界条件和验收标准。",
        acceptance=(
            "目标覆盖 today、submit、check 三个命令的输入输出",
            "非目标不少于 2 条",
            "边界条件不少于 3 条，包含重复 submit 的提示",
            "验收标准不少于 2 条，且可通过命令检查",
        ),
        suggestions=(
            "先写用户可见行为，再写异常处理",
            "验收标准尽量写成可运行命令或可观察输出",
        ),
    ),
    Task(
        name="plan.md",
        description="说明模块划分、数据结构、命令流程和风险。",
        acceptance=(
            "模块不少于 2 个",
            "包含任务数据结构和提交状态结构",
            "风险不少于 1 条",
        ),
        suggestions=(
            "把命令解析、任务数据、状态读写分开描述",
            "说明为什么选择轻量本地状态文件",
        ),
    ),
    Task(
        name="tasks.md",
        description="拆解每一步开发任务、产出和验收方式。",
        acceptance=(
            "步骤不少于 3 步",
            "每一步都有明确产出",
            "每一步都有验收方式",
        ),
        suggestions=(
            "按文档、实现、验收、备份顺序拆分",
            "每个验收方式都要能判断是否完成",
        ),
    ),
    Task(
        name="AGENTS.md",
        description="说明 Agent 和用户如何调用命令，以及失败处理策略。",
        acceptance=(
            "包含 today、submit、check 三个命令清单",
            "说明 submit 使用任务名字，不使用任务序号",
            "包含范围外拒答和工具失败处理",
        ),
        suggestions=(
            "把示例命令写完整",
            "提醒用户任务名必须来自 today 输出",
        ),
    ),
    Task(
        name="cli.py",
        description="按文档实现 Day2 学习任务清单助手。",
        acceptance=(
            "today 输出 5 个明确文件任务",
            "submit 只接收任务名字，并能识别重复提交",
            "check 不接收参数，输出已提交任务名字并用空格分隔",
        ),
        suggestions=(
            "使用 argparse 保持命令帮助清晰",
            "用本地状态文件保存已提交任务，便于跨命令检查",
        ),
    ),
)


def task_names() -> tuple[str, ...]:
    return tuple(task.name for task in TASKS)


def find_task(name: str) -> Task | None:
    normalized = name.strip()
    for task in TASKS:
        if task.name == normalized:
            return task
    return None


def load_submitted() -> list[str]:
    if not STATE_FILE.exists():
        return []
    submitted: list[str] = []
    valid_names = set(task_names())
    for line in STATE_FILE.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if name in valid_names and name not in submitted:
            submitted.append(name)
    return submitted


def save_submitted(names: list[str]) -> None:
    STATE_FILE.write_text("\n".join(names) + ("\n" if names else ""), encoding="utf-8")


def print_task(task: Task) -> None:
    print(task.name)
    print(f"    说明: {task.description}")
    print("    验收:")
    for item in task.acceptance:
        print(f"      - {item}")


def handle_today(_: argparse.Namespace) -> int:
    print("Day2 学习任务清单助手 - 今日任务")
    print("=" * 42)
    for index, task in enumerate(TASKS):
        if index:
            print()
        print_task(task)
    return 0


def handle_submit(args: argparse.Namespace) -> int:
    task = find_task(args.task_name)
    if task is None:
        print(
            f"错误: 不存在任务 `{args.task_name}`。可提交任务: {' '.join(task_names())}",
            file=sys.stderr,
        )
        return 2

    submitted = load_submitted()
    if task.name in submitted:
        print(f"提示: `{task.name}` 已提交过，无需重复提交。")
        return 0

    submitted.append(task.name)
    save_submitted(submitted)
    print(f"提交成功: {task.name}")
    print("当前已提交任务:")
    print(" ".join(submitted))
    return 0


def handle_check(_: argparse.Namespace) -> int:
    submitted = load_submitted()
    if not submitted:
        print("暂无已提交任务")
        return 0
    print(" ".join(submitted))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="Day2 学习任务清单助手",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            示例:
              python cli.py today
              python cli.py submit spec.md
              python cli.py check
            """
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    today = subparsers.add_parser("today", help="查看今日学习任务")
    today.set_defaults(func=handle_today)

    submit = subparsers.add_parser("submit", help="按任务名字提交完成项")
    submit.add_argument("task_name", help="任务名字，例如 spec.md")
    submit.set_defaults(func=handle_submit)

    check = subparsers.add_parser("check", help="查看当前已提交任务")
    check.set_defaults(func=handle_check)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
