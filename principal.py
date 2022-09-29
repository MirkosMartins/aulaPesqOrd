import streamlit as st

def ordena(lista):
  t = len(lista)
  i=0
  j=0
  while j<t-1 and t>1:
    while i<t-1:
      if lista[i]>lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]#troca
      i+=1
    i=0
    j+=1

nomes = [] #lista para guardar os nomes
resposta = ''
while resposta != 'SAIR':
  #resposta = input('Digite o nome: ').upper()
  resposta = st.text_input('Digite o nome: ',key='resp')
  if resposta != 'SAIR':
    nomes.append(resposta)#colocou em ultimo
  ordena(nomes)
  st.write(nomes)

#nomes.pop()#exclui o ultimo da lista - 'sair'
st.write(nomes)
