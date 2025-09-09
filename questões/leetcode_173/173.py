# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Pilha para armazenar os nós durante a travessia
        self.stack = []
        # Inicializa a pilha com todos os nós à esquerda a partir da raiz
        self._push_all_left(root)
    
    def _push_all_left(self, node):
        # Percorre até o nó mais à esquerda, empilhando todos os nós no caminho
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Remove o último nó adicionado à pilha (mais à esquerda disponível)
        node = self.stack.pop()
        # Se este nó tiver subárvore direita, processa todos os nós à esquerda dela
        if node.right:
            self._push_all_left(node.right)
        # Retorna o valor do nó atual
        return node.val

    def hasNext(self) -> bool:
        # Verifica se ainda há nós na pilha para processar
        return len(self.stack) > 0
