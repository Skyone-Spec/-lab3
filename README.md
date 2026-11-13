# 均分背后｜MovieLens 交互数据故事

这是课程“交互式可视化”作业，研究问题是：**一个平均分隐藏了多少关于样本与分歧的信息？**从两片评分分布猜均分，揭晓后逐档拆解差距，再进入自由选片与榜单实验。

## 打开与探索

[打开作品](https://skyone-spec.github.io/-lab3/) · [阅读研究报告](研究报告.md)

我从两部均分都接近 2.8 星的电影入手：一部收到更多低分，也收到更多高分；另一部的评分更集中在中间。首页先展示十档评分，让读者猜哪部均分更高。揭晓后可以点选任意星级，查看这一档给两片拉开了多少差距。

想自己找例子，可以在双片对照中调整人数门槛和均分容差。想知道分差是否受观众打分习惯影响，可以切换校准力度，或点击排行榜片名，检查匿名用户的评分记录。散点图支持按类型、年代筛选和框选；最后的榜单实验可以检验小样本电影对排名的影响。

本地预览时，在仓库目录运行 `python -m http.server 8000`，用浏览器打开 `http://localhost:8000`。网页从仓库读取两份 CSV，图表与 ZIP 导入所需的库均随项目提供。

复现报告汇总：安装 `pandas` 和 `scipy` 后运行 `python analysis/research.py`。网页运行无需 Python。

## 文件

- `index.html`：D3.js 交互式可视化
- `data/`：MovieLens Small 官方数据 CSV 与许可说明
- `研究报告.md`：研究问题、设计理由、数据发现、局限与开发过程
- `analysis/research.py`：复现候选量、重合度与 Spearman 相关
- `assets/`：D3 7.9.0、JSZip 3.10.1 及许可

## 数据与引用

数据来自 [GroupLens MovieLens Latest Small](https://grouplens.org/datasets/movielens/latest/)，本目录保留官方 README / 使用许可。外部图表库为 [D3.js](https://d3js.org/)；ZIP 本地导入使用 [JSZip](https://stuk.github.io/jszip/)。
