#-------------------------------------------------------------------------------------#
# File: rag_manager.py
# Description: Main RAG system manager integrating document processing and vector storage
# Author: @hams_ollo
#-------------------------------------------------------------------------------------#

import os
from typing import List, Dict, Any, Optional
from pathlib import Path
import uuid
import json
from datetime import datetime

from .document_processor.loader import DocumentLoader
from .document_processor.chunker import TextChunker
from .vectorstore.chroma_client import ChromaVectorStore

class RAGManager:
    """Manages the RAG (Retrieval Augmented Generation) system."""

    def __init__(self, 
                 persist_directory: str = "./data/chromadb",
                 chunk_size: int = 512,
                 chunk_overlap: int = 50):
        """Initialize the RAG manager.
        
        Args:
            persist_directory: Directory for ChromaDB persistence
            chunk_size: Maximum size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.vector_store = ChromaVectorStore(persist_directory=persist_directory)
        self.chunker = TextChunker(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        self.document_loader = DocumentLoader()

    def process_document(self, file_path: str) -> Dict[str, Any]:
        """Process a single document and add it to the vector store.
        
        Args:
            file_path: Path to the document
            
        Returns:
            Dictionary with processing results and metadata
        """
        # Load and process document
        doc = self.document_loader.load_document(file_path)
        
        # Generate chunks
        chunks = self.chunker.chunk_text(doc["content"], doc["metadata"])
        
        # Prepare data for vector store
        texts = [chunk.text for chunk in chunks]
        metadatas = [chunk.metadata for chunk in chunks]
        ids = [str(uuid.uuid4()) for _ in chunks]
        
        # Add to vector store
        self.vector_store.add_documents(
            texts=texts,
            metadatas=metadatas,
            ids=ids
        )
        
        return {
            "document": doc,
            "num_chunks": len(chunks),
            "chunk_ids": ids
        }

    def process_directory(self, 
                         directory_path: str, 
                         recursive: bool = True) -> List[Dict[str, Any]]:
        """Process all documents in a directory.
        
        Args:
            directory_path: Path to the directory
            recursive: Whether to process subdirectories
            
        Returns:
            List of processing results for each document
        """
        results = []
        documents = self.document_loader.process_directory(
            directory_path=directory_path,
            recursive=recursive
        )
        
        for doc in documents:
            try:
                result = self.process_document(doc)
                results.append(result)
            except Exception as e:
                print(f"Error processing document {doc['metadata']['filename']}: {str(e)}")
                continue
                
        return results

    def query(self, 
              query_text: str, 
              n_results: int = 5,
              min_relevance_score: float = 0.5) -> Dict[str, Any]:
        """Query the RAG system for relevant documents.
        
        Args:
            query_text: The query string
            n_results: Number of results to return
            min_relevance_score: Minimum relevance score (0-1) for results
            
        Returns:
            Dictionary containing query results and metadata
        """
        # Query vector store
        results = self.vector_store.query_documents(
            query_text=query_text,
            n_results=n_results
        )
        
        # Process and format results
        formatted_results = []
        for i, (doc, metadata, score) in enumerate(zip(
            results["documents"][0],
            results["metadatas"][0],
            results.get("distances", [1.0] * len(results["documents"][0]))
        )):
            if score < min_relevance_score:
                continue
                
            formatted_results.append({
                "content": doc,
                "metadata": metadata,
                "relevance_score": score,
                "rank": i + 1
            })
        
        return {
            "query": query_text,
            "results": formatted_results,
            "total_results": len(formatted_results),
            "timestamp": datetime.now().isoformat()
        }

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about the RAG system.
        
        Returns:
            Dictionary containing system statistics
        """
        collection_stats = self.vector_store.get_collection_stats()
        
        return {
            "total_documents": collection_stats["count"],
            "collection_name": collection_stats["name"],
            "collection_metadata": collection_stats["metadata"],
            "supported_file_types": list(DocumentLoader.SUPPORTED_EXTENSIONS),
            "chunk_size": self.chunker.chunk_size,
            "chunk_overlap": self.chunker.chunk_overlap
        }
