class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        self.contagemUns = [s.count('1') for s in strs]  # Conta o número de '1's em cada string
        self.dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]  # Inicializa a matriz de programação dinâmica
        return self.mochila(strs, m, n, 0)  # Inicia a função mochila

    def mochila(self, strs, m, n, i):
        if i >= len(strs):  # Se chegamos ao final da lista de strings, retornamos 0
            return 0
        if self.dp[i][m][n] != -1:  # Se já calculamos este subproblema, retornamos o resultado armazenado
            return self.dp[i][m][n]
        uns = self.contagemUns[i]  # Número de '1's na string atual
        zeros = len(strs[i]) - uns  # Número de '0's na string atual
        # Se podemos formar a string atual com os '0's e '1's disponíveis, fazemos uma escolha
        if m - zeros >= 0 and n - uns >= 0:
            self.dp[i][m][n] = max(1 + self.mochila(strs, m - zeros, n - uns, i+1), self.mochila(strs, m, n, i+1))
        else:  # Se não podemos formar a string atual, passamos para a próxima string
            self.dp[i][m][n] = self.mochila(strs, m, n, i+1)
        return self.dp[i][m][n]  # Retornamos o número máximo de strings que podemos formar
    
