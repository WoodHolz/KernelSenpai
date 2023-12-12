# 项目构想 Project Concept

日安，我想构建一个项目，使用 LLM 来编写 Linux Kernel 的书或者介绍手册的万能书。

Hello,there. I want to build a project that utilizes Large Language Models (LLM) to create a comprehensive guide or manual for the Linux Kernel.

我了解到的现在背景是 对于 Linux kernel 这种极其复杂巨大且经过多年发展的大项目，所有有关 Linux kernel 学习的书讲解涉及的内核版本与现实差距过大，再版这些书籍对人类作者而言需要对内核有丰富了解且有巨量的精力，但是考虑到目前熟悉 Linux kernel的专家普遍年龄偏大且 Linux 内核本身发展迅速，而使得这项工作几乎不可能赶得上内核的发展。

The current background I've observed is that when it comes to learning about the Linux kernel, a project that is both extremely complex and vast, and has evolved over many years, existing books often have a significant gap between the kernel versions they cover and the current reality. Revising these books requires human authors with extensive knowledge of the kernel and a substantial amount of time. However, considering that many experts familiar with the Linux kernel are generally older, and the Linux kernel itself is evolving rapidly, keeping these books up to date has become nearly impossible.

因此我想要使用 AI 大语言模型来分析 Linux kernel 的更新，做到与时俱进地更新编写 Linux Kernel 的书。

Therefore, my idea is to use an AI Large Language Model to analyze updates to the Linux kernel, ensuring that the writing of the Linux Kernel guide stays current.

我的想法是通过结合[`Bootlin`网站](https://elixir.bootlin.com/linux/)和 github中 Linux 官方项目的所有 commit, pr, issue 记录来作为语料训练大模型，通过大模型来总结现在内核的结构，工作流程编写成 Gitbook 在线书籍。同时支持引入人类对编写的文档进行纠错并反馈给大模型改正。功能还有描述 Linux 内核某一功能的发展，方便学习者理解。

I propose to achieve this by combining information from the Bootlin website and all commit, pull request (PR), and issue records from the official Linux project on GitHub as training data for the language model. The large model would then summarize the current structure of the kernel and its workflow, producing an online Gitbook. This platform would also support human input for document editing, allowing users to provide corrections and feedback to the model. Additionally, the system would include features to describe the development of specific functionalities within the Linux kernel, making it easier for learners to comprehend.

---

作为一名大三学生，我需要准备考研升学和寻找实习，因此这个项目的进展会相对较慢。(´;ω;`)

As a third-year undergraduate student, I need to prepare for postgraduate entrance exams and search for internships, so the progress of this project will be relatively slow. (´;ω;`)