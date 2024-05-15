from pprint import pprint
from utils import *

# Ler json com mapeamento de nomes de suprimentos
filename = 'supplyNamesMap.json'
supply_mames_map = read_json(filename)

tags_mapped = {}

array = ["Roupa íntima ",
    "Roupa íntima ",
    "Roupa Íntima (adulto) Feminina E Masculina",
    "Roupa íntima feminina",
    "Roupa íntima feminina",
    "Roupa Íntima Feminina",
    "Roupa Íntima - G E Gg",
    "Roupa Íntima Infantil",
    "Roupa Íntima Infantil",
    "Roupa íntima masculina",
    "Roupa íntima masculina",
    "Roupa íntima masculina e feminina",
    "Roupas Infantil",
    "Roupas íntimas",
    "Roupas íntimas",
    "Roupas Íntimas De Criança E Adolescente",
    "Roupas Íntimas Femininas",
    "Roupas Íntimas Femininas",
    "Roupas Intimas Feminino",
    "Roupas Íntimas (masc E Fem)",
    "Roupas Íntimas (masc E Fem)",
    "Roupas Intimas Masculino",
    "Roupas íntimas plus size feminina",
    "Roupas íntimas plus size feminina",
    "Cueca",
    "Cueca",
    "Cueca G E Gg",
    "Cueca Infantil Tamanho 6+",
    "Cuecas",
    "Cuecas Adultos G",
    "Cuecas Tamanhos P M G",
    "Calcinha",
    "Calcinha G E Gg",
    "Calcinha Infantil",
    "Calcinhas",
    "Calcinhas Infantis G",
    "Sutiã",
    "Sutiãs",
]

for item in array:
    closest_key = find_closest_key(item, supply_mames_map, confidence_threshold=0.7)
    if tags_mapped.get(closest_key) is None:
        tags_mapped[closest_key] = []
    
    tags_mapped[closest_key].append(item)

    print(f"{item:<30} ->   {closest_key}")

pprint(tags_mapped)

filename_output = 'supplyNamesMap_OUTPUT_TEST.json'

save_json(tags_mapped, filename_output)

