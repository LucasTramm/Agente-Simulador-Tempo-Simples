#Crie um agente simples em Python que:
#Percebe o Clima (simulado)
#Decide se leva ou não um guarda-chuva
# Exemplo de percepção: "sol", "chuva", "nublado"

import random 

class agente_clima:
    def __init__(self):
        self.percepcao = None
#Inicializa a percepção do clima

    def perceber_clima(self):
        # Simula a percepção do clima
        self.percepcao = random.choice(["sol", "chuva", "nublado"])
        print(f"Clima percebido: {self.percepcao}")

    def decidir(self):
        if self.percepcao == "sol":
            return "Não levar guarda-chuva"
        elif self.percepcao == "chuva":
            return "Levar guarda-chuva"
        elif self.percepcao == "nublado":
            return "Levar guarda-chuva para garantir"
        else:
            return "Clima desconhecido"
#Decide se levar ou não o guarda-chuva com base na percepção
        
    def agir(self):
        self.perceber_clima()
        decisao = self.decidir()
        print(decisao)
# Executa o ciclo de percepção e decisão, e imprime a decisão


# uso do agente
if __name__ == "__main__":
    #Cria uma instância do agente
    agente = agente_clima()
    #Repete o cilco de agir 5 vezes
    for _ in range(5):
        agente.agir()
