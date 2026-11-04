
from ollama import chat
class Ai:

    def __init__(self, question, result_model, prompt, *model):
        self.models = model
        self.question = question
        self.result_model = result_model
        self.prompt = prompt

    def one(self):
        counter = 0
        answer = []
        for detail in self.models:
            response = chat(
                model=f'{detail}',
                messages=[
                    {'role': 'system', 'content': f'{self.prompt}'}, 
                    {'role': 'user', 'content': f'{self.question}'}],
            )
            answer.append(response.message.content)
            counter += 1
            print(counter)
        return answer
 

class Ai_Use(Ai):

    def resultator(self):
        texts = self.one()
        response = chat(
            model=f'{self.result_model}',
            messages=[
                {'role': 'system', 'content': f'Твоя роль: "Результатор" текста. Тебе даются текста от прошлых LLM, ты все подытоживаешь и отправляешь финальный результат. твоя задача полностью объединить его, сделать так, чтобы текст меньше дублировался, но имел абсолютно ту же суть, имея каждую частичку разных ответов от моделей. Ты не должен объяснять, что было в тексте например "В этом тексте, все модели хотели донести..." Ты получаешь информацию и эту информацию, должен объяснять не так, как пересказ, а так, будто ты сам сгенерировал и объясняешь всю суть.'}, 
                {'role': 'user', 'content': f' {texts}'}],
        )
        print("Итоги подведены")
        return response.message.content


def testing():

    # 1) prompt, 2) model that will generate the final answer 3) a sys. prompt 4) models

    a = Ai_Use('Привет', 'model', '', 'model', 'model', 'model', 'model')



    text = a.resultator()

    print(text)

testing()
