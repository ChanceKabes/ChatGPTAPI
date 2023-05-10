import openai
import gradio as gr
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "Tell a Joke"}]

def CustomChatGPT(Topic):
    messages.append({"role": "user", "content": Topic})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = gr.Textbox(lines=1, placeholder = "Joke Topic..."), outputs = gr.Textbox(label="Joke"), title = "Joke Teller", allow_flagging = "never")

demo.launch(share=False)