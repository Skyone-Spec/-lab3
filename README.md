# MovieLens 评分探索｜交互式可视化

这是课程“交互式可视化”作业原型，研究问题是：**评分人数和评分分歧会怎样影响我们对电影口碑的判断？**

## 打开与探索

直接访问部署站点，或在本地通过静态 HTTP 服务打开 `index.html`。页面会从 `data/movies.csv` 与 `data/ratings.csv` 自动读取 MovieLens Small 数据。可按类型、发行年代和最低评分人数筛选；切换榜单指标；点击散点或榜单行联动查看单片评分详情与评分分布。

## 文件

- `index.html`：D3.js 交互式可视化
- `data/`：MovieLens Small 官方数据 CSV 与许可说明
- `研究报告.md`：研究问题、设计理由、数据发现、局限与开发过程

## GitHub Pages 部署

将本目录文件推送到 GitHub 仓库默认分支，然后在仓库 **Settings → Pages** 选择从分支部署，分支选 `main`，目录选 `/ (root)`。该项目无需构建步骤或服务器端程序。启用后等待 GitHub Pages 完成发布，并将公开网址填入报告。

## 数据与引用

数据来自 [GroupLens MovieLens Latest Small](https://grouplens.org/datasets/movielens/latest/)，本目录保留官方 README / 使用许可。外部图表库为 [D3.js](https://d3js.org/)；ZIP 本地导入使用 [JSZip](https://stuk.github.io/jszip/)。
