from openai import OpenAI
import os
from dotenv import load_dotenv
import yaml
# import anthropic


#TODO: code clean up
def get_response_openai(messages, settings):
    """
    Function to generate response from openAI's API
    :param prompt: input prompt
    :return: respond string
    """
    model_engine = settings["model_engine"]
    client = OpenAI(api_key=os.environ.get('OPENAI_API'))
    completion = client.chat.completions.create(model=model_engine,
    messages=messages)
    completion = client.chat.completions.create(model=model_engine,
    messages=messages)
    # print(completion)
    message = completion.choices[0].message.content
    return message


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]


#TODO: code clean up
# def get_response_claude(prompt):
#     api_key = os.environ.get("ANTHROPIC_API_KEY")
#     client = anthropic.Anthropic(api_key=api_key)
#     message = client.messages.create(
#     model="claude-3-opus-20240229",
#     max_tokens=1000,
#     temperature=0,
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": prompt
#                 }
#                 ]
#             }
#         ]
#     )
#     return message.content[0].text


def get_settings(yaml_file):
    """
    Function to load settings, e.g., prompts from yaml file.
    """
    with open(yaml_file, "r") as f:
        settings = yaml.load(f, Loader=yaml.SafeLoader)
    return settings


def main():
    load_dotenv()
    yaml_file = "./prompts.yaml"
    prompt = "generate a joke with one sentence"
    # reply = get_response_claude(prompt)
    messages_openai = [
        {"role": "user", "content": prompt}
    ]
    settings = get_settings(yaml_file)
    reply = get_response_openai(messages_openai, settings)
    print(reply)


if __name__ == '__main__':
    main()
