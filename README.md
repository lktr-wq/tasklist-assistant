# Day2 学习任务清单助手

这是一个零依赖 Python CLI 项目，用来辅助完成 Day2 作业要求中的 5 个交付文件：

- `spec.md`
- `plan.md`
- `tasks.md`
- `AGENTS.md`
- `cli.py`

工具提供三个命令：`today` 查看任务清单，`submit` 按任务名字提交，`check` 查看当前已提交任务。

## 快速开始

```powershell
python cli.py today
python cli.py submit spec.md
python cli.py check
```

如果本机没有 `python` 命令，可以尝试：

```powershell
py cli.py today
```

## 人工审查应该跑的精选测试样例

以下样例覆盖了完整正确流程和关键边界条件。建议从一个干净状态开始，先删除本地运行状态文件：

```powershell
Remove-Item .submitted_tasks.txt -ErrorAction SilentlyContinue
```

1. 查看完整任务清单：

```powershell
python cli.py today
```

期望：输出包含 `spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py` 五个任务。

2. 检查尚未提交时的边界提示：

```powershell
python cli.py check
```

期望：输出 `暂无已提交任务`。

3. 正常提交一个任务：

```powershell
python cli.py submit spec.md
```

期望：输出 `提交成功: spec.md`，并显示当前已提交任务。

4. 重复提交同一个任务：

```powershell
python cli.py submit spec.md
```

期望：输出 `提示: spec.md 已提交过，无需重复提交。`

5. 提交第二个任务并检查空格分隔输出：

```powershell
python cli.py submit plan.md
python cli.py check
```

期望：`check` 输出 `spec.md plan.md`。

6. 提交不存在的任务：

```powershell
python cli.py submit unknown.md
```

期望：返回错误，并提示可提交任务为 `spec.md plan.md tasks.md AGENTS.md cli.py`。

7. 缺少参数：

```powershell
python cli.py submit
```

期望：argparse 输出用法提示，并说明缺少 `task_name`。

## 如果你是 Agent

请先自动打开 `tasks.md`，按照里面的调试指令顺序执行样例。`tasks.md` 是本项目的任务执行清单；如果审查说明中写作 `task.md`，在本仓库中对应文件就是 `tasks.md`。

执行时注意：

- 不要凭空推断任务名字，任务名字必须来自 `python cli.py today` 的输出。
- 调试前先删除 `.submitted_tasks.txt`，确保重复提交和空状态边界可复现。
- 跑完样例后删除 `.submitted_tasks.txt` 和 `__pycache__`，避免把本地运行状态当作交付文件。

## 项目文件说明

- `cli.py`：命令行实现。
- `spec.md`：需求、非目标、边界条件和验收标准。
- `plan.md`：模块设计、数据结构、命令流程和风险。
- `tasks.md`：给 Agent 和开发者使用的调试执行清单。
- `AGENTS.md`：Agent 使用规则、范围外拒答和工具失败处理。

## 状态文件

`submit` 会在本地生成 `.submitted_tasks.txt` 来保存已提交任务。该文件是运行状态，不是作业交付物，已经通过 `.gitignore` 忽略。
