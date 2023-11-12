from transformers import GPT2LMHeadModel, GPT2Tokenizer

def modify_text(input_text):
    # Загрузка предварительно обученной модели GPT-2 и токенизатора
    model = GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")

    # Токенизация входного текста
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Генерация текста с некоторыми параметрами
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, temperature=0.2)

    # Декодирование сгенерированного текста
    modified_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return modified_text

if __name__ == "__main__":
    while True:
      input_text = input()

      modified_text = modify_text(input_text)

      print("Исходный текст: " + input_text)
      print("\nИзмененный текст:")
      print(modified_text)
