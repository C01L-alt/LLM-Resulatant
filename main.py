
from ollama import chat

# Класс с LLM

class Ai:

    def __init__(self, model1, model2, model3, model4, question, result_model=None, prompt=None):
        self.model1 = model1
        self.model2 = model2
        self.model3 = model3
        self.model4 = model4
        self.question = question
        self.result_model = result_model
        self.prompt = prompt

    def one(self):
        response = chat(
            model=f'{self.model1}',
            messages=[
                {'role': 'system', 'content': f'{self.prompt}'}, 
                {'role': 'user', 'content': f'{self.question}'}],
        )
        print("первая модель закончила.")
        return response.message.content

    def two(self):
        response = chat(
            model=f'{self.model2}',
            messages=[
                {'role': 'system', 'content': f'{self.prompt}'}, 
                {'role': 'user', 'content': f'{self.question}'}],
        )
        print("вторая модель закончила.")
        return response.message.content
    
    def three(self):
        response = chat(
            model=f'{self.model3}',
            messages=[
                {'role': 'system', 'content': f'{self.prompt}'}, 
                {'role': 'user', 'content': f'{self.question}'}],
        )
        print("третья модель закончила.")
        return response.message.content

    def four(self):
        response = chat(
            model=f'{self.model4}',
            messages=[
                {'role': 'system', 'content': f'{self.prompt}'}, 
                {'role': 'user', 'content': f'{self.question}'}],
        )
        print("четвертая модель закончила.")
        return response.message.content

# Класс работы с результатами ответов LLMs

class Ai_Use(Ai):

    def summator(self):
        result = self.one() + self.two() + self.three() + self.four()
        print("Суммированно")
        return result

    def resultator(self):
        result = self.summator()
        response = chat(
            model=f'{self.result_model}',
            messages=[
                {'role': 'system', 'content': f'Твоя роль: "Результатор" текста. Тебе дается 4 текста от прошлых LLM, ты все подытоживаешь и отправляешь финальный результат. твоя задача полностью объединить его, сделать так, чтобы текст меньше дублировался, но имел абсолютно ту же суть, имея каждую частичку разных ответов от моделей. Ты не должен объяснять, что было в тексте например "В этом тексте, все модели хотели донести..." Ты получаешь информацию и эту информацию, должен объяснять не так, как пересказ, а так, будто ты сам сгенерировал и объясняешь всю суть.'}, 
                {'role': 'user', 'content': f' {result}'}],
        )
        print("Итоги подведены")
        return response.message.content


def testing():
    # Аргументация: 1) Модель 2) Модель 3) Модель 4) Модель 5) Промпт 6) Модель, генерирующая общий ответ 7) Системный промпт
    a = Ai_Use('gemma3:4b','gemma3:4b','gemma3:4b','gemma3:4b', 'Здравствуй', 'gemma3:4b', '')

    print(a.resultator())
    print(a.summator)
