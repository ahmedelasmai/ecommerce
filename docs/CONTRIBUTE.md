# Welcome to our contributing guide

Thank you for investing your time in contributing to our project! We sincerely appreciate it.

## Content

- [Welcome to our contributing guide](#welcome-to-our-contributing-guide)
  - [New contributor guide](#new-contributor-guide)
  - [Getting started](#getting-started)
    - [:File Structure](#file-structure)
  - [Issues](#issues)
      - [Create a new issue](#create-a-new-issue)
    - [Solve an issue](#solve-an-issue)
      - [Prerequisites](#prerequisites)
      - [Commits](#commits)
      - [Branch](#branch)

## New contributor guide

To get an overview of the project, read the [README](../README.md). Here are some resources to help you get started with open source contributions:

- [How to install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [How to handle repositories](https://docs.gitlab.com/ee/user/project/repository/)
- [Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
- [Creating merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)

## Getting started

###   File Structure
    .
    └── docs              // documentation of the project

## Issues

#### Create a new issue

If you spot a problem with the tool or the documentation, please check [issues_page](https://github.com/jacketoff/ecommerce/issues)

<details>
<summary>How to write a useful issue?</summary>
<br />

- It should be _reproducible_. It should contain all the instructions needed to reproduce the same outcome.

- It should be _specific_. It's important that it addresses one specific problem.

</details>

### Solve an issue

Scan through our [existing issues](https://github.com/jacketoff/ecommerce/issues) to find one that interests you.
If you find an issue to work on, you are welcome to open a merge request with a fix.

#### Prerequisites

Please, before submitting any merge request, be sure that your branch is passing all requirements.

1. Check that all tests are working:

```bash

```

2. Check that there are no linting issues:

```bash

```
(the command will also try to fix found issues)

3. Check that the files are formatted:

```bash

```
(the command will also try to fix found issues)

#### Commits

The commits must be compliant with the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).

#### Branch

We use the [Git-Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) branching model:

```mermaid
        gitGraph
       commit id: "a"
       commit id: "b"
       branch develop
       checkout develop
       checkout develop
       branch feature1
       checkout feature1
       commit id: "c"
       checkout develop
       merge feature1
       branch feature2
       checkout feature2
       commit id: "d"
       checkout develop
       merge feature2
       checkout main
       merge develop
       branch "release"
       checkout release
       commit id: "1.0.0" tag: "release"
       checkout main
       merge release
       checkout develop
       merge main
```
