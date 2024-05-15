import unicodedata
import difflib
import json

def save_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"\n\nDados salvos com sucesso em {filename}")
    except Exception as e:
        print(f"\n\nErro ao salvar os dados: {e}")

def read_json(arquivo_json):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError as e:
        print(f"Erro: O arquivo {arquivo_json} não foi encontrado.")
        raise
    except json.JSONDecodeError as e:
        print("Erro: O arquivo não está em formato JSON válido.")
        raise
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        raise


def normalize_text(text):
    # Normaliza o texto para remover acentos e converter para minúsculas
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()

def find_closest_key(search_word, dictionary, confidence_threshold=0.75):
    search_word = normalize_text(search_word)  # Normaliza a palavra de busca
    best_match_key = None
    best_match_ratio = 0  # Armazena a melhor correspondência de semelhança encontrada

    for key, values in dictionary.items():
        normalized_values = [normalize_text(value) for value in values]
        # Obtém as correspondências mais próximas na lista de valores normalizados e limita a uma correspondência
        matches = difflib.get_close_matches(search_word, normalized_values, n=1, cutoff=0.1)
        if matches:
            # Calcula a razão de semelhança para a melhor correspondência
            ratio = difflib.SequenceMatcher(None, search_word, matches[0]).ratio()
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                if best_match_ratio >= confidence_threshold:
                    best_match_key = key
                else:
                    best_match_key = None

    return best_match_key