from model_factory import get_model

class Defender:
    def __init__(self):
        self.model = get_model()

    def get_response(self, query):
        chat = self.model.start_chat()
        return chat.send_message(query).text
