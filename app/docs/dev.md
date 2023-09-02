# chatGPT Evaluation Function

## Overview
This chatGPT evaluation function is designed to automatically evaluate student responses to questions. It currently uses the openAI API to determine the correctness (true/false) of the student's answer and can also provide them with feedback.

## Setup
To successfully run this function, ensure you set your OpenAI API key. The code fetches this key from environment variables, so ensure it's set up in your environment or `.env` file.

## Inputs

### Parameters dictionary:

1. **model**: 
   - Deinfes the AI model used for evaluation.
   - Currently, "gpt-3.5-turbo" is the only model available.

2. **main_prompt**: 
   - **Description**: This prompt provides context to the AI, detailing the nature of the question and the expected answer(s).

3. **default_prompt**: 
   - **Description**: A standardised instruction directing the AI to output a boolean correctness of the stident's answer.

4. **feedback_prompt**: 
   - This prompt guides the AI on how feedback should be given. 
   - If left blank, only a binary correctness assessment is returned without detailed feedback.
  
Note that an input of a variable called `answer` is also required. This can be any value. This is to ensure compatibility with LambdaFeedback.

### Example Input:

```python
parameters = {
    'model': 'gpt-3.5-turbo',
    'main_prompt': "Evaluate the student's response regarding the definition of photosynthesis",
    'default_prompt': "Output a Boolean: True if the student is correct and False if they are incorrect.",
    'feedback_prompt': "You are an AI tutor. Provide feedback based on the student's answer."
}
response = "Photosynthesis is the process by which plants convert light energy into chemical energy to fuel their growth."
```

## Outputs

The function will yield a dictionary with the following structure:

```python
{
    'is_correct': bool,
    'feedback': string (Optional)
}
```

## Usage Examples

### Capital City Assessment

```python
parameters = {
    'model': 'gpt-3.5-turbo',
    'main_prompt': "Analyze the student's response about the capital of France.",
    'default_prompt': "Output a Boolean: True if the student is correct and False if they are incorrect.",
    'feedback_prompt': "You are an AI tutor. Offer constructive feedback."
}
response = "The capital of France is Berlin."
output = evaluation_function(response, answer, parameters)
```

Expected Output:

```python
{
    'is_correct': False,
    'feedback': "The actual capital of France is Paris. Please revisit your geography notes."
}
```
