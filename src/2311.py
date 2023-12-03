import math

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        def dp(s, index, k, val, memo, power):
            # Caso base: se o índice for -1, retorne 0
            if index == -1:
                return 0
            # Se já calculamos este subproblema antes, retorne o resultado armazenado
            if (index, val) in memo:
                return memo[(index, val)]
            # Inicialize a resposta como -infinito
            ans = -math.inf
            # Calcule o novo valor
            new_val = 2**power * int(s[index])
            # Escolha incluir este valor
            if val + new_val <= k:
                # Calcule a resposta local se incluirmos este valor
                loc_ans = 1 + dp(s, index - 1, k, val + new_val, memo, power + 1)
                # Atualize a resposta se a resposta local for maior
                ans = max(loc_ans, ans)
            # Pule este valor
            else:
                # Calcule a resposta local se pulamos este valor
                loc_ans = dp(s, index - 1, k, val, memo, power)
                # Atualize a resposta se a resposta local for maior
                ans = max(loc_ans, ans)
            # Armazene a resposta para este subproblema no memo
            memo[(index, val)] = ans
            # Retorne a resposta
            return ans
        # Chame a função dp para o problema completo
        return dp(s, len(s) - 1, k, 0, {}, 0)