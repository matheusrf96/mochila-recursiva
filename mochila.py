#coding: utf-8

def mochila(val, pes, item, cap): 
	if(item == 0 or cap == 0): 
		return 0 
	else:
		if(pes[item - 1] > cap): 
			return mochila(val, pes, item - 1, cap) 
		else: 
			return max( 
				val[item - 1] + mochila(val, pes, item - 1, cap - pes[item - 1]), 
				mochila(val, pes, item-1, cap) 
			)

def defValores(val, pes): 
	quant = input("Insira a quantidade de itens: ",)
	print
	for j in range(2):
		if j == 0:
			for i in range(quant):
				print "Insira o valor do item " + str(i + 1) + ": ",
				aux = input()
				val.append(aux) 
			print
		else:
			for i in range(quant):
				print "Insira o peso do item " + str(i + 1) + ": ",
				aux = input() 
				pes.append(aux) 
			print

	cap = input("Insira a capacidade da mochila: ",) 
	print
	return cap 			
	
valor = [] 
peso = []
caminho = []
nome = [] 

#Exemplo:
	#Capacidade da mochila: 30;
	#Quantidade: 5;
   	#Valor: {20, 100, 50, 5, 30};
  	#Peso: {5, 19, 11, 1, 20};
 	
	#Resultado no melhor caso: 150

capacidade = defValores(valor, peso) 
print "Valor máximo: ", mochila(valor, peso, len(valor), capacidade) 


