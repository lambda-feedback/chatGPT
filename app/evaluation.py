import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

def evaluation_function(response, answer, parameters, counter=0):
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - 'response' which contains the student's answer
    - 'prompt' which contains the teacher's prompt
    - 'parameters' is a dictionary which contains the 'model' parameter, the 'prompt' parameter and the 'default_prompt' parameter.

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

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    # Call openAI API
    completion = openai.ChatCompletion.create(
        model=parameters['model'],
        messages=[{"role": "system", "content": parameters['prompt'] + parameters['default_prompt']},
                  {"role": "user", "content": response}]
    )

    chat_response = completion.choices[0].message.content

    # Split the chat_response string by the vertical bar and strip any extra spaces
    parts = chat_response.split("|")
    boolean = parts[0].strip()
    feedback = parts[1].strip()

    # Convert the boolean string to a boolean value
    is_correct = boolean == "True"

    # Create the output dictionary
    output = {"feedback": feedback, "is_correct": is_correct}

    return output
