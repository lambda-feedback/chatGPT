# Evaluation Function using ChatGPT

This function can be used to prompt GPT models by providing prompts in the request parameters. For more information, look at `app/docs`.

## Table of Contents
- [Evaluation Function Using ChatGPT](#evaluation-function-using-ChatGPT)
  - [Table of Contents](#table-of-contents)
  - [Repository Structure](#repository-structure)
  - [Usage](#usage)
    - [Getting Started](#getting-started)
  - [How it works](#how-it-works)
    - [Docker & Amazon Web Services (AWS)](#docker--amazon-web-services-aws)
    - [Middleware Functions](#middleware-functions)
    - [GitHub Actions](#github-actions)
  - [Pre-requisites](#pre-requisites)

## Repository Structure

```bash
evaluation_function/
    __init__.py
    evaluation.py # Script containing the main evaluation_function
    preview.py # Script containing the preview functionality
    docs.md # Documentation page for this function (required)
    evaluation_tests.py # Unittests for the main evaluation_function
Dockerfile # for building whole image to deploy to AWS

.github/
    workflows/
        test-and-deploy.yml # Testing and deployment pipeline

config.json # Specify the name of the evaluation function in this file
.gitignore
```