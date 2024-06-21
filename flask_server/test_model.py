import json

from transformers import BertTokenizerFast, BertForSequenceClassification, pipeline

# Load the saved model
model = BertForSequenceClassification.from_pretrained('./model')

# Load the tokenizer
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

# Create a pipeline
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Use the model for inference
text = "I need to get the title of the page"
result = nlp(text)

# Load the config file
with open('./model/config.json', 'r') as f:
    config = json.load(f)

# Get the id2label dictionary
label2id = config['label2id']

# Get the predicted label ID
predicted_label_id = result[0]['label']

# Translate the label ID to the text label
predicted_label_text = label2id[predicted_label_id]

print(predicted_label_text)