from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import TextLoader
data=TextLoader(r"c:\Users\Admin HP\OneDrive\Desktop\Generative AI\RAG_projects\Text_Splitter\notes.txt")
docs=data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
)
'''
Suppose text is

ABCDEFGHIJKLMN

Without overlap

ABCDEFGHIJ
KLMN
'''

'''
Why is it called Recursive?

Because it tries one separator after another.

Whole document
        │
        ▼
Can I split by paragraphs?
        │
   Yes / No
        │
        ▼
Can I split by newlines?
        │
   Yes / No
        │
        ▼
Can I split by spaces?
        │
   Yes / No
        │
        ▼
Split character by character
'''

chunks=splitter.split_documents(docs)

print("=====================RecursiveCharacterTextSplitter======================")

print(len(chunks))
print("===========================================")
print(chunks)
print("===========================================")

for i in chunks:
    print(i.page_content)
    print(" ")
    print(" ")


'''
A token is not exactly a word.

Depending on the tokenizer, a token can be:

a whole word
part of a word
punctuation
a number
even a space in some tokenizers
'''

tok_splitter= TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2,
)

tok_chunks=tok_splitter.split_documents(docs)

print("========================TokenTextSplitter===================")
print(len(tok_chunks))
print("===========================================")
print(tok_chunks)

for i in tok_chunks:
    print(i.page_content)
    print(" ")
    print(" ")

'''
Assume the tokenizer produces these tokens:

Token No.	Token
1	Hello
2	how
3	are
4	you
5	I
6	want
7	to
8	see
9	what
10	can
11	I
12	do
13	and
14	also
15	I
16	need
17	your
18	help
19	please
20	help
21	me


With overlap (chunk_overlap=2)

Chunk 1:
Hello how are you I want to see what can
                           ↑      ↑

Chunk 2:
what can I do and also I need your help
↑      ↑

Chunk 3:
your help please help me
↑      ↑

The repeated words provide continuity between chunks.
'''