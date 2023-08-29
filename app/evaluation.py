import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

default_prompt = """
Provide feedback to the student's answer in first person.

Output your feedback, a new line, and then a boolean (True if the student is correct and False if the student is wrong). i.e., your response should be in the form:
feedback
boolean
"""

def evaluation_function(response, prompt, parameters, counter = 0):
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - 'response' which contains the student's answer.
    - 'prompt' which contains the teacher's prompt
    - 'parameters' is a dictionary which contains the 'model' parameter

    The output of this function is what is returned as the API response 
    and therefore must be JSON-encodable. It must also conform to the 
    response schema.

    Any standard python library may be used, as well as any package 
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or 
    split into many) is entirely up to you. All that matters are the 
    return types and that evaluation_function() is the main function used 
    to output the evaluation response.
    """

    openai.api_key = "sk-"

    completion = openai.ChatCompletion.create(
        model = parameters['model'],
        messages = [{"role": "system", "content": prompt + default_prompt},
            {"role": "user", "content": response}]
    )

    chat_response = completion.choices[0].message.content

    # Remove any empty lines from the chat response 
    lines = chat_response.splitlines ()
    lines = [line for line in lines if line.strip ()]
    chat_response = "\n".join (lines)

    # Split the chat response by newline and strip any whitespace
    chat_response_list = chat_response.split("\n")
    chat_response_list = [x.strip() for x in chat_response_list]

    # Checks if 'chat_response_list' contains 2 items (feedback and bool)
    if len(chat_response_list) != 2:
        if counter >= 10: 
            return 
        return evaluation_function(response, prompt, parameters, counter + 1)
        

    # Assign the bool and feedback string to the output dictionary
    output = {}
    output['feedback'] = chat_response_list[0]
    output['is_correct'] = eval(chat_response_list[1])

    return output