# Sentiment Analysis Fine-tuning Comparison
This project explores and compares different fine-tuning strategies for pre-trained transformer models on a sentiment analysis task using the IMDb movie review dataset. The goal is to understand the trade-offs between model accuracy, training time, memory usage, and parameter efficiency across various fine-tuning approaches.

# Introduction
Sentiment analysis is a fundamental task in Natural Language Processing (NLP) that involves classifying the emotional tone behind a piece of text. Pre-trained transformer models, such as BERT, RoBERTa, and DistilBERT, have achieved state-of-the-art results in various NLP tasks, including sentiment analysis. However, effectively adapting these large models to specific downstream tasks often requires fine-tuning.

This project investigates four distinct fine-tuning methodologies:

Full Fine-tuning: The standard approach where all parameters of the pre-trained model are updated.

Frozen Feature Extraction: Only the newly added classification head is trained, while the pre-trained transformer backbone remains frozen.

Low-Rank Adaptation (LoRA): A parameter-efficient fine-tuning technique that injects small, trainable matrices into the pre-trained model's layers.

Gradual Unfreezing: A progressive fine-tuning strategy where layers of the pre-trained model are unfrozen in stages during training.

# Methodologies Explored
Each fine-tuning method is implemented as a separate nn.Module class in PyTorch:

FullFineTuningClassifier:

Updates all parameters of the distilbert-base-uncased model.

Represents the baseline for performance but is typically resource-intensive.

FrozenBackboneClassifier:

Freezes the entire distilbert-base-uncased transformer.

Trains only a small, custom classification head.

Highly parameter-efficient and fast, but may sacrifice accuracy.

LoRAClassifier:

Implements LoRA by adding low-rank matrices to the query and value projections within the attention layers of distilbert-base-uncased.

Only the LoRA parameters and the classification head are trainable.

Offers a balance between efficiency and performance.

GradualUnfreezingClassifier:

Starts by freezing all transformer layers and gradually unfreezes the top layers during training.

Aims to leverage pre-trained knowledge while allowing some task-specific adaptation.

# Dataset
The project utilizes the IMDb movie review dataset, which is commonly used for binary sentiment classification (positive/negative).

Source: Loaded using the datasets library.

Preprocessing: Tokenization is performed using AutoTokenizer from the transformers library, with a max_length of 256 and padding/truncation applied.

Splitting: A subset of the dataset is used for faster experimentation:

Training: 4000 samples

Validation: 1000 samples (20% of initial training data)

Test: 1000 samples
