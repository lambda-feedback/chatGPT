import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

default_prompt = "You are an AI based on an online learning platform. Provide feedback to the student in first person. Output your answer in exactly and only the following format: {\n'is_correct': <bool>,\n'feedback':'<string>',\n'warnings': <array>}. Follow the python syntax rules in this output."

def evaluation_function(response, prompt, parameters):
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
    print(chat_response)
    output = eval(chat_response)
    return output
