class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        return self.ajudaDecodificacao(s, 0, memo)

    def ajudaDecodificacao(self, s, index, memo):
        # Se já chegamos ao final da string, retornamos 1 para a solução
        if index == len(s):
            return 1

        # Se o caractere atual for '0', não podemos decodificá-lo
        if s[index] == '0':
            return 0

        # Se já calculamos a solução para este subproblema, retornamos o resultado
        if memo[index] != -1:
            return memo[index]

        # Caso contrário, calculamos a solução
        resultado = self.ajudaDecodificacao(s, index + 1, memo)

        # Se o próximo caractere formar um número válido com o atual, adicionamos o número de decodificações do restante da string
        if index < len(s) - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] < '7')):
            resultado += self.ajudaDecodificacao(s, index + 2, memo)

        # Armazenamos a solução no memo e a retornamos
        memo[index] = resultado
        return resultado