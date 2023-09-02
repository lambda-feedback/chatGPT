# chatGPT

## What does it do?
This chatGPT evaluation function is designed to automatically evaluate student responses to questions. It currently uses the openAI API to determine the correctness (true/false) of the student's answer and can also provide them with feedback.


## What does the teacher need to input?
- `Model`
  - As of now, "gpt-3.5-turbo" is the only model available. In the future, more openAI and other models can be implemented.
- `Main_prompt`
  - In this prompt you should explain the question and answer to the AI.
- `Default_prompt`
  - As of now, this prompt should not be changed.
  - It tells the AI to output a Boolean, which marks the student's answer as correct or incorrect.
  - In the future, this could be changed so that 'partially incorrect' answers, etc, are possible.
- `Feedback_prompt`
  - Leave this prompt **blank** if you do not want any textual feedback to be given to the student, but just correct/incorrect.
  - Fill in this prompt to tell the AI how to give feedback to the student. The default prompt, which works well in most cases, is:
   "You are an AI based on an online learning platform. Give the student feedback on their answer in first person."

## Usage examples
Each example below demonstrates the potential usage of `main_prompt` and `feedback_prompt` for different questions.

### Risk assessment
**Main Prompt**:
> In this question, the student must enter a risk and a short description of what harm it can cause.

**Feedback Prompt**:
> "You are an AI based on an online learning platform. Give the student objective and constructive feedback on their answer in first person"

<img src="https://github.com/lambda-feedback/chatGPT/assets/138524447/af083bff-fade-4186-89aa-bc0b7f48ce0d" width="450">

