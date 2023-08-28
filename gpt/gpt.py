#!/usr/bin/env python
# coding=utf-8

import itertools
import openai
import time
from rich import print

import config

openai.debug = config.gpt.get("debug")
openai.log = config.gpt.get("log")
class GPT(object):
    def __init__(self, keys, model, prompt_user, prompt_system, temperature, api_base, proxy=None):
        self.model = model

        self.valid_keys_list = keys
        self.keys_cnt = len(keys)
        self.keys = itertools.cycle(keys)
        self.keys_stats = {key: {} for key in keys}
        self.cur_key = keys[0]

        self.prompt_user = prompt_user
        self.prompt_system = prompt_system
        self.proxy = proxy
        self.temperature = temperature

        if api_base:
            openai.api_base = api_base

    def chat_with_retry(self, language, text, retry_count=3):
        while retry_count > 0:
            try:
                return self.chat(language, text)
            except openai.error.AuthenticationError as e:
                self.keys_stats[self.cur_key]["AuthenticationError"] = self.keys_stats[self.cur_key].get("AuthenticationError", 0) + 1
                print("[bold red]" + f"Exception: {type(e)}, {e}" + "[/bold red]")
            except StopIteration as e:
                print("[bold red]" + f"Exception: {type(e)}, no valid key" + "[/bold red]")
                raise
            except Exception as e:
                # 1. openai server error or own network interruption, sleep for a fixed time
                # 2. an apikey has no money or reach limit, don`t sleep, just replace it with another apikey
                # 3. all apikey reach limit, then use current sleep
                self.keys_stats[self.cur_key][type(e)] = self.keys_stats[self.cur_key].get(type(e), 0) + 1
                sleep_time = int(60 / self.keys_cnt)
                print("Exception: ", type(e), e, f"will sleep {sleep_time} seconds")
                time.sleep(sleep_time)
                retry_count -= 1
        else:
            # 重试次数耗尽，处理失败情况
            print(f"Get {retry_count} consecutive exceptions")
            raise

    def chat(self, language, text):
        self.rotate_key()

        user_content = self.prompt_user.format(text=text, language=language)
        completion = {}

        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.prompt_system},
                    {"role": "user", "content": user_content}
                ],
                temperature=self.temperature,
            )
        except Exception as e:
            if (
                    "choices" not in completion
                    or not isinstance(completion["choices"], list)
                    or len(completion["choices"]) == 0
                    or completion["choices"][0]["finish_reason"] != "length"
            ):
                raise e

        choice = completion["choices"][0]
        t_text = choice.get("message").get("content", "").encode("utf8").decode()

        if choice["finish_reason"] == "length":
            with open("log/long_text.txt", "a") as f:
                f.write(f"""==================================================
                The total token is too long and cannot be completely translated:\n
                {text}\n\n""")

        return t_text

    def rotate_key(self):
        key = next(self.keys)

        if self.key_is_invalid(key):
            self.valid_keys_list.remove(key)
            self.keys = itertools.cycle(self.valid_keys_list)
            self.keys_cnt = len(self.valid_keys_list)
            key = next(self.keys)

        self.cur_key = key
        openai.api_key = key
        return key

    def key_is_invalid(self, key):
        return self.keys_stats[key].get("AuthenticationError", 0) >= 3
