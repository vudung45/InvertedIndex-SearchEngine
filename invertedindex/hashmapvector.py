from typing import List
import copy


class HashMapVector:
    def __init__(self: None, weights=None) -> None:
        if weights:
            self.weights = weights
        else:
            self.weights = {}

    @classmethod
    def construct_from_words(cls, words: List[str]) -> "HashMapVector":
        hmv = HashMapVector()
        for word in words:
            hmv.add_key(word)
        return hmv


    def add_key(self: None, key: str) -> None:
        if key not in self.weights:
            self.weights[key] = 0
        self.weights[key] += 1

    def normalize(self: None) -> None:
        if not self.weights:
            return
        max_freq = max(self.weights.values())
        for key in self.weights:
            self.weights[key] /= max_freq

    # dot product
    def dot(self: None, rhs: "HashMapVector") -> float:
        return sum(self.weights[key] * rhs.weights[key] for key in self.weights if key in rhs.weights)

    def length(self: None) -> float:
        return sum(val**2 for val in self.weights.values())**(1/2)

    # cossine similarity between 2 vectors
    def cossine_sim(self: None, rhs: "HashMapVector") -> float:

        length_rhs = sum(rhs.weights[token]**2 for token in rhs.weights if token in self.weights)**(1/2)
        if self.length() == 0.0 or length_rhs == 0.0:
            return 0
        return self.dot(rhs) / (self.length() * length_rhs)


if __name__ == "__main__":
    # insert unit test here
    pass
