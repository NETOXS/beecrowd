def resultado_instancia(frase, time1, time2):
    list_frase = list(frase)
    list_time1 = list(time1)
    list_time2 = list(time2)
    result1 = 0
    result2 = 0
    primeiro_erro_time1 = -1
    primeiro_erro_time2 = -1
    
    for i in range(len(frase)):
        if list_frase[i] == list_time1[i]:
            result1 += 1
        elif primeiro_erro_time1 == -1: 
            primeiro_erro_time1 = i
        if list_frase[i] == list_time2[i]:
            result2 += 1
        elif primeiro_erro_time2 == -1: 
            primeiro_erro_time2 = i
            
    if result1 > result2:
        return "time 1"
    elif result1 < result2:
        return "time 2"
    else:
        if primeiro_erro_time1 < primeiro_erro_time2:
            return "time 1"
        elif primeiro_erro_time1 > primeiro_erro_time2:
            return "time 2"
        else:
            return "empate"
               
t = int(input())

for i in range(t):
    frase = input()
    time1 = input()
    time2 = input()
    vencedor = resultado_instancia(frase, time1, time2)
    
    print(f"Instancia {i + 1}")
    print(vencedor)
    print()