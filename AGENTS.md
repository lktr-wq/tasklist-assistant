# Day2 学习任务清单助手 Agent 指南

## 可用命令
- `python cli.py today`：查看今日全部文件任务。
- `python cli.py submit <任务名字>`：提交某个文件任务，例如 `python cli.py submit spec.md`。
- `python cli.py check`：查看当前已提交任务；多个任务名字用空格分隔。

## 用户如何提问或调用
- 想知道今天要提交哪些文件时，运行 `python cli.py today`。
- 完成某个文件后，运行类似 `python cli.py submit spec.md`。
- 想查看当前已经提交了哪些任务时，运行 `python cli.py check`。
- 如果不知道任务名字，先运行 `today`，再复制其中的任务名字提交。

## 范围外拒答
- 如果用户要求提交未在 `today` 中列出的任务，应说明当前工具只覆盖 `spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py`。
- 如果用户要求执行危险操作、删除文件或修改系统配置，应拒绝，并建议只运行本项目提供的三个安全命令。
- 如果用户要求把提交内容上传到外部服务，应说明本版本不连接外部 API。

## 工具失败处理
- 如果 Python 命令不可用，先尝试 `py cli.py today` 或检查 Python 是否已安装。
- 如果任务名字不存在，提示用户运行 `python cli.py today` 查看有效任务名字。
- 如果重复提交同一个任务，提示该任务已提交过，无需重复提交。
- 如果 `check` 没有输出任务名或显示暂无已提交任务，说明当前还没有成功提交记录。
- 如果 git 推送失败，先检查远程地址、网络和 GitHub 登录状态，再重新执行推送。
