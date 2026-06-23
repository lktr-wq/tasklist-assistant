# Day2 学习任务清单助手 Spec

## 目标
- 提供一个零依赖 Python CLI，帮助学习者查看 Day2 需要提交的文件任务。
- 支持 `today`、`submit`、`check` 三个命令的输入输出。
- `today` 输出明确任务清单：`spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py`。
- `submit` 只接收任务名字，不接收任务序号。
- `check` 不接收参数，直接返回当前已提交任务名字，并用空格分隔。

## 非目标
- 不实现用户登录、多人协作或权限系统。
- 不连接远程学习平台、数据库或外部 API。
- 不检查文件内容是否真的满足课程全部质量标准，只提供任务提交状态辅助。

## 边界条件
- 当 `submit` 的任务名字不在今日任务清单中时，返回清晰错误，并提示可提交任务名字。
- 当 `submit` 的任务已经提交过时，返回“已提交过，无需重复提交”的对应提示信息。
- 当 `check` 尚无提交记录时，返回“暂无已提交任务”。
- 当命令缺少参数或命令未知时，展示 argparse 提供的用法提示。

## 验收标准
- 运行 `python cli.py today` 能看到 `spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py` 五个任务。
- 运行 `python cli.py submit spec.md` 能看到 `spec.md` 提交成功。
- 再次运行 `python cli.py submit spec.md` 能看到已提交过的提示信息。
- 运行 `python cli.py check` 能看到当前已提交任务名字，多个任务用空格分隔。
- 运行 `python cli.py submit unknown.md` 返回不存在该任务的错误信息。
