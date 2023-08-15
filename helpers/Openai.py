from globals import API_KEY_OPENAI, ENGINE_MODEL_OPENAI
import openai

class Openai:
    
        
    ENGINE_MODEL = str()
    
    def __init__(self, api_key = API_KEY_OPENAI, engine_model = ENGINE_MODEL_OPENAI):
        
        global ENGINE_MODEL 
        ENGINE_MODEL = engine_model
        
        openai.api_key = api_key
    
    
    def completion(self, prompt, engine = None, max_tokens = 1024, temperature = 1, n = 1, stop = None):
          
        global ENGINE_MODEL
          
        if not engine: engine = ENGINE_MODEL
          
        response = openai.Completion.create(
                    engine=engine,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    n = n,
                    stop = stop
                )
            
        return response['choices'][0]['text'].strip("\n")