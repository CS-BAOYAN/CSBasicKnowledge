# CSBasicKnowledge   

欢迎来到这个专注于计算机科学基础知识的仓库。本仓库的目标是补充计算机专业教育中可能缺失的知识点，提供广泛、优质的学习资源。

我们鼓励并期待有缘人加入我们，共同维护和丰富这个仓库。无论是添加新内容，还是改进现有内容，您的贡献都将使这个仓库变得更好。

在线阅读：https://cs-baoyan.github.io/CSBasicKnowledge/

Welcome to this repository focused on fundamental knowledge of computer science. The goal of this repository is to supplement potential gaps in computer science education and provide a wide range of high-quality learning resources.

We encourage and look forward to like-minded individuals joining us to collectively maintain and enrich this repository. Whether it's adding new content or improving existing content, your contributions will make this repository better.

Online reading: https://cs-baoyan.github.io/CSBasicKnowledge/

## 鸣谢

<a href="https://github.com/CS-BAOYAN/CSBasicKnowledge/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=CS-BAOYAN/CSBasicKnowledge" />
</a>

Made with [contrib.rocks](https://contrib.rocks).


## 贡献指南
若希望对**CSBasicKnowledge**进行贡献，请以`SUMMARY.md`为大纲，在`src`文件夹下进行markdown文件的添加即可。

- src/ac(academic)：本章节主要讲一些学术相关的知识，包括文献搜索，科研经验、读博体验等。
- src/ai(artificial intelligence)：本章节包括PyTorch，huggingface，各个小方向的相关知识。
  - PyTorch resources
  - huggingface resources（包括如何换源/加速下载
  - dataset resources
  - NLP / CV / Audio / Recommendation System / Large Language Model
  - 常见的tutorials，主要围绕有监督学习方向提供材料
  - prompts的使用
  - CUDA & NVIDIA
- src/cg(computer graphics)：计算机图形学相关资料
- src/cs(computer science): 计算机科学相关材料
- src/pl(programming language): 包括Program Synthesis & Automated Reasoning和Program Analysis
- src/security: 安全相关的知识
- src/sys(system): 是Computer System，涵盖sys的各个方面，包括arch/os/storage/db/HPC等等
- src/useful: 一些实用的小工具。包括Linux常见操作，bash的编写，Vim，git/github的使用，如何debug，conda&docker
- src/writing：写作相关的工具（LaTex，Typst，常见的简历模板
- src/programmer: 程序员指南
- src/file: 一些附属文件
- src/misc: 一些杂项（如果你对要添加的内容没有一个很明确的归类，可以放在这个里面

目前，mdbook对数学公式的支持还不完善，如您需要使用数学公式，请参考下面的**数学公式支持**部分。

**（可选）** 如果您在部署了mdbook并运行后，可以直接在`SUMMARY.md`中添加章节，例如：
```md
# CSBasicKnowledge

- [example](./example/example.md)
```
mdbook会自动创建`example`文件夹和`example.md`文件。
当然，mdbook依赖于rust语言开发，如果您不喜欢rust相关内容，可以无视可选项及后续的**本地部署**部分。

## 数学公式支持
> **注意**： MathJax 目前仍不能使用 `$$ ... $$` 作为分隔符，并且 `\[ ... \]` 分隔符需要额外的反斜杠才能工作。 希望这个限制很快能解除。

> **注意**： 当您需要在 MathJax 块中使用双反斜杠（例如 `\begin{cases} \frac 1 2 \\ \frac 3 4 \end{cases}` 等命令中）时，您需要添加两个额外的反斜杠（例如，`\begin{cases} \frac 1 2 \\\\ \frac 3 4 \end{cases}`)。

### 行内公式
行内公式由 `\\(` 和 `\\)`包围。例如，要渲染以下行内方程
\\( \int x dx = \frac{x^2}{2} + C \\)，可以这么写：
```
\\( \int x dx = \frac{x^2}{2} + C \\)
```

### 块公式
块公式由 `\\[` 和 `\\]`分隔。 要渲染下面这个块公式

\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]

可以这么写:

```
\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]
```

## 本地部署
CSBasicKnowledge的bookfy基于[mdbook](https://github.com/rust-lang/mdBook)实现，该工具基于Rust开发，是markdown文件书本化非常值得推荐的工具。Rust的圣经 ***The Rust Programming Language*** 便是利用了mdbook生成的。

要安装**mdbook**请安装Rust相关工具链。随后，通过Rust的包管理器cargo进行mdbook的安装：
```bash
cargo install mdbook
```
通常，mdbook会安装在`$HOME/.cargo/bin`，请将该目录添加至PATH

mdbook的运行非常简单，只需要：
```bash
# For detail, run `mdBook serve -h`
mdbook serve            # default 127.0.0.1:3000
mdbook serve -p 8080    # 127.0.0.1:8080
```
