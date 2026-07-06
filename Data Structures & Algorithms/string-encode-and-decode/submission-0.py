class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []

        for seq in strs:
            final.append(str(len(seq)) + ">" + seq)

        return "".join(final)

    def decode(self, s: str) -> List[str]:

        strs = []
        pntr = 0

        while pntr < len(s):

            j = pntr
            while s[j] != ">":
                j += 1

            length = int(s[pntr:j])

            word = s[j + 1 : j + 1 + length]
            strs.append(word)

            pntr = j + 1 + length

        return strs