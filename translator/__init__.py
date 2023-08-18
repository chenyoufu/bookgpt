from translator.chatgptapi_translator import ChatGPTAPI
from translator.gpt4_translator import GPT4
from translator.claude_translator import Claude

MODEL_DICT = {
    "gpt": ChatGPTAPI,
    "gpt4": GPT4,
    "claude": Claude,
}
