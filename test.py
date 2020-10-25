class Solution:
    def overlap(self, a, b):
        na, nb = len(a), len(b)
        for i in range(min(na, nb), 0, -1):
            if a[na - i:] == b[0:i]:
                return i
        return 0

    def shortestSuperstring(self, A:[str]) -> str:
        INF = 0x3f3f3f3f
        n = len(A)
        M = 1 << n
        o = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                o[i][j] = self.overlap(A[i], A[j])
        dp = [[INF] * n for _ in range(M)]
        path = [[0] * n for _ in range(M)]
        for i in range(n):
            dp[1 << i][i] = len(A[i])
        for s in range(M):
            for i in range(n):
                if s ^ (1 << i) == 0:
                    continue
                for j in range(n):
                    if i != j and ((s >> j) & 1):
                        if dp[s][i] > dp[s ^ (1 << i)][j] + len(A[i]) - o[j][i]:
                            dp[s][i] = dp[s ^ (1 << i)][j] + len(A[i]) - o[j][i]
                            path[s][i] = j
        last = 0
        for i in range(1, n):
            if dp[M - 1][i] < dp[M - 1][last]:
                last = i
        seq = [last]
        s = M - 1
        for _ in range(n - 1):
            tmp = last
            last = path[s][last]
            seq.append(last)
            s = s ^ (1 << tmp)
        seq = seq[::-1]
        res = A[seq[0]]
        for i in range(1, n):
            res += A[seq[i]][o[seq[i - 1]][seq[i]]:]
        return res
if __name__ == '__main__':

 s=Solution()
 #res=s.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])

 res = s.shortestSuperstring(['ATGT', 'CCGT', 'CGTC', 'CTTG', 'GTCC', 'GTCT', 'TCCG', 'TCTT', 'TGTC'])
 print(res)