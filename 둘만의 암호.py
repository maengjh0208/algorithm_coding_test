def solution(s: str, skip:str, index:int) -> str:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabet_index = {c: idx for idx, c in enumerate(alphabets)}
    index_alphabet = {idx: (c, False) if c in skip else (c, True) for idx, c in enumerate(alphabets)}

    result = []
    for c in s:
        count = 0
        idx = alphabet_index[c]
        while count != index:
            idx = (idx + 1) % 26

            next_c, is_valid = index_alphabet[idx]
            if is_valid:
                count += 1

        result.append(index_alphabet[idx][0])

    return "".join(result)


if __name__ == "__main__":
    result = solution("aukks", "wbqd", 5)

    print(result)
    print(result == "happy")