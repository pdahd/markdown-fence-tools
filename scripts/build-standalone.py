#!/usr/bin/env python3
"""Embed the shared panel runtime into index.html for a fully self-contained page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PANEL = (ROOT / "panel.js").read_text(encoding="utf-8")
INDEX = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="dark">
  <title>Markdown 代码围栏工具</title>
  <style>
    html,body{{min-height:100%;margin:0}}
    body{{overflow:hidden;background:radial-gradient(circle at 20% 0,#164e63 0,transparent 38%),radial-gradient(circle at 90% 100%,#312e81 0,transparent 42%),#0b1020;color:#e6e9f0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}}
    .page-note{{position:fixed;z-index:1;left:50%;bottom:2.5vh;max-width:min(90vw,680px);transform:translateX(-50%);color:#94a3b8;font-size:12px;line-height:1.5;text-align:center;pointer-events:none}}
    .page-note kbd{{padding:1px 5px;border:1px solid #475569;border-radius:4px;background:#1e293b;color:#e2e8f0;font:11px ui-monospace,Consolas,monospace}}
    noscript{{display:block;margin:20px;color:#fecaca}}
  </style>
</head>
<body>
  <noscript>此工具需要启用 JavaScript。</noscript>
  <div class="page-note">Markdown 代码围栏工具独立版 · 面板自动打开 · <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>M</kbd> 可切换面板</div>
  <script>
    // 独立页嵌入与 panel.js 相同的运行时，因此即使直接打开 index.html 也无需额外网络请求。
    window.__MDFenceToolsAutoOpen = true;
{PANEL}
  </script>
</body>
</html>
'''
(ROOT / "index.html").write_text(INDEX, encoding="utf-8")
print("Wrote", ROOT / "index.html")

