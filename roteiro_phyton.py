import os

# ============================================================
#   ROTEIRO TURÍSTICO INTELIGENTE - FLORIANÓPOLIS
#   Projeto SENAC - Sistema de Recomendação Turística
# Alunas: Maria Luiza Dalsasso, Nahyara Miranda, Raphaela Barreto
# ============================================================

# 1. BASE DE DADOS (Substituindo múltiplos vetores por Dicionários)
locais = [
    {
        "nome": "Mercado Público Municipal",
        "tipo": "gastronomia",
        "subtipo": "frutos do mar",
        "regiao": "centro",
        "preco": "$$",
        "descricao": "Ícone de Floripa com barracas de frutos do mar e lojas típicas.",
        "pet_friendly": False,
        "acessivel": True,
        "ordem_visita": 1
    },
    {
        "nome": "Praia da Joaquina",
        "tipo": "praia",
        "subtipo": "",
        "regiao": "leste",
        "preco": "Gratuito",
        "descricao": "Famosa pelas dunas de areia e ondas perfeitas para o surfe.",
        "pet_friendly": True,
        "acessivel": False,
        "ordem_visita": 2
    },
    {
        "nome": "Fortaleza de São José da Ponta Grossa",
        "tipo": "historia",
        "subtipo": "",
        "regiao": "norte",
        "preco": "Gratuito",
        "descricao": "Fortificação do século XVIII com vista deslumbrante para o mar.",
        "pet_friendly": False,
        "acessivel": True,
        "ordem_visita": 1
    },
    {
        "nome": "Santo Antônio de Lisboa",
        "tipo": "historia",
        "subtipo": "",
        "regiao": "norte",
        "preco": "Gratuito",
        "descricao": "Vilarejo açoriano preservado, com ostras frescas e pôr do sol incrível.",
        "pet_friendly": True,
        "acessivel": True,
        "ordem_visita": 2
    },
    {
        "nome": "Rua Felipe Schmidt",
        "tipo": "compras",
        "subtipo": "", # Adicionado vírgula faltante
        "regiao": "centro",
        "preco": "gratuito",
        "descricao": "Principal calçadão de compras do centro, com lojas e artesanato.", # Corrigido 'dercricao' para 'descricao'
        "pet_friendly": False, # Adicionado vírgula faltante
        "acessivel": True, # Adicionado vírgula faltante
        "ordem_visita": 1
    },
    # Os outros locais entram aqui seguindo o mesmo padrão...
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def filtrar_roteiro():
    limpar_tela()
    print("==================================================")
    print("      CONFIGURAÇÃO DO SEU ROTEIRO EM FLORIPA      ")
    print("==================================================\n")
    
    # Seleção de Múltiplas Regiões
    print("Selecione as regiões desejadas (separe por vírgula se quiser mais de uma):")
    print("1 - Centro\n2 - Norte\n3 - Sul\n4 - Leste\n5 - Lagoa\n6 - Continente")
    regiao_op = input("Digite as opções (ex: 1,3,5) ou '0' para todas: ")
    
    mapeamento_regioes = {
        "1": "centro", "2": "norte", "3": "sul", 
        "4": "leste", "5": "lagoa", "6": "continente"
    }
    
    # Processa a entrada do usuário para gerar uma lista de regiões
    regioes_escolhidas = []
    
    # Se digitar '0' ou vazio, considera todas as regiões (lista vazia significa "não filtrar por região")
    if regiao_op.strip() != "0" and regiao_op.strip() != "":
        # Divide a string pelas vírgulas e remove espaços extras de cada número
        opcoes = [opcao.strip() for opcao in regiao_op.split(",")]
        for op in opcoes:
            if op in mapeamento_regioes:
                regioes_escolhidas.append(mapeamento_regioes[op])

    # Filtros de Acessibilidade e Pet
    quer_pet = input("\nDeseja locais Pet Friendly? (S/N): ").strip().upper() == 'S'
    quer_acesso = input("Necessita de acessibilidade motora? (S/N): ").strip().upper() == 'S'
    
    # 2. FILTRAGEM INTELIGENTE
    roteiro = []
    for local in locais:
        # Validar múltiplas regiões: se a lista não estiver vazia, o local precisa estar nela
        if regioes_escolhidas and local["regiao"] not in regioes_escolhidas:
            continue
        # Validar Pet Friendly
        if quer_pet and not local["pet_friendly"]:
            continue
        # Validar Acessibilidade
        if quer_acesso and not local["acessivel"]:
            continue
            
        roteiro.append(local)
    
    # Ordenar o roteiro com base no atributo 'ordem_visita'
    roteiro.sort(key=lambda x: x["ordem_visita"])
    
    # 3. EXECUÇÃO DO ROTEIRO (Modo interativo)
    if not roteiro:
        print("\n[!] Nenhum local encontrado com os filtros selecionados.")
        input("\nPressione Enter para voltar...")
        return

    total_paradas = len(roteiro)
    for idx, local in enumerate(roteiro):
        limpar_tela()
        print(f"=== PARADA {idx + 1} de {total_paradas} ===")
        print(f"Nome: {local['nome']}")
        print(f"Tipo: {local['tipo'].capitalize()}")
        print(f"Preço: {local['preco']}")
        print(f"Descrição: {local['descricao']}")
        
        if local['pet_friendly']:
            print("  [*] Pet Friendly")
        if local['acessivel']:
            print("  [*] Acessível")
        print("-" * 30)
        
        if idx < total_paradas - 1:
            print(f"Próxima parada --> {roteiro[idx + 1]['nome']}\n")
            input("Digite 1 para realizar CHECK-IN e avançar... ")
        else:
            print("*** ÚLTIMA PARADA DO ROTEIRO! ***\n")
            input("Digite 1 para finalizar o seu dia turístico! ")

    # Encerramento
    limpar_tela()
    print("==================================================")
    print("   PARABÉNS! VOCÊ CONCLUIU SEU ROTEIRO!           ")
    print("==================================================")
    print("\n   Esperamos que tenha aproveitado Floripa!")
    print("   Volte sempre à Ilha da Magia!\n")
    print("==================================================")

# Início do Programa
if __name__ == "__main__":
    filtrar_roteiro()