import sys 
def solve(large, small):
    for i in range(1, n):
        large = [
            max(large[0],large[1])+table[i][0],
            max(large[0],large[1],large[2])+table[i][1],
            max(large[1],large[2])+table[i][2]
            ]

        small = [
            min(small[0],small[1])+table[i][0],
            min(small[0],small[1],small[2])+table[i][1],
            min(small[1],small[2])+table[i][2]
        ]

    return max(large), min(small)

        




if __name__ == "__main__":
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(n)]
    large = small = table[0]
    largest = solve(large,small)[0]
    smallest = solve(large,small)[1]
    print(largest, smallest)




