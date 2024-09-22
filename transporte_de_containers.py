A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

containers_largura = X // A
containers_comprimento = Y // B
containers_altura = Z // C

total_containers = containers_largura * containers_comprimento * containers_altura

print(total_containers)