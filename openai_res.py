from openai import OpenAI
import os
# import anthropic


def get_response_openai(prompt):
    """
    Function to generate response from openAI's API
    :param prompt: input prompt
    :return: respond string
    """
    # set the model and prompt
    # model_engine = "gpt-3.5-turbo-16k-0613"
    # model_engine = "gpt-4-turbo-preview"
    # model_engine = "o1-preview"
    model_engine = "gpt-4o-mini"
    # set the maximum number of tokens to generate in the response
    # max_tokens = 1024
    # generate a response
    client = OpenAI(api_key=os.environ.get('OPENAI_API'))
    completion = client.chat.completions.create(model=model_engine,
    messages=prompt)
    # return the response

    # # set the model and prompt
    # model_engine = "gpt-3.5-turbo"
    # # set the maximum number of tokens to generate in the response
    # max_tokens = 1024
    # # generate a response
    # completion = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=max_tokens,
    #     temperature=0.5,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    # # return the response

    return completion.choices[0].message.content


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]


def get_response_claude(prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
                ]
            }
        ]
    )
    return message.content[0].text


def main():
    prompt = "generate a joke with one sentence"
    # reply = get_response_claude(prompt)
    prompt_openai = [
        {"role": "user", "content": prompt}
    ]
    reply = get_response_openai(prompt_openai)
    print(reply)


if __name__ == '__main__':
    main()
