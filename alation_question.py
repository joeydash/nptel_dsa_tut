# def solution(strings):
#     if not strings:
#         return ''
#     s1 = min(strings)
#     s2 = max(strings)
#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i]
#     return s1
#
#
# print(solution(["abc", "abcd", "abcnssn"]))


# def solution(prices):
#     profit = [0]
#     for i in range(len(prices)-1):
#         profit = profit + [max(prices[i+1:])-prices[i]]
#     return max(profit)
#
# print(solution([6,0,-1,10]))


def solution(words, width):
    words_total_length = 0
    result_array = []
    temp_words_array = []
    temp_string = ""
    for word in words:
        if words_total_length + len(word) < width:
            temp_words_array = temp_words_array + [word]
            words_total_length = words_total_length + len(word)
        else:
            for i in range(len(temp_words_array)):
                if i != len(temp_words_array)-1:
                    temp_string = temp_string + "{" + str(i) + ":" + str(
                        (width - words_total_length) // (len(temp_words_array) - 1)) + "}"
                else:
                    temp_string = temp_string + "{" + str(i) + ":" + str(i) + "}"
            # result_array = result_array + [temp_string.format(*temp_words_array)]
                    print(temp_words_array)

                    # print(temp_string.format(*temp_words_array))
    return result_array


solution(["All", "happy", "families", "are", "alike", "every", "unhappy", "family", "is", "unhappy", "in", "its", "own",
          "way"], 20)

# print("Location: {0:20} Revision {1}".format("hello", "world"))
