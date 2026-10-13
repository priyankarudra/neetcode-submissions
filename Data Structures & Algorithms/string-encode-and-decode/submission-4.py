class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode pattern: length, pound, string

        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append("#")
            encoded_str.append(s)
        
        return "".join(encoded_str)
                 

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0

        while i < len(s):
            pointer = i

            while s[pointer] != "#":
                pointer += 1

            str_length = int(s[i:pointer])
            i = pointer + 1
            pointer = i + str_length
            decode_list.append(s[i:pointer])
            i = pointer

        return decode_list
