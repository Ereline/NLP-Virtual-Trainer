from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import pipeline
MODEL_NAME = pipeline(
    model = 'cointegrated/rut5-base-paraphraser')

#MODEL_NAME = 'cointegrated/rut5-base-paraphraser'
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model.cuda();
model.eval();

def paraphrase(text, beams=5, grams=4):
    x = tokenizer(text, return_tensors='pt', padding=True).to(model.device)
    max_size = int(x.input_ids.shape[1] * 1.5 + 10)
    out = model.generate(**x, encoder_no_repeat_ngram_size=grams, num_beams=beams, max_length=max_size)
    return tokenizer.decode(out[0], skip_special_tokens=True)

text = open(lore.docx)
text = text.readlines()
post_text = paraphrase(text)
with open('lore.txt', 'w', encoding='utf-8') as file:
    for str_text in post_text:
        file.write(str_text + '\n')
