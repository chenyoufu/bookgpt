gpt = {
    "debug": False,

    "openai_keys": [
        "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",
    ],
    "model": "gpt-3.5-turbo",
    "temperature": 1.0,
    "api_base": "https://proxy.5aitool.com/v1",
    "proxy": "",

    "prompt": {
        "system": "You are a professional translator.",
        "user": "Translate the given text to {language}. Be faithful or accurate in translation. Make the translation readable or intelligible. Be elegant or natural in translation. If the text cannot be translated, return the original text as is. Do not translate person's name. Do not add any additional text in the translation. The text to be translated is:\n{text}"
    }
}

book = {
    "test": True,
    "to_language": "zh-hans"
}
