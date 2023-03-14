# Simulador de Alocação de Leitos

O Simulador consiste de 4 arquivos, sendo eles o Simulador.py,Fila.py,
Estrutura.py e Nó.py.Começando pelo Nó, ele é basicamente a Estrutura que aprendemos 
ná sala de aula, onde ele serve como base para criar a Estrutura de Fila, cujo a qual é a Estrutura
mais importante desse programa, pois além de usada repetidas vezes, será a principal forma de 
ordenar os pacientes, além da fila ainda foi preciso criar outras duas classes, que servem para simular a 
chegada de pacientes no Hospital, ondé será explicado mais a frente como funcionam,e por fim temos o arquivos
principal, que realiza a Alocação dos pacientes em conjunto com os leitos, tendo em vista que toda vez que existe 
um leito disponível e um paciente pendente, esse paciente seria alocado para esse leito, em outras palavras, excluir ambos
do sistema.

# Ficha Técnica
O método utilizado para simular a chegada dos pacientes foi a criação de uma classe chamada "paciente", onde dentro desta classe
é usado um metodo aleatorio para escolher o nivel de gravidade e o tipo de leito em que ele precisa ser alocado.basicamente  cada paciente tem 
um numero de 3 digitos ou mais, cujo a qual o digito mais significativo(O primeiro a esquerda) representa a gravidade do paciente, onde a mesma
pode ter apenas 3 valores: 3(Urgente),4(Muito Urgente) e 5(Emergência), e o digito a direita do mais significativo representa o tipo de paciente: 0(Neonatal),1(Pediátrico) e 2(Adulto).
Os numeros depois destes representam a contagem de pacientes até o momento.

Muito semelhante ao método escolhido para simular os pacientes, o método de simular os leitos faz basicamente a mesma coisa
porém com a diferença de que ele aleatoriza apenas o tipo de leito que precisa ser escolhido, e com o mesmo metodo já explicado antes (0,1,2)


Exemplo:
O paciente "4212" teria a gravidade muito urgente e seria um Adulto.

O simulador no momento de fazer os teste repete o ciclo apenas 5 vezes, coloquei um limite de 5 para o processo não ficar tã demorado na hora de testar,
além disso a entrada máxima de pacientes e leitos por vez é de 100 de cada, metodo 

A interface Gráfica foi feita com prints na tela em comjunto com o modulo time,para uma melhor vizualização das 
informações



## Referência

 - [Referência de como usar filas](https://www.youtube.com/watch?v=tiee9D54tE0)
