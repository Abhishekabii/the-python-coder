'''2.  Given an array print all the numbers that are repeating in it
and the number of times they are repeating.

Below is an example:

Input: [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
Output:
1 - 4
2 - 2
5 - 3
8 - 2
4 - 2

Note: The final order of output need not be the same as above.
The number after the dash(-) is the repeating count'''




lisst=[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]


def count_repeat(inp_list):
    count_rep={i:0 for i in lisst}
    for i in lisst:
        if i in count_rep:
            count_rep[i]+=1
    for k,v in count_rep.items():
        if v>1:
            print(k,'-',v)



count_repeat(lisst)
