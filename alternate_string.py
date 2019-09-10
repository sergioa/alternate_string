import itertools


def alternate_string(string):
    max_alternate = 0
    aggregate = 0
    for char, group in itertools.groupby(string):
        group_len = len(list(group))
        if group_len > 2:
            if aggregate > 0:
                aggregate = aggregate + 2
                if max_alternate < aggregate:
                    max_alternate = aggregate
            aggregate = 2
        else:
            aggregate = aggregate + group_len
    return max_alternate



if __name__ == "__main__":
    print(alternate_string("baaabbaabbb"))
