#!/usr/bin/env python3
"""Day2 learning task list assistant."""

from __future__ import annotations

import argparse
import sys
import textwrap
from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    task_id: int
    title: str
    description: str
    acceptance: tuple[str, ...]
    suggestions: tuple[str, ...]


TASKS: tuple[Task, ...] = (
    Task(
        task_id=1,
        title="阅读 Day2 学习材料",
        description="完成指定章节阅读，提炼关键概念和不理解的问题。",
        acceptance=(
            "写出不少于 3 条关键概念",
            "记录至少 1 个需要追问的问题",
            "能用自己的话说明今天学习目标",
        ),
        suggestions=(
            "先扫目录，再逐段记录关键词",
            "把不确定的地方标成问题，留到复盘时处理",
        ),
    ),
    Task(
        task_id=2,
        title="完成 Spec Coding 练习",
        description="围绕一个小工具编写 spec、plan、tasks 和 agent 说明。",
        acceptance=(
            "spec.md 包含目标、非目标、边界条件、验收标准",
            "plan.md 包含模块划分、数据结构和风险",
            "tasks.md 每一步都有产出和验收方式",
        ),
        suggestions=(
            "先写用户能看到的行为，再补内部实现",
            "每个验收点都尽量可运行或可检查",
        ),
    ),
    Task(
        task_id=3,
        title="运行并检查 CLI",
        description="使用 today、submit、check 三个命令验证工具可用性。",
        acceptance=(
            "today 能列出全部任务",
            "submit 能接受合法任务编号和提交内容",
            "check 能输出对应任务的验收项",
        ),
        suggestions=(
            "先跑正常路径，再跑缺参和错误编号",
            "记录命令输出，作为最终提交说明的一部分",
        ),
    ),
)


def find_task(task_id: int) -> Task | None:
    for task in TASKS:
        if task.task_id == task_id:
            return task
    return None


def print_task(task: Task) -> None:
    print(f"[{task.task_id}] {task.title}")
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
    task = find_task(args.task_id)
    if task is None:
        print(f"错误: 不存在编号为 {args.task_id} 的任务。请运行 `python cli.py today` 查看任务清单。", file=sys.stderr)
        return 2

    content = args.content.strip()
    if not content:
        print("错误: 提交内容不能为空。", file=sys.stderr)
        return 2

    print("提交成功")
    print(f"任务: [{task.task_id}] {task.title}")
    print(f"内容: {content}")
    print("下一步: 运行 `python cli.py check {}` 对照验收项自查。".format(task.task_id))
    return 0


def handle_check(args: argparse.Namespace) -> int:
    task = find_task(args.task_id)
    if task is None:
        print(f"错误: 不存在编号为 {args.task_id} 的任务。请运行 `python cli.py today` 查看任务清单。", file=sys.stderr)
        return 2

    print(f"任务检查: [{task.task_id}] {task.title}")
    print("=" * 42)
    print("验收项:")
    for item in task.acceptance:
        print(f"  [ ] {item}")
    print()
    print("完成建议:")
    for item in task.suggestions:
        print(f"  - {item}")
    print()
    print("检查结果: 请逐项确认，全部满足后即可视为完成。")
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
              python cli.py submit 1 "完成阅读并整理笔记"
              python cli.py check 1
            """
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    today = subparsers.add_parser("today", help="查看今日学习任务")
    today.set_defaults(func=handle_today)

    submit = subparsers.add_parser("submit", help="提交某个任务的完成说明")
    submit.add_argument("task_id", type=int, help="任务编号")
    submit.add_argument("content", help="提交内容")
    submit.set_defaults(func=handle_submit)

    check = subparsers.add_parser("check", help="查看某个任务的验收清单")
    check.add_argument("task_id", type=int, help="任务编号")
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
