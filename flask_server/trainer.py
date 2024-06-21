import json
import os
import torch
from logger import Logger
from sklearn.model_selection import train_test_split
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments

# Create a logger instance
logger = Logger(log_file='training.log', level='INFO')

# Define file paths
label_mappings_path: str = 'label_mappings.json'
selenium_actions_path: str = 'selenium_actions.json'

# Load data
if not os.path.isfile(selenium_actions_path):
    logger.critical('Path to selenium_actions.json not found. Exiting...')
with open(selenium_actions_path, 'r') as f:
    data = json.load(f)

# Prepare data
texts = []
labels = []
for action, info in data.items():
    for description in info['descriptions']:
        texts.append(description)
        labels.append(action)

# Split data into training and validation sets
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2)

# Initialize a tokenizer
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

# Tokenize the texts
train_encodings = tokenizer(train_texts, truncation=True, padding=True)
val_encodings = tokenizer(val_texts, truncation=True, padding=True)

# Convert labels to IDs
label_to_id = {v: i for i, v in enumerate(sorted(set(labels)))}
train_labels = [label_to_id[label] for label in train_labels]
val_labels = [label_to_id[label] for label in val_labels]

# map ids to original actions
id_to_label = {i: v for v, i in label_to_id.items()}

# Save the mappings to a JSON file
if not os.path.isfile(label_mappings_path):
    logger.info('Path to label_mappings.json not found. Creating a new file.')

with open('label_mappings.json', 'w') as f:
    json.dump({'label_to_id': label_to_id, 'id_to_label': id_to_label}, f)

# Define a PyTorch dataset
class SeleniumDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Create datasets for training and validation
train_dataset = SeleniumDataset(train_encodings, train_labels)
val_dataset = SeleniumDataset(val_encodings, val_labels)

# Load pre-trained model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(label_to_id))

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    eval_strategy='steps',  # or 'epoch' if you want to evaluate at the end of each epoch
    logging_dir='./logs',
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# Train model
trainer.train()

# Save model
model.save_pretrained('./model')