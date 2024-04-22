class WG:

    MaxGuesses = 6
    Chars = 5

    def __init__(self, Ans: str):
        self.Ans: str = Ans.upper()
        self.Guesses = []
        pass

    def Guess(self, word: str):
        self.Guesses.append(word.upper())

    def trial(self, word: str):
        result = []

        for i in range(self.Chars):
            char = word.upper()[i]
            letter = Letter_Breakdown(char)
            letter.in_word = char in self.Ans
            letter.in_position = char == self.Ans[i]
            result.append(letter)

        return result

    @property
    def ans_correct(self):
        return len(self.Guesses) > 0 and self.Guesses[-1] == self.Ans

    @property
    def Guess_Remaining(self) -> int:
        return self.MaxGuesses - len(self.Guesses)

    @property
    def Can_Guess(self):
        return self.Guess_Remaining > 0 and not self.ans_correct



class Letter_Breakdown:
    def __init__(self, character: str):
        self.character: str = character
        self.in_word: bool = False
        self.in_position: bool = False

    def __repr__(self):
        return f"[{self.character} in_word:{self.in_word} in_position: {self.in_position}]"