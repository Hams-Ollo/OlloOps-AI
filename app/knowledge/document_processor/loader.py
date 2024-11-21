#-------------------------------------------------------------------------------------#
# File: loader.py
# Description: Document loading and processing utilities for various file formats
# Author: @hams_ollo
#-------------------------------------------------------------------------------------#

import os
from typing import List, Dict, Any, Optional
from pathlib import Path
import docx
import PyPDF2
import markdown
import docx2txt
from unstructured.partition.auto import partition

class DocumentLoader:
    """Handles loading and initial processing of various document types."""
    
    SUPPORTED_EXTENSIONS = {'.txt', '.pdf', '.docx', '.md'}

    @staticmethod
    def load_document(file_path: str) -> Dict[str, Any]:
        """Load a document and extract its content based on file type.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Dictionary containing document content and metadata
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = path.suffix.lower()
        if extension not in DocumentLoader.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {extension}")

        content = ""
        metadata = {
            "filename": path.name,
            "file_type": extension,
            "file_size": os.path.getsize(file_path),
            "created_at": os.path.getctime(file_path),
            "modified_at": os.path.getmtime(file_path)
        }

        try:
            if extension == '.txt':
                content = DocumentLoader._load_text(file_path)
            elif extension == '.pdf':
                content = DocumentLoader._load_pdf(file_path)
            elif extension == '.docx':
                content = DocumentLoader._load_docx(file_path)
            elif extension == '.md':
                content = DocumentLoader._load_markdown(file_path)
        except Exception as e:
            raise Exception(f"Error loading {file_path}: {str(e)}")

        return {
            "content": content,
            "metadata": metadata
        }

    @staticmethod
    def _load_text(file_path: str) -> str:
        """Load content from a text file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def _load_pdf(file_path: str) -> str:
        """Load content from a PDF file."""
        content = []
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                content.append(page.extract_text())
        return "\n".join(content)

    @staticmethod
    def _load_docx(file_path: str) -> str:
        """Load content from a Word document."""
        return docx2txt.process(file_path)

    @staticmethod
    def _load_markdown(file_path: str) -> str:
        """Load content from a Markdown file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Convert markdown to plain text while preserving structure
            html = markdown.markdown(content)
            # TODO: Convert HTML to plain text while preserving structure
            return content

    @staticmethod
    def process_directory(directory_path: str, recursive: bool = True) -> List[Dict[str, Any]]:
        """Process all supported documents in a directory.
        
        Args:
            directory_path: Path to the directory
            recursive: Whether to process subdirectories
            
        Returns:
            List of dictionaries containing document contents and metadata
        """
        documents = []
        path = Path(directory_path)
        
        if not path.exists() or not path.is_dir():
            raise NotADirectoryError(f"Invalid directory path: {directory_path}")

        pattern = '**/*' if recursive else '*'
        for file_path in path.glob(pattern):
            if file_path.suffix.lower() in DocumentLoader.SUPPORTED_EXTENSIONS:
                try:
                    doc = DocumentLoader.load_document(str(file_path))
                    documents.append(doc)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
                    continue

        return documents
