def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
      mid = left + (right - left) // 2

      # Verifica se o elemento do meio é o alvo
      if arr[mid] == target:
          return mid
      # Se o alvo estiver na metade esquerda, descarte a metade direita
      elif arr[mid] > target:
          right = mid - 1
      # Se o alvo estiver na metade direita, descarte a metade esquerda
      else:
          left = mid + 1

  # Se o elemento não estiver presente no array
  return -1

# Exemplo de uso:
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)

if result != -1:
  print("Elemento encontrado no índice:", result)
else:
  print("Elemento não encontrado no array.")
