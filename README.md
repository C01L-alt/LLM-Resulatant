# LLM-with-classes
🇬🇧
## The idea is simple:

Several models answer the same question, and then one model merges everything into a single, clean answer.

## Why?

A single LLM can miss something, hallucinate, or repeat itself.
If you ask several models (or the same one multiple times) and then carefully stitch their answers together, the result is fuller and has less fluff.

## How does the script work?

The project has just two classes:
Ai - stores the models, the question, and the prompt. The one() method queries all of them and returns a list of answers.
Ai_Use - a subclass. The resultator() method takes the answers and runs them through the summarizer model.

1) Ask each model from the list.
2) Collect all answers into a variable.
3) Pass that variable to another model, which builds a single text out of all the received ones - containing all the information, taking every answer from the previous models into account.

## Libraries

`pip install ollama`

`ollama pull your-model`

Find models here → https://ollama.com/library

🇷🇺
## Идея простая: 
несколько моделей отвечают на один вопрос, а потом одна модель сводит всё в один нормальный ответ.

## Зачем? 
Одна LLM может что-то упустить, наврать или повториться. 
Если спросить несколько моделей (или одну и ту же несколько раз) и потом аккуратно склеить их ответы - результат получается полнее и без воды.

## Как работает скрипт?

В Проекте всего два класса:
Ai - хранит модели, вопрос и промпт. Метод one() опрашивает всех и возвращает список ответов.
Ai_Use - наследник. Метод resultator() берёт ответы и прогоняет их через модель-результатор.

1) Спрашиваем каждую модель из списка.
2) Все ответы собираются в переменную
3) Переменная отдается другой модели, которая формирует из всех полученных текстов один, где собрана вся информация, учитывая каждый ответ от предыдущих моделей

## библиотеки
`pip install ollama`

`ollama pull ваша-модель`

Модели можно найти тут -> https://ollama.com/library
