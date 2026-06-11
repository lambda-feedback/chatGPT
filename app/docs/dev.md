# chatGPT Evaluation Function

## Overview
This chatGPT evaluation function is designed to automatically evaluate student responses to questions. It uses the OpenAI API to determine the correctness (true/false) of the student's answer and can also provide them with feedback.

Evaluation runs in three stages:
1. **Moderation** — checks the student response is not attempting to manipulate the AI evaluator.
2. **Correctness** — determines whether the response is correct (boolean).
3. **Feedback** — generates written feedback (only if `feedback_prompt` is provided).

If moderation fails, stages 2 and 3 are skipped and the response is immediately marked incorrect.

## Setup
To successfully run this function, ensure you set your OpenAI API key. The code fetches this key from environment variables, so ensure it's set up in your environment or `.env` file.

## Inputs

### Parameters dictionary:

1. **model**:
   - Defines the AI model used for evaluation.
   - Accepts a simple alias (`small`, `medium`, `large`, `reasoning`) or any raw OpenAI model string (e.g. `gpt-4o-mini`).

   | Alias | Model |
   |---|---|
   | `small` | `gpt-4o-mini` |
   | `medium` | `gpt-4o` |
   | `large` | `gpt-4.1` |
   | `reasoning` | `o4-mini` |

2. **question** *(optional)*:
   - The text of the question being answered by the student.
   - When provided, it is substituted into prompt templates wherever `{{question}}` appears.

3. **moderator_prompt** *(optional)*:
   - A prompt instructing the AI to check whether the student response is a legitimate attempt to answer the question, rather than an attempt to manipulate the evaluator (e.g. prompt injection).
   - If omitted, a built-in default prompt is used.
   - If moderation returns `False`, the function immediately returns:
     ```python
     {"is_correct": False, "feedback": "Response did not pass moderation."}
     ```

4. **main_prompt**:
   - **Description**: Provides context to the AI about the nature of the question and the expected answer(s).

5. **default_prompt**:
   - **Description**: A standardised instruction directing the AI to output a boolean representing the correctness of the student's answer.

6. **feedback_prompt**:
   - Guides the AI on how feedback should be given.
   - If left blank, only a binary correctness assessment is returned without detailed feedback.

### Template variables

All prompt fields (`main_prompt`, `default_prompt`, `feedback_prompt`, `moderator_prompt`) support the following substitution variables:

| Variable | Replaced with |
|---|---|
| `{{answer}}` | The correct answer supplied to the function |
| `{{question}}` | The value of the `question` parameter (if provided) |
| `{{response}}` | The student's response |

Example: setting `main_prompt` to `"The question is {{question}}. The correct answer is {{answer}}."` will produce a fully populated prompt at evaluation time.

Note that an input of a variable called `answer` is also required. This can be any value. This is to ensure compatibility with LambdaFeedback.

### Example Input:

```python
parameters = {
    'model': 'small',
    'question': 'What is photosynthesis?',
    'main_prompt': "The question asked was: {{question}}. The correct answer is: {{answer}}. Evaluate the student's response: {{response}}.",
    'default_prompt': "Output a Boolean: True if the student is correct and False if they are incorrect.",
    'feedback_prompt': "You are an AI tutor. Provide feedback based on the student's answer."
}
response = "Photosynthesis is the process by which plants convert light energy into chemical energy to fuel their growth."
answer = "Photosynthesis converts light energy into chemical energy stored as glucose."
```

## Outputs

The function returns a dictionary with the following structure:

```python
{
    'is_correct': bool,
    'feedback': string  # present when feedback_prompt is non-empty, or when moderation fails
}
```

## Usage Examples

### Capital City Assessment

```python
parameters = {
    'model': 'small',
    'main_prompt': "Analyze the student's response about the capital of France. The correct answer is {{answer}}.",
    'default_prompt': "Output a Boolean: True if the student is correct and False if they are incorrect.",
    'feedback_prompt': "You are an AI tutor. Offer constructive feedback."
}
response = "The capital of France is Berlin."
answer = "Paris"
output = evaluation_function(response, answer, parameters)
```

Expected Output:

```python
{
    'is_correct': False,
    'feedback': "The actual capital of France is Paris. Please revisit your geography notes."
}
```