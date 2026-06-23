# Day2 学习任务清单助手 Tasks

本文件是给 Agent 使用的执行清单。Agent 接手项目后，应先阅读本文件，再按顺序完成调试，不要跳过边界条件样例。

## 1. 准备干净调试状态
- 任务：删除本地运行状态，避免历史提交记录影响测试。
- 命令：`Remove-Item .submitted_tasks.txt -ErrorAction SilentlyContinue`
- 产出：项目目录中没有 `.submitted_tasks.txt`。
- 验收方式：运行 `python cli.py check` 时，应输出 `暂无已提交任务`。

## 2. 验证 today 的完整任务清单
- 任务：确认 `today` 返回明确的五个文件任务。
- 命令：`python cli.py today`
- 产出：输出任务清单。
- 验收方式：输出中必须包含 `spec.md`、`plan.md`、`tasks.md`、`AGENTS.md`、`cli.py`。

## 3. 验证 check 的空状态边界
- 任务：确认无提交记录时有清晰提示。
- 命令：`python cli.py check`
- 产出：空状态提示。
- 验收方式：输出必须是 `暂无已提交任务`。

## 4. 验证 submit 的正常路径
- 任务：用任务名字提交一个有效任务。
- 命令：`python cli.py submit spec.md`
- 产出：提交状态写入 `.submitted_tasks.txt`。
- 验收方式：输出包含 `提交成功: spec.md`，随后运行 `python cli.py check` 应输出 `spec.md`。

## 5. 验证重复 submit 的边界条件
- 任务：重复提交已提交过的任务。
- 命令：`python cli.py submit spec.md`
- 产出：重复提交提示。
- 验收方式：输出包含 `已提交过，无需重复提交`，且 `.submitted_tasks.txt` 中不应出现重复的 `spec.md`。

## 6. 验证多任务提交和 check 输出格式
- 任务：继续提交第二个任务并检查空格分隔格式。
- 命令：`python cli.py submit plan.md`，然后运行 `python cli.py check`
- 产出：已提交任务列表。
- 验收方式：`check` 输出必须是 `spec.md plan.md`。

## 7. 验证非法任务名
- 任务：提交不在 today 清单中的任务。
- 命令：`python cli.py submit unknown.md`
- 产出：错误提示。
- 验收方式：输出包含 `不存在任务`，并列出可提交任务 `spec.md plan.md tasks.md AGENTS.md cli.py`。

## 8. 验证缺少参数
- 任务：确认缺少 submit 参数时不会静默成功。
- 命令：`python cli.py submit`
- 产出：argparse 用法提示。
- 验收方式：输出说明缺少 `task_name`，命令返回非零状态。

## 9. 收尾
- 任务：清理调试生成物，保持提交内容干净。
- 命令：删除 `.submitted_tasks.txt` 和 `__pycache__`。
- 产出：只保留项目交付文件。
- 验收方式：`git status --short` 不应出现运行状态文件或 Python 缓存。
