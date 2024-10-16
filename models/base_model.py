from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def generate_response(self, input_text, resume_content, prompt):
        pass