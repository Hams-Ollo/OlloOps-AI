#-------------------------------------------------------------------------------------#
# File: chroma_client.py
# Description: ChromaDB client implementation for vector storage and retrieval
# Author: @hams_ollo
#-------------------------------------------------------------------------------------#

import os
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

class ChromaVectorStore:
    def __init__(self, persist_directory: str = "./data/chromadb"):
        """Initialize ChromaDB client with persistence."""
        self.persist_directory = persist_directory
        self.client = chromadb.PersistentClient(path=persist_directory)
        
        # Use sentence-transformers for embeddings
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        
        # Create or get the default collection
        self.collection = self.client.get_or_create_collection(
            name="document_store",
            embedding_function=self.embedding_function,
            metadata={"description": "Main document storage for RAG system"}
        )

    def add_documents(self, texts: List[str], metadatas: List[Dict[str, Any]], ids: List[str]) -> None:
        """Add documents to the vector store.
        
        Args:
            texts: List of document texts
            metadatas: List of metadata dictionaries for each document
            ids: List of unique IDs for each document
        """
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

    def query_documents(self, query_text: str, n_results: int = 5) -> Dict[str, Any]:
        """Query the vector store for similar documents.
        
        Args:
            query_text: The query string
            n_results: Number of results to return
            
        Returns:
            Dictionary containing query results with documents and metadata
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

    def update_document(self, document_id: str, text: str, metadata: Dict[str, Any]) -> None:
        """Update an existing document in the vector store.
        
        Args:
            document_id: ID of document to update
            text: New document text
            metadata: New metadata dictionary
        """
        self.collection.update(
            ids=[document_id],
            documents=[text],
            metadatas=[metadata]
        )

    def delete_documents(self, ids: List[str]) -> None:
        """Delete documents from the vector store.
        
        Args:
            ids: List of document IDs to delete
        """
        self.collection.delete(ids=ids)

    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the current collection.
        
        Returns:
            Dictionary containing collection statistics
        """
        return {
            "count": self.collection.count(),
            "name": self.collection.name,
            "metadata": self.collection.metadata
        }
