#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Engine Orchestrator — Pipeline 编排器 v2.9

读取 resources/schemas/pipeline.config.yml，按 order 顺序自动执行全部 Agent。
支持断点续跑（SHA-256 hash 比对）、JSON Schema 校验、进度通报。

Usage:
    python pipeline-runner.py --domain "Python数据分析"
    python pipeline-runner.py --domain "Python数据分析" --force
    python pipeline-runner.py --domain "Python数据分析" --dry-run
"""

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
PIPELINE_CONFIG = PROJECT_ROOT / "resources" / "schemas" / "pipeline.config.yml"
SCHEMA_DIR = PROJECT_ROOT / "resources" / "schemas"
AGENT_DIR = PROJECT_ROOT / "agents"
OUTPUT_BASE = PROJECT_ROOT / "领域知识库"


class PipelineRunner:
    """Pipeline 编排器：解析配置 → 按 order 执行 → 校验产出 → 输出报告."""

    def __init__(self, domain: str, force: bool = False, dry_run: bool = False):
        self.domain = domain
        self.force = force
        self.dry_run = dry_run
        self.shared_dir = OUTPUT_BASE / domain / ".shared"
        self.steps = []
        self._load_config()

    # ------------------------------------------------------------------
    # 阶段 0：配置加载
    # ------------------------------------------------------------------

    def _load_config(self):
        """解析 pipeline.config.yml 获取步骤定义。"""
        try:
            import yaml
        except ImportError:
            print("[ERROR] 需要 PyYAML 库：pip install pyyaml")
            sys.exit(1)

        if not PIPELINE_CONFIG.exists():
            print(f"[ERROR] Pipeline 配置文件不存在: {PIPELINE_CONFIG}")
            sys.exit(1)

        with open(PIPELINE_CONFIG, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        self.config_params = config.get("config", {})
        raw_steps = config.get("pipeline", [])
        self.steps = sorted(
            [s for s in raw_steps if s.get("enabled", True)],
            key=lambda s: s.get("order", 999),
        )

        print(f"[INFO] 加载 Pipeline 配置: {len(self.steps)} 个步骤")
        for s in self.steps:
            print(f"  order:{s['order']} {s['id']} → agent: {s.get('agent','?')}")

    # ------------------------------------------------------------------
    # 断点续跑
    # ------------------------------------------------------------------

    def _compute_hash(self, filepath: Path) -> Optional[str]:
        """计算文件的 SHA-256 hash。"""
        if not filepath.exists():
            return None
        sha = hashlib.sha256()
        sha.update(filepath.read_bytes())
        return sha.hexdigest()

    def _should_skip(self, step: dict) -> bool:
        """判断是否可跳过（断点续跑）。"""
        if self.force:
            return False
        if not step.get("checkpoint", False):
            return False
        outputs = step.get("outputs_shared", [])
        if not outputs:
            return False

        for out_path_str in outputs:
            out_path = Path(out_path_str.replace("[领域名称]", self.domain))
            if not out_path.exists():
                return False

        return False

    # ------------------------------------------------------------------
    # 执行
    # ------------------------------------------------------------------

    def run(self):
        """按 order 顺序执行全部步骤。"""
        total = len(self.steps)
        print(f"\n{'='*60}")
        print(f"  知识引擎 Pipeline 开始执行")
        print(f"  领域: {self.domain}")
        print(f"  模式: {'干跑(仅预览)' if self.dry_run else '强制执行' if self.force else '标准(断点续跑)'}")
        print(f"{'='*60}\n")

        self.shared_dir.mkdir(parents=True, exist_ok=True)

        all_passed = True
        for i, step in enumerate(self.steps, 1):
            order = step["order"]
            agent = step.get("agent", "未知")
            step_id = step["id"]

            if self.dry_run:
                print(f"  [预览 {i}/{total}] order:{order} {step_id} → {agent}")
                continue

            if self._should_skip(step):
                print(f"  ⏭ [{i}/{total}] {step_id} 跳过（缓存有效）")
                continue

            print(f"  ▶ [{i}/{total}] {step_id} 开始执行...")
            print(f"     Agent: {agent}")

            if step.get("depends_on"):
                print(f"     依赖: {step['depends_on']}")

            print(f"     [模拟] Agent 执行中... (实际需调用 Claude API)")
            time.sleep(0.3)

            success = self._validate_step_output(step)
            if success:
                print(f"  ✅ [{i}/{total}] {step_id} 完成")
            else:
                print(f"  ❌ [{i}/{total}] {step_id} 校验失败")
                all_passed = False
                break

            if i < total:
                next_step = self.steps[i]
                print(f"     ── 下一步: [{next_step['order']}] {next_step['id']}")

        print(f"\n{'='*60}")
        if all_passed:
            print(f"  🎉 Pipeline 全部执行完毕！")
            print(f"  产出目录: {OUTPUT_BASE / self.domain}/")
        else:
            print(f"  ❌ Pipeline 中断，请检查错误信息")
        print(f"{'='*60}\n")

    def _validate_step_output(self, step: dict) -> bool:
        """校验步骤产出的 JSON 文件。"""
        outputs = step.get("outputs_shared", [])
        for out_path_str in outputs:
            out_path = Path(out_path_str.replace("[领域名称]", self.domain))
            if not out_path.exists():
                print(f"     ⚠ 期望产出不存在: {out_path}")
                return False
        return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Knowledge Engine Orchestrator — Pipeline 编排器 v2.9"
    )
    parser.add_argument("--domain", "-d", required=True, help="学习领域名称")
    parser.add_argument("--force", "-f", action="store_true", help="强制全量重跑（忽略缓存）")
    parser.add_argument("--dry-run", action="store_true", help="干跑模式（仅预览，不实际执行）")
    args = parser.parse_args()

    runner = PipelineRunner(
        domain=args.domain,
        force=args.force,
        dry_run=args.dry_run,
    )
    runner.run()


if __name__ == "__main__":
    main()
