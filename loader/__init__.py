from loader.epub_loader import EPUBBookLoader
from loader.txt_loader import TXTBookLoader
from loader.srt_loader import SRTBookLoader

BOOK_LOADER_DICT = {
    "epub": EPUBBookLoader,
    "txt": TXTBookLoader,
    "srt": SRTBookLoader,
    # TODO add more here
}
