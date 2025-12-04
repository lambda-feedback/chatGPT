# chatGPT

## What does it do?
This chatGPT evaluation function is designed to automatically evaluate student responses to questions. It currently uses the OpenAI API to determine the correctness (true/false) of the student's answer and can also provide them with feedback.

## What does the teacher need to input?
- `Model`
    - Suggest (July 2025), `gpt-4o-mini` or `gpt-4.1-mini`. 
-  `Main_prompt`
    - In this prompt you should explain the question and answer to gpt.
    
-  `Default_prompt` [do not change from default]
    - To determine the completeness of the response. 
    - It tells GPT to output a Boolean, which marks the student's answer as correct (complete) or incorrect (incomplete).

-  `Feedback_prompt`  [optional]
    - Leave this prompt **blank** if you do not want any textual/qualitative feedback to be given to the student.
    - Fill in this prompt to tell gpt how to give written feedback to the student. Examples of things you may want to include in your `feedback_prompt`:
        - `Give the student objective and constructive feedback on their answer in first person.`
        - `If the student is incorrect, provide feedback/hints to help them, but do not reveal the answer.`
   
The cost and performance of LLMs changes by the month, so do not assume that your prompts, and model choice, are good in the long term. Approaches with LLMs should be considered experimental.

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



