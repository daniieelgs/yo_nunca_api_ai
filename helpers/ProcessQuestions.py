from helpers.Openai import Openai

PROMPT_TEMPLATE = """<|im_start|>system
Eres sistema que se encarga de generar preguntas para el juego de amigos del 'YO NUNCA NUNCA'. Este se juego se basa en hacer preguntas a un grupo de amigos para conocerse más entre si.
Deberás generar preguntas de los siguientes estilos: {categories}.
Aquí tienes algunos ejemplos también del estilo de  preguntas que debes generar: {examples}.
Genera {n} preguntas y devuelvelas separadas por el caracter '~'. Por ejemplo: '{example_response}'
"""

class ProcessQuestions:
    
    def __init__(self):
        self.openai = Openai()
    
    def get_questions(self, categories, examples, n = 5):
        prompt = PROMPT_TEMPLATE.replace('{categories}', ', '.join(categories)).replace('{examples}', ', '.join(examples)).replace('{n}', str(n)).replace('{example_response}', '~'.join(examples[:10]))
        
        response = self.openai.completion(prompt)
        
        return response.split("~")
        
        