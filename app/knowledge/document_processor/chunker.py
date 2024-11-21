#-------------------------------------------------------------------------------------#
# File: chunker.py
# Description: Text chunking strategies for optimal document processing
# Author: @hams_ollo
#-------------------------------------------------------------------------------------#

from typing import List, Dict, Any
import re
from dataclasses import dataclass

@dataclass
class Chunk:
    """Represents a chunk of text with metadata."""
    text: str
    metadata: Dict[str, Any]
    start_idx: int
    end_idx: int

class TextChunker:
    """Handles text chunking with various strategies."""

    def __init__(self, 
                 chunk_size: int = 512, 
                 chunk_overlap: int = 50,
                 separator: str = "\n"):
        """Initialize the chunker with specific parameters.
        
        Args:
            chunk_size: Maximum size of each chunk
            chunk_overlap: Number of characters to overlap between chunks
            separator: Character(s) to use as chunk separator
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator

    def chunk_text(self, text: str, metadata: Dict[str, Any]) -> List[Chunk]:
        """Split text into chunks with overlap.
        
        Args:
            text: Text to chunk
            metadata: Metadata to attach to each chunk
            
        Returns:
            List of Chunk objects
        """
        if not text:
            return []

        chunks = []
        start = 0
        
        while start < len(text):
            # Find the end of the current chunk
            end = start + self.chunk_size
            
            if end >= len(text):
                # Last chunk
                chunk_text = text[start:]
                chunks.append(Chunk(
                    text=chunk_text,
                    metadata=metadata.copy(),
                    start_idx=start,
                    end_idx=len(text)
                ))
                break
            
            # Find a good breaking point
            break_point = self._find_break_point(text[start:end])
            if break_point:
                end = start + break_point
            
            chunk_text = text[start:end]
            chunks.append(Chunk(
                text=chunk_text,
                metadata=metadata.copy(),
                start_idx=start,
                end_idx=end
            ))
            
            # Move start position for next chunk, accounting for overlap
            start = end - self.chunk_overlap

        return chunks

    def _find_break_point(self, text: str) -> int:
        """Find a suitable break point in the text.
        
        Args:
            text: Text to find break point in
            
        Returns:
            Index of the break point
        """
        # Try to break at paragraph
        if match := re.search(r"\n\s*\n[^\n]*$", text):
            return match.start()
        
        # Try to break at sentence
        if match := re.search(r"[.!?]\s+[A-Z][^\n]*$", text):
            return match.start() + 1
        
        # Try to break at comma or semicolon
        if match := re.search(r"[,;]\s+[^,;]*$", text):
            return match.start() + 1
        
        # Break at last space if all else fails
        if match := re.search(r"\s+[^\s]*$", text):
            return match.start()
        
        # If no good break point found, use the full chunk size
        return len(text)

    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Chunk]:
        """Process multiple documents into chunks.
        
        Args:
            documents: List of document dictionaries with content and metadata
            
        Returns:
            List of Chunk objects
        """
        all_chunks = []
        
        for doc in documents:
            content = doc["content"]
            metadata = doc["metadata"]
            
            # Add document index to metadata
            metadata["doc_index"] = len(all_chunks)
            
            chunks = self.chunk_text(content, metadata)
            all_chunks.extend(chunks)
        
        return all_chunks
