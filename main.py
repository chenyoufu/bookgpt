import argparse
import config
import os
from gpt.gpt import GPT
from loader import BOOK_LOADER_DICT
from rich import print


class Book(object):
    def __init__(self, name):
        self.name = name
        self.type = name.split(".")[-1]
        self.to_language = config.book['to_language']

    def load(self):
        book_loader = BOOK_LOADER_DICT.get(self.type)
        if not book_loader:
            raise Exception(f"book type {self.type} unsupported")
        return book_loader(options.book_name).load()

    def translate(self, gpt):
        paragraphs = self.load()
        for paragraph in paragraphs:
            print(paragraph)
            translated_text = gpt.chat_with_retry(self.to_language, paragraph)
            print("[bold green]" + translated_text + "[/bold green]")

    def summary(self):
        # 提取图书概述
        pass


def cli_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--book",
        dest="book_name",
        default="the_little_prince.txt",
        type=str,
        help="path of the book to be translated",
    )
    opts = parser.parse_args()
    if not os.path.isfile(opts.book_name):
        print(f"Error: {opts.book_name} does not exist.")
        exit(1)
    return opts


if __name__ == '__main__':
    options = cli_options()
    gpt = GPT(
        keys=config.gpt["openai_key"],
        model=config.gpt["model"],
        prompt_user=config.gpt["prompt"]["user"],
        prompt_system=config.gpt["prompt"]["system"],
        temperature=config.gpt["temperature"],
        api_base=config.gpt["api_base"],
        proxy=config.gpt["proxy"],
    )
    book = Book(options.book_name)
    book.translate(gpt)
