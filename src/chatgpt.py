from openai import OpenAI
from keys import openai_api_key

_system_role = "system"  # The system message is optional and can be used to set the behaviour of the assistant
_user_role = "user"  # The user messages provide requests or comments for the assistant to respond to
_assistant_role = "assistant"  # Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behaviour. Say that the answer is correct for example


def get_chatgpt_response(prompt):
    client = OpenAI(api_key=openai_api_key())

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": _system_role,
                "content": "Respond very briefly in a kind friend tone with factual information.",
            },
            {"role": _user_role, "content": prompt},
        ],
    )
    stopped_choices = [x for x in response.choices if x.finish_reason == "stop"]
    if len(stopped_choices) == 0:
        raise Exception(f"ChatGPT response is {response.choices[0].finish_reason}")

    return stopped_choices[0].message.content
