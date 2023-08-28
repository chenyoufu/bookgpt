gpt = {
    "debug": True,
    "log": "info",

    "openai_keys": [
        # invalid
        "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",
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
    "to_language": "zh-hans"
}
