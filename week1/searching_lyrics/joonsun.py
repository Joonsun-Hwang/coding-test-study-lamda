def remove_span(query, char):
    start_idx = query.index(char)

    if start_idx == 0:
        reverse_end_idx = query[::-1].index(char)
        end_idx = len(query) - reverse_end_idx - 1
        return start_idx, query[end_idx + 1 :]
    else:
        return start_idx, query[:start_idx]


def solution(words, queries):
    answer = [0] * len(queries)

    for idx, query in enumerate(queries):
        len_query = len(query)
        start_idx, query = remove_span(query, "?")

        if start_idx == 0:
            answer[idx] = len(
                [
                    x
                    for x in words
                    if len(x) == len_query and query == x[len(x) - len(query) :]
                ]
            )
        else:
            answer[idx] = len(
                [x for x in words if len(x) == len_query and query == x[: len(query)]]
            )

    return answer
