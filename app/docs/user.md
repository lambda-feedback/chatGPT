# chatGPT

## What does it do?
This chatGPT evaluation function is designed to automatically evaluate student responses to questions. It uses the OpenAI API to determine the correctness (true/false) of the student's answer and can also provide them with feedback.

## What does the teacher need to input?
- `model`
    - Suggest (July 2025), `gpt-4o-mini` or `gpt-4.1-mini`.

- `question` [optional]
    - The text of the question being answered. Set this if you want to reference the question wording inside your prompts using `{{question}}`.

- `main_prompt`
    - In this prompt you should explain the question and answer to GPT.
    - You can embed `{{answer}}`, `{{question}}`, and `{{response}}` as placeholders in your prompts (see **Template variables** below).

- `correctness_prompt` [do not change from default]
    - Instructs GPT to output a boolean: `True` if the student is correct, `False` if not. Leave this as the default.

- `feedback_prompt` [optional]
    - Leave this prompt **blank** if you do not want any textual/qualitative feedback to be given to the student.
    - Fill in this prompt to tell GPT how to give written feedback to the student. Examples of things you may want to include in your `feedback_prompt`:
        - `Give the student objective and constructive feedback on their answer in first person.`
        - `If the student is incorrect, provide feedback/hints to help them, but do not reveal the answer.`

- `moderator_prompt` [optional, advanced]
    - By default, the system automatically checks whether a student response is attempting to manipulate the AI evaluator (prompt injection). A student response that tries to dictate feedback or override the marking will be automatically marked as incorrect with the message "Response did not pass moderation."
    - You do not need to set this — the built-in default handles common manipulation attempts.
    - You can override it with a custom prompt if you have specific moderation needs.

The cost and performance of LLMs changes by the month, so do not assume that your prompts and model choice are good in the long term. Approaches with LLMs should be considered experimental.

## Template variables

Any prompt field (`main_prompt`, `correctness_prompt`, `feedback_prompt`, `moderator_prompt`) can include placeholders that are replaced at evaluation time:

- `{{answer}}` and `{{response}}` are filled in automatically from the correct answer and the student's submission.
- `{{question}}` is filled in from the `question` parameter — you must set this in the UI for it to have a value.

**Example** — referencing the student's response in feedback:

**Feedback Prompt**:
> Give objective feedback. The student wrote: {{response}}. If they are incorrect, give a hint without revealing the answer.

## Usage examples
Each example below demonstrates the potential usage of `main_prompt` and `feedback_prompt` for different questions.

### Technical question, for correctness and with no feedback.
**Main Prompt**:
> In this question, the student is asked to make a comment about the behaviour of a partial sum. The correct answer is 'fast convergence'. Accept any paraphrasing/equivalent answers. To be correct, they must mention both aspects (fast and convergence).

**Feedback Prompt**:
> *(Empty)*

<img src="https://github.com/lambda-feedback/chatGPT/assets/138524447/af083bff-fade-4186-89aa-bc0b7f48ce0d" width="450">

### Essay with feedback.
**Main Prompt**:
> Students should write an essay for GCSE English ... [details to go here]

**Feedback Prompt**:
> Give objective feedback. Be concise.