class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        
        # Pré-calcula as potências de power módulo modulo
        p_powers = [1] * k
        for i in range(1, k):
            p_powers[i] = (p_powers[i-1] * power) % modulo
        
        # Calcula o hash da última substring de tamanho k
        current_hash = 0
        for i in range(n - k, n):
            char_val = ord(s[i]) - ord('a') + 1
            current_hash = (current_hash + char_val * p_powers[i - (n - k)]) % modulo
        
        # Encontra a primeira substring com hashValue da direita para esquerda
        result_index = n - k if current_hash == hashValue else -1
        
        # Rolling hash: processa da direita para esquerda
        for i in range(n - k - 1, -1, -1):
            # Remove o caractere mais à direita
            right_char_val = ord(s[i + k]) - ord('a') + 1
            current_hash = (current_hash - right_char_val * p_powers[k-1]) % modulo
            
            # Multiplica por power 
            current_hash = (current_hash * power) % modulo
            
            # Adiciona o novo caractere à esquerda
            left_char_val = ord(s[i]) - ord('a') + 1
            current_hash = (current_hash + left_char_val) % modulo
            
            # Corrige valores negativos do módulo
            if current_hash < 0:
                current_hash += modulo
                
            if current_hash == hashValue:
                result_index = i
        
        return s[result_index:result_index + k]
