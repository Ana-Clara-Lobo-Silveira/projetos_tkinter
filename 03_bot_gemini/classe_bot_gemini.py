import google.generativeai as genai

class Boot_gemini:
    """Criando um robo especialista em arte."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyBKOgKFvkIxswiyKeOjwXbHGqEl_l6mUPs")
        instrucao_sistema = """
            Você é um artista especialista em arte e arquitetuira gótica, com 20 anos de experiência.
            Seu nome é Ms. Gothart. Você deve responder a todas as perguntas de forma 
            profissional, detalhada e focada exclusivamente no mundo da arte. 
            Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa 
            de volta para arte, afirmando que seu conhecimento é especializado.
            """
        self.model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def responder(self,pergunta:str) -> str:
        """Função que apresenta a resposta."""

        resposta = self.chat.send_message(pergunta)
        return resposta.text