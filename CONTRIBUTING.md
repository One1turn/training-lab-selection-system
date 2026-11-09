# 团队协作指南

## 1. 首次获取项目

从远端克隆（推荐），或直接复制项目文件夹后重新绑定远端：

```bash
git clone <仓库地址>
cd training-lab-selection-system
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Windows
pip install -r backend\requirements.txt
python scripts\seed.py
```

本地已有代码、要接入远端时：

```bash
git remote add origin <仓库地址>
git remote -v
git push -u origin main
```

## 2. 分支约定

| 分支 | 用途 |
|---|---|
| `main` | 可演示、测试通过的稳定版本，禁止直接提交 |
| `feature/<模块>` | 新功能，如 `feature/appeal-workflow` |
| `fix/<问题>` | 缺陷修复，如 `fix/confirm-idempotent` |
| `docs/<主题>` | 文档与设计补充 |

## 3. 日常流程

```bash
git checkout main && git pull --ff-only
git checkout -b feature/<模块>

# 开发 + 自测
pytest backend/tests -q
ruff check backend/app backend/tests scripts

git add -A
git commit -m "feat(selection): 支持多轮补录顺位"
git push -u origin feature/<模块>
```

push 后在 GitHub 上发起 Pull Request，CI 通过且至少 1 人评审后合并。

## 4. 提交信息规范

采用 Conventional Commits：

- `feat:` 新功能
- `fix:` 缺陷修复
- `docs:` 文档
- `test:` 测试
- `refactor:` 重构（不改变行为）
- `chore:` 构建、依赖、脚本

示例：`feat(admin): 增加 dry-run 预演选拔`

## 5. 分工建议

| 方向 | 涉及文件 |
|---|---|
| 领域算法 | `backend/app/services/selection.py` + `tests/test_selection.py` |
| 流程编排与接口 | `backend/app/services/selection_service.py`、`backend/app/api/*.py` |
| 数据模型与校验 | `backend/app/models.py`、`backend/app/schemas.py` |
| 前端联调 | `docs/design.md` 的 API 约定章节 |
| 文档与演示 | `docs/*.md`、`scripts/demo_flow.py` |

**约定**：改动领域算法必须同步补测试；改动接口必须同步更新 `docs/design.md` 的接口表。

## 6. 提交前检查清单

- [ ] `pytest backend/tests -q` 全绿
- [ ] `ruff check backend/app backend/tests scripts` 无告警
- [ ] 未提交 `data/*.db`、`.env`、`.venv/`
- [ ] 涉及算法/接口变更时已更新文档
- [ ] 新增业务动作已写审计日志

## 7. 冲突处理

```bash
git checkout main && git pull --ff-only
git checkout feature/<模块>
git rebase main
# 解决冲突后
git add <文件>
git rebase --continue
git push --force-with-lease
```

仅在个人分支使用 `--force-with-lease`，禁止强推 `main`。
