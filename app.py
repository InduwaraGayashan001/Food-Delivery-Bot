import chainlit as cl
from src.llm import ask_llm, messages

@cl.on_message
async def on_message(message: cl.Message):
    messages.append(
        {
            "role": "user",
            "content": message.content,
        }
    )
    response = ask_llm(messages)
    messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
    await cl.Message(response).send()