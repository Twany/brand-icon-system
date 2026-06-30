# Brand Icon System

[English](README.md) | [简体中文](README.zh-CN.md)

一个用于生成生产可用 PNG 品牌图标系统的阶段化 Agent Skills 仓库。

它不是“一句话直接出最终 logo”的流程，而是刻意拆成可选择、可回退、可审计的几个阶段：brief、explore、select、refine、produce、audit。适合能够生成 PNG 图片并运行本地 Python 脚本的 AI agent 使用。

![AI 白噪音图标探索表](examples/ai-white-noise/exploration-contact-sheet.png)

![AI 白噪音图标系统总览](examples/ai-white-noise/logo-system-overview.png)

## 能做什么

- 生成 4x6 的黑白 logo 探索板。
- 把探索板切分成 24 个带编号的 PNG 候选图。
- 在最终生产前暂停，让用户先选择方向。
- 将选中的方向细化成干净的 raster mark。
- 导出透明 mark、app icon、favicon、lockup、主题色变体、预览图、manifest 和 README。
- 审计最终产物的 mask 质量、favicon 可读性、透明背景、图标留白和 lockup 构图。

## 项目结构

```text
brand-icon-system/
  skills/
    brand-icon-system/       # 总控 skill，共享脚本和资源
    brand-logo-brief/        # 将主题整理成 logo brief
    brand-logo-explore/      # 生成候选探索板和选择表
    brand-logo-refine/       # 将选中候选细化成最终 mark
    brand-logo-produce/      # 导出 PNG 图标系统
    brand-logo-audit/        # 最终质量审计
  docs/
  examples/
  tests/
```

## 环境要求

- Python 3.10+
- Pillow
- 一个可以生成 PNG 图片的 AI 生图工具

安装 Python 依赖：

```bash
python3 -m pip install -r requirements.txt
```

## 安装

这个仓库遵循 Agent Skills 目录结构：每个 skill 都放在 `skills/<skill-name>/SKILL.md`。

如果你的 agent host 支持从 GitHub 安装 skills，可以直接安装本仓库里的全部 skills。对于支持 `gh skill` 的 host，命令形式类似：

```bash
gh skill install OWNER/brand-icon-system --all
```

手动安装也可以：

```bash
mkdir -p ~/.agents/skills
cp -R skills/* ~/.agents/skills/
```

请根据你的 agent host 使用对应的 skills 目录。常见目录包括 `.agents/skills`、`.claude/skills`、`~/.codex/skills`。

也可以使用内置安装脚本，并传入你的 host 读取的 skills 目录：

```bash
./scripts/install.sh ~/.agents/skills
```

## 使用方式

推荐从总控 skill 开始：

```text
Use $brand-icon-system to generate a brand icon system for "AI white noise".
```

默认流程会在探索阶段结束后停下来，让用户从候选表里选择编号。只有当用户确认候选或最终 mark 后，才会进入 PNG 图标系统生产阶段。

如果你想精细控制，也可以单独调用某个阶段：

```text
Use $brand-logo-explore to generate a black-and-white candidate board for "AI white noise".
Use $brand-logo-produce to export this approved mark as a PNG logo system.
```

## 工作流

1. `brand-logo-brief`：把产品主题、品牌名或粗略方向整理成简短 logo brief。
2. `brand-logo-explore`：生成黑白 4x6 候选探索板，并切成 24 个候选 PNG。
3. 用户选择候选编号，或明确授权 agent 自主选择。
4. `brand-logo-refine`：把选中方向细化成干净的独立 mark。
5. 用户确认最终 mark。
6. `brand-logo-produce`：导出完整 PNG 图标系统。
7. `brand-logo-audit`：检查 mask、透明背景、小尺寸可读性、lockup 和颜色表现。

## 验证

运行：

```bash
python3 tests/validate_skills.py
python3 tests/smoke_test_split_board.py
python3 tests/smoke_test_build_system.py
```

## 参考来源

探索阶段参考了 `fucha1122/minimalist-bw-logo-skill` 的黑白候选探索思路：先生成大量单色方向，再从其中一个方向进入生产。这个项目没有复制它的 prompt 或实现，而是使用自己的阶段化 prompt、PNG 脚本和生产流程。

## 许可证

代码和文档使用 MIT License。内置 Newsreader 字体使用 SIL Open Font License，详见 `skills/brand-icon-system/assets/fonts/OFL.txt`。
