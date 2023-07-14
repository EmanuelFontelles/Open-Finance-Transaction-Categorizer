# Open Finance Transaction Categorizer

Este projeto usa a API ChatGPT da OpenAI para categorizar transações financeiras.

## Instalação

Este projeto requer Python 3.8 ou superior. Recomendamos que você crie um ambiente virtual para instalar as dependências. Aqui estão as instruções para criar um ambiente virtual e instalar as dependências:

```bash
python -m venv env
source env/bin/activate  # No Windows, use `env\Scripts\activate`
pip install -r requirements.txt
```

## Uso
Para usar este projeto, primeiro você precisa obter uma chave de API da OpenAI. Depois de obter a chave, você pode configurá-la como uma variável de ambiente:

```bash
export OPENAI_API_KEY=your-api-key
```
Depois de configurar a chave de API, você pode executar o script principal:

```bash
python src/main.py
```

## Contribuição
Contribuições para este projeto são bem-vindas. Por favor, abra um problema para discutir a mudança que você gostaria de fazer antes de fazer uma solicitação de pull.

## Licença
Este projeto é licenciado sob a licença MIT.