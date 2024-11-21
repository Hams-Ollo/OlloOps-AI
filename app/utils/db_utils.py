import sqlite3
from typing import List, Dict, Any, Optional
import json
import logging

class DatabaseUtils:
    def __init__(self, db_path: str):
        """Initialize database connection"""
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize database tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create conversations table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS conversations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        user_message TEXT,
                        ai_response TEXT,
                        metadata TEXT
                    )
                ''')

                # Create podcast_episodes table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS podcast_episodes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        description TEXT,
                        outline TEXT,
                        show_notes TEXT,
                        recording_date DATETIME,
                        status TEXT
                    )
                ''')

                # Create content_items table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS content_items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        content_type TEXT,
                        platform TEXT,
                        content TEXT,
                        metadata TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

                conn.commit()
        except Exception as e:
            logging.error(f"Error initializing database: {str(e)}")
            raise

    def save_conversation(self, user_message: str, ai_response: str, metadata: Optional[Dict] = None) -> int:
        """Save a conversation interaction"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO conversations (user_message, ai_response, metadata) VALUES (?, ?, ?)',
                    (user_message, ai_response, json.dumps(metadata) if metadata else None)
                )
                return cursor.lastrowid
        except Exception as e:
            logging.error(f"Error saving conversation: {str(e)}")
            return -1

    def save_podcast_episode(self, title: str, description: str, outline: str, 
                           show_notes: str, recording_date: str, status: str) -> int:
        """Save podcast episode details"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''INSERT INTO podcast_episodes 
                       (title, description, outline, show_notes, recording_date, status)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (title, description, outline, show_notes, recording_date, status)
                )
                return cursor.lastrowid
        except Exception as e:
            logging.error(f"Error saving podcast episode: {str(e)}")
            return -1

    def save_content_item(self, content_type: str, platform: str, 
                         content: str, metadata: Optional[Dict] = None) -> int:
        """Save a content item"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'INSERT INTO content_items (content_type, platform, content, metadata) VALUES (?, ?, ?, ?)',
                    (content_type, platform, content, json.dumps(metadata) if metadata else None)
                )
                return cursor.lastrowid
        except Exception as e:
            logging.error(f"Error saving content item: {str(e)}")
            return -1

    def get_conversation_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Retrieve recent conversation history"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM conversations ORDER BY timestamp DESC LIMIT ?',
                    (limit,)
                )
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logging.error(f"Error retrieving conversation history: {str(e)}")
            return []

    def get_podcast_episodes(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve podcast episodes"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                if status:
                    cursor.execute('SELECT * FROM podcast_episodes WHERE status = ?', (status,))
                else:
                    cursor.execute('SELECT * FROM podcast_episodes')
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            logging.error(f"Error retrieving podcast episodes: {str(e)}")
            return []
