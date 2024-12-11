# RAG Agent for E-Commerce Product Advisor

## Overview
This Retrieval-Augmented Generation (RAG) agent is designed to enhance customer support for e-commerce platforms. It retrieves product information, FAQs, and reviews from a dataset to provide accurate, context-aware responses to user queries.

## Features
- **Product Search**: Retrieve product descriptions, prices, and reviews based on user queries.
- **FAQ Retrieval**: Provide answers to frequently asked questions about products.
- **Seamless Integration**: Built to integrate with other agents like chatbots and sentiment analysis tools.

## Dataset
The agent uses a refined dataset of JC Penney e-commerce products, including:
- Product titles and descriptions.
- Sale prices.
- Average customer ratings.
- Customer reviews.
- Product categories.

## Requirements
- Python 3.10+
- Libraries: `pandas`, `transformers` (if used for NLP)

## Installation
1. Clone the repository:
   git clone git@github.com:TanyaBuildsAI/rag-agent.git
   cd rag-agent
2. Install dependencies:
Copy code
pip install -r requirements.txt

## Usage  
- Load the dataset: python rag_agent.py
- Input a query to retrieve relevant information.

## Next Steps  
- Implement query preprocessing and NLP for enhanced retrieval accuracy.
- Integrate with a chatbot interface for real-time user interaction.
- Expand the dataset to include additional product categories and FAQs.

## License
MIT License
