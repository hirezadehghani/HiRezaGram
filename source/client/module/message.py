from source.utils import generate_uuid

class Message:
    def __init__(self, sender_id: str, recipient_id: str, message_text: str, timestamp: str, status: bool):
        self.message_id = generate_uuid()
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.message_text = message_text
        self.timestamp = timestamp
        self.status = status #delivered or read
        
    