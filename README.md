# Sumarização de Texto Automática em Português
Este projeto oferece uma ferramenta de sumarização automática de texto focada na abordagem extrativa, desenvolvida em Python 3. Seu objetivo principal é simplificar a compreensão de documentos longos, extraindo as sentenças mais relevantes para formar um resumo conciso.

## 🚀 Funcionalidades
- Sumarização Extrativa: Identifica e seleciona as frases mais importantes do texto original.
- Suporte a Português: Otimizado para processar textos no idioma português.
- Entrada e Saída Simples: Recebe um arquivo .txt e gera um summary.txt com o resumo.

## 💡 Por Que Usar?

Em um mundo com excesso de informação, a capacidade de digerir grandes volumes de texto rapidamente é crucial. Este projeto é ideal para:

- Pesquisadores: Obtenha uma visão geral rápida de artigos e relatórios.

- Estudantes: Crie resumos de materiais de estudo extensos.

- Profissionais: Extraia os pontos-chave de documentos e e-mails longos.

- Qualquer pessoa: Economize tempo e foque no que realmente importa em qualquer texto em português.

## 🛠️ Tecnologias Utilizadas
- Python 3: A linguagem de programação principal.
- Spacy: Para processamento de linguagem natural (tokenização, lematização, etc.).
- Scikit-learn: Para algoritmos de aprendizado de máquina, possivelmente para análise de similaridade ou agrupamento de sentenças.

## ⚙️ Instalação

Para configurar e executar este projeto em sua máquina local, siga os passos abaixo:

- Clone o repositório:
```
git clone https://github.com/bivar/text-summarization.git
cd text-summarization
```
- Crie e ative um ambiente virtual (recomendado):
```
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# ou
.\venv\Scripts\activate  # No Windows
```
- Instale as dependências:
```
pip install -r requirements.txt
```

- Baixe o modelo de idioma português do Spacy:
```
python -m spacy download pt_core_news_sm
```

## 🚀 Como Usar
-Prepare seu texto: Coloque o texto que deseja resumir em um arquivo .txt (por exemplo, meu_documento.txt).
-Execute o script de sumarização:
```
python summarize.py meu_documento.txt
```

- Verifique o resumo: Um novo arquivo chamado summary.txt será criado no mesmo diretório, contendo o texto sumarizado.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você tiver ideias para melhorias, novas funcionalidades ou encontrar algum bug, sinta-se à vontade para:

-Fazer um "fork" do repositório.
-Criar uma nova "branch" (git checkout -b feature/sua-feature).
-Fazer suas alterações e "commitá-las" (git commit -m 'Adiciona nova funcionalidade X').
-Fazer um "push" para a "branch" (git push origin feature/sua-feature).
-Abrir um "Pull Request".

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.

Autor: Rebeca Bivar
