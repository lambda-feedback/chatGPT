# YourFunctionName
This evaluation function allows response areas to be marked (true/false with feedback) via openAI models. 

To run this code, you need to enter your openAI API key into openai.api_key ="" in evaluation.py.

## Inputs
*Specific input parameters which can be supplied when the `eval` command is supplied to this function.*

## Outputs
*Output schema/values for this function*
```
{'feedback': string,
'is_correct': bool}
```

## Examples
*List of example inputs and outputs for this function, each under a different sub-heading*

### Capital city

```python
prompt = "Analyze the response regarding the capital of France"
        response = "The capital of France is Berlin."
        parameters = {'model': 'gpt-3.5-turbo'}
        output = evaluation_function(response, prompt, parameters)
```

```python
{'feedback': 'Good job! Paris is indeed the capital of France. However, it is not the largest city in the world. Keep up the good work!',
'is_correct': False}
```
