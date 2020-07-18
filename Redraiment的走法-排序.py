'''
题目描述
   Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，但走的步数最多，不知道为什么？你能替Redraiment研究他最多走的步数吗？
样例输入
6
2 5 1 5 4 5
样例输出
3
提示
Example:
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5
从第5格开始走最多有2步,4 5

所以这个结果是3。
'''
while True:
    try:
        n = int(input())
        b = list(map(int, input().split())) # 默认空格切割
        dp = [1] * n # 到自己，默认一步

        for i in range(1, n):  # 到
            for j in range(i):
                if b[j] < b[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = max(dp)
        print(res)

    except:
        break