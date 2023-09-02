# chatGPT

There are three arguments to consider:
- 'Main_prompt'
-   This



This function makes an openAI API call to gpt to evaluate the student's answer. The overall prompt into gpt is made up of:

- The system prompt
- The user prompt

The **system prompt** into gpt is

```
teacher prompt + default prompt
```

and the **user prompt** is the student's answer in Lambda Feedback.

The default prompt is fixed, and it as follows:

```
Provide feedback to the student's answer in first person.

Output your feedback, a new line, and then a boolean (True if the student is correct and False if the student is wrong). i.e., your response should be in the form:
feedback
boolean
```

The only consideration for the teacher is **teacher prompt**; this is what you input into Lambda Feedback. Some tips are to

- Speak to gpt as if you are telling someone how to mark the student's work.
- Tell gpt what the question is.
- Mention what your expected answer is.
- Mention any points that the student must include/discuss in their answer.
  - E.g. if your prompt is "Evaluate the student's response for the definition of photosynthesis. They should mention the     conversion of light energy to chemical energy", and the student enters "Photosynthesis is the process by which plants make their     food", the student will be marked as incorrect, because they have not added the required detail about energy conversion.

