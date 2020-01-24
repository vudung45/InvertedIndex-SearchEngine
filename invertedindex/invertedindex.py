from typing import List, Iterable, Dict
from math import log2
import copy

from invertedindex import HashMapVector


class Document:
    def __init__(self, name: str, words: List[str]):
        self.name = name
        self.words = words

class InvertedIndex:
    """
        A specialized datastructure utilizing hashmapvector to quickly
        retrieve relevant documents in a corpus given a tokenized query string
    """
    def __init__(self, documents: Iterable[Document]) -> None:
        self.documents = documents
        self.doc_hmvs = {}
        self.idfs = {}
        self._construct_hmvs()
        self._calculate_idfs()
        self._normalize_hmvs()

    def _construct_hmvs(self):
        self.doc_hmvs = {}
        for document in self.documents:
            self.doc_hmvs[document.name] = HashMapVector.construct_from_words(document.words)

    def _calculate_idfs(self):
        self.idfs = {}

        # iterate through each document and calculate dfi for each token i
        # dfi: the number of documents containing token i
        for document in self.documents:
            for word in document.words:
                if word not in self.idfs:
                    self.idfs[word] = 0
                self.idfs[word] += 1

        # idf = log2(N / dfi) where N is the number of documents 
        # and dfi is the number of documents containing token i
        for word in self.idfs:
            self.idfs[word] = log2(len(self.documents) / self.idfs[word])


    def _normalize_hmvs(self):
        for document in self.documents:
            hmv = self.doc_hmvs[document.name]
            # multiply each term frequency weight with its corresponding idf weight
            for word in hmv.weights:
                hmv.weights[word] *= self.idfs[word] if word in self.idfs else 0


    def retrieve(self, words: List[str], threshold = 0.1) -> List[str]: 
        """
            @params:
                words  tokenized query string
            @return:
                List of tuple representing top ranked documents
                (score, DOCUMENT_NAME)
        """
        query_vector = HashMapVector.construct_from_words(words)
        #multiply each term frequency weight with its corresponding idf weight
        for word in query_vector.weights:
            query_vector.weights[word] *= self.idfs[word] if word in self.idfs else 0

        query_vector.normalize()

        return [result for result in \
                    sorted(((query_vector.cossine_sim(self.doc_hmvs[document.name]), document.name) \
                    for document in self.documents), reverse=True) if result[0] > threshold]

# tests
if __name__ == "__main__":
    print("-- Test 1 ---\nDoc1: this is test number one\nDoc2: this is test number two")
    documents  = [Document("Doc1", ["this", "is", "test", "number", "one"]), Document("Doc2", ["this", "is", "test", "number", "two"])]
    index = InvertedIndex(documents)
    print(f'Testing with query: number one. Rankings: {index.retrieve(["number", "one"])}')
    print(f'Testing with query: number one. Rankings: {index.retrieve(["number", "two"])}')








        