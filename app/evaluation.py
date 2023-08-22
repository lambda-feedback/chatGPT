import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

def evaluation_function(prompt, response):
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `prompt' which contains the system prompt, written by the teacher.
    - `response` which contains the student's answer.

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
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
            {"role": "user", "content": response}]
    )

    chat_response = completion.choices[0].message.content
    return chat_response
