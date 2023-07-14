import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class TransactionCategorizer:
    def __init__(self):
        self.transactions = []

    def load_transactions_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.transactions = data['transactions']

    def categorize_transaction(self, transaction):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant with a lot of domain in Brazilian Open Finance."},
                {"role": "user", "content": f"I have a transaction with the following details: Description: {transaction['description']}, Type: {transaction['type']}, Amount: {transaction['amount']}, Currency: {transaction['currency']}, Institution: {transaction['institution']}, Merchant: {transaction['merchant']['merchant_name']}. Can you help me categorize this transaction into category and subcategory? Put the category and subcategory inside '<>' to be easy to fetch"},
            ]
        )
        category = response['choices'][0]['message']['content']
        return category

    def categorize_transactions(self):
        results = []
        for transaction in self.transactions:
            categories = self.categorize_transaction(transaction)
            result = {
                "Transaction ID": transaction['transaction_id'],
                "Category": self._extract_category(categories),
                "Subcategory": self._extract_subcategory(categories),
                "Transaction Data": transaction,
                "ChatGPT Response": categories
            }
            results.append(result)
        return results

    def _extract_category(self, categories):
        return categories.split('<')[1].split('>')[0]

    def _extract_subcategory(self, categories):
        return categories.split('<')[2].split('>')[0]


if __name__ == '__main__':
    categorizer = TransactionCategorizer()
    categorizer.load_transactions_from_file('transactions.json')
    categorized_transactions = categorizer.categorize_transactions()
    print(categorized_transactions)
