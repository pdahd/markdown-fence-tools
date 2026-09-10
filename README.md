
# Markdown Fence Tools

一个无需服务器、无需账号的 Markdown 文本处理面板，提供：

- 逐行缩进 / 反缩进（1、2、4 个空格，支持长按连续处理）
- 复制、清空、导入和按扩展名导出
- 清理代码围栏；可选“清理后整体加围栏”模式
- 将常见 Markdown 转为纯文本
- 适配移动端触控操作、文件导入 Bottom Sheet 与 Android 软键盘行为
- 避免 `innerHTML` 等 HTML 解析 sink，兼容启用 Trusted Types 的 YouTube 页面

## 文件说明

```text
index.html                               完整自包含的 GitHub Pages 独立网页，打开即显示工具
panel.js                                 供远程书签注入的面板运行时
remote-bookmarklet-template.txt          远程书签模板
userscript/MD_Fence_Tools.user.js        Tampermonkey 油猴脚本版
```

## GitHub Pages 独立网页

在 GitHub 仓库的 **Settings → Pages** 中，将发布源设为：

```text
Deploy from a branch → main → /(root)
```

保存后，独立网页地址为：

```text
https://pdahd.github.io/markdown-fence-tools/
```

该页面是完整自包含的单个 HTML 文件；即使直接打开 `index.html`，也不需要再请求 `panel.js`。访问后会自动打开工具面板，适合需要独立处理 Markdown、不希望依赖当前网页的情况。

## 远程书签

1. 打开 `remote-bookmarklet.txt`。
2. 将其中唯一的一整行内容（含开头 `javascript:`）复制到浏览器书签的 URL/地址栏字段。

该书签会加载：

```text
https://pdahd.github.io/markdown-fence-tools/panel.js
```

再次使用同一个书签时会切换打开/关闭面板。部分站点可能因为自己的 CSP 或 Trusted Types 策略禁止远程脚本注入；独立 GitHub Pages 页面不受此限制。

## Tampermonkey 版

`userscript/MD_Fence_Tools.user.js` 可直接粘贴进 Tampermonkey。它在普通网页内提供右下角“工具”启动按钮，以及 `Ctrl + Alt + M` 快捷键。

## 更新远程版本

修改 `panel.js` 后，先运行 `python3 scripts/build-standalone.py` 同步生成自包含的 `index.html`，再将两者提交到 `main` 分支。远程书签会附加当前时间戳参数，避免浏览器长期复用旧缓存，因此无需每次手工修改书签版本号。

## 说明

“转纯文本”面向常见笔记、README、教程类 Markdown。它会处理标题、强调、链接、图片、围栏代码、引用、无序列表、任务列表、分隔线和常见 HTML 标签；复杂 CommonMark/GFM 边界语法并非完整解析器范围。
