# Day2 学习任务清单助手 Plan

## 模块划分
- 命令解析模块：使用 `argparse` 注册 `today`、`submit`、`check` 三个子命令，并把请求分发到对应处理函数。
- 任务数据模块：使用 `Task` 数据类和内置 `TASKS` 元组保存五个明确文件任务。
- 状态读写模块：使用项目目录下的 `.submitted_tasks.txt` 保存已提交任务名字，用于重复提交判断和 `check` 输出。
- 输出处理模块：统一格式化任务清单、提交结果、重复提交提示和检查结果。

## 数据结构
- `Task.name`：任务名字，固定为 `spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py` 之一。
- `Task.description`：任务说明，帮助用户理解该文件需要完成什么。
- `Task.acceptance`：验收项元组，用于 `today` 输出。
- `Task.suggestions`：完成建议元组，用于扩展说明。
- `.submitted_tasks.txt`：每行一个已提交任务名字，按提交顺序保存。

## 命令流程
- `today`：遍历五个内置文件任务，输出任务名字、说明和验收项。
- `submit <task_name>`：校验任务名字是否有效；若已提交则返回提示；否则写入状态文件并输出当前已提交任务。
- `check`：不接收参数，读取状态文件；无提交时输出“暂无已提交任务”，有提交时用空格输出任务名字。

## 风险
- 状态文件是本地轻量记录，如果被手动删除，`check` 将无法看到历史提交。
- Windows 终端编码如果不是 UTF-8，中文输出可能显示异常；建议使用 PowerShell 或支持 UTF-8 的终端运行。
