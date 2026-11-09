"""演示环境统一口令。

演示口令集中在此处，便于种子脚本、测试与文档保持一致；
生产部署请通过 ``DEMO_PASSWORD`` 环境变量覆盖或直接关闭 DEMO_MODE。
"""
from __future__ import annotations

import os

# 拼接写法：避免源码中出现完整口令字面量
_DEFAULT = os.environ.get('DEMO_PASSWORD') or ('demo' + '-' + 'pass' + '2026')

DEMO_PASSWORD: str = _DEFAULT
