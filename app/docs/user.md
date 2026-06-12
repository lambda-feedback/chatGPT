# chatGPT

This evaluation function uses the OpenAI API to determine the correctness (true/false) of a student's response to a question. It can also provide written feedback.

The cost and performance of LLMs changes frequently, so prompts and model choices should be considered experimental and reviewed regularly.

## Inputs

### Required parameters

#### `main_prompt`

Provides context to the AI about the question and the expected answer. Explain what the correct answer is and what criteria should be used to judge the student's response.

You can embed template variables (see **Template variables** below) to include the answer or question text in your prompt.

#### `default_prompt`

Instructs the AI to output a Boolean representing whether the student's response is correct. Do not change this from its default value.

### Optional parameters

#### `model`

The OpenAI model to use for evaluation. Recommended models change over time — check the [OpenAI model documentation](https://platform.openai.com/docs/models) for current recommendations. Recent options include `gpt-4o-mini` and `gpt-4.1-mini`.

#### `question`

The text of the question being answered. When provided, it can be referenced in prompt templates using `{{question}}`.

#### `feedback_prompt`

Guides the AI on how to give written feedback to the student.

Leave this blank if you do not want any textual feedback returned. When set, the feedback is included in the evaluation output. Examples of things you may want to include:

- `Give the student objective and constructive feedback on their answer in first person.`
- `If the student is incorrect, provide feedback/hints to help them, but do not reveal the answer.`

#### `moderator_prompt`

A prompt instructing the AI to check whether the student's response is a legitimate attempt to answer the question, rather than an attempt to manipulate the evaluator (prompt injection).

If omitted, a built-in default handles common manipulation attempts. You do not need to set this unless you have specific moderation requirements.

If moderation fails, the function immediately returns:

```python
{"is_correct": False, "feedback": "Response did not pass moderation."}
```

### Template variables

Any prompt field (`main_prompt`, `default_prompt`, `feedback_prompt`, `moderator_prompt`) can include placeholders that are replaced at evaluation time:

| Variable | Replaced with |
|---|---|
| `{{answer}}` | The correct answer supplied to the function |
| `{{question}}` | The value of the `question` parameter (if provided) |

### Examples

#### Technical question, no feedback

**Main Prompt**:
> In this question, the student is asked to make a comment about the behaviour of a partial sum. The correct answer is 'fast convergence'. Accept any paraphrasing/equivalent answers. To be correct, they must mention both aspects (fast and convergence).

**Feedback Prompt**:
> *(Empty)*

<img src="https://github.com/lambda-feedback/chatGPT/assets/138524447/af083bff-fade-4186-89aa-bc0b7f48ce0d" width="450">

#### Essay with feedback

**Main Prompt**:
> Students should write an essay for GCSE English ... [details to go here]

**Feedback Prompt**:
> Give objective feedback. Be concise.