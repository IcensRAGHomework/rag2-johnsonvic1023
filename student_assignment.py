from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    pages = loader.load()

    # print(len(pages))

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    chunks = text_splitter.split_documents(pages)

    last_chunk = chunks[-1]

    return last_chunk

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    pages = loader.load()

    full_text = "\n".join([page.page_content for page in pages])

    # full_text = ""
    # for index, page in enumerate(pages):
    #     full_text = "".join(page.page_content)
    #     if index == 2:
    #         break

    # print(full_text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1,
        chunk_overlap=0,
        separators=[r"第.+(?:條 *|章 .*)(?:\n|-)"],
        is_separator_regex=True,
        keep_separator=True
    )

    chunks = splitter.split_text(full_text)

    # debug usage
    # count = 0
    # for chunk in chunks:
    #     print(chunk)
    #     print("--------------------------------------")
    #     count += 1
    #     if count == 13:
    #         break

    return len(chunks)

# if __name__ == '__main__':
#     result = hw02_1(q1_pdf)
#     print("---------------------- hw1 result ----------------------")
#     print(result)
#     print(f"檔名: {result.metadata['source']}")
#     print(f"頁數: {result.metadata['page'] + 1}")
#     print(f"內文: {result.page_content}")

#     result = hw02_2(q2_pdf)
#     print("---------------------- hw2 result ----------------------")
#     print(result)
