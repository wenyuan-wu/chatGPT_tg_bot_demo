import openai
import os


def get_response_openai(prompt):
    """
    Function to generate response from openAI's API
    :param prompt: input prompt
    :return: respond string
    """
    openai.api_key = os.environ.get('OPENAI_API')
    # set the model and prompt
    model_engine = "gpt-3.5-turbo"
    # set the maximum number of tokens to generate in the response
    max_tokens = 1024
    # generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # return the response
    return completion.choices[0].text


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]
