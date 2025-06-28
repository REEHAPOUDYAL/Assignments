Transformer Architecture: My PyTorch Implementation
This repository showcases my hands-on implementation of the Transformer neural network, as detailed in "Attention Is All You Need" (Vaswani et al., 2017). I built this project in PyTorch to deeply understand its core components and its application in sequence-to-sequence tasks.

Project Overview
I developed a modular Transformer model, a revolutionary architecture that processes entire input sequences simultaneously, unlike traditional sequential models (RNNs/CNNs). This enables parallel processing, significantly speeding up training. The core idea is self-attention, which allows the model to weigh the importance of different parts of the input sequence when processing each element. This project was a key step in my learning journey to grasp this foundational architecture in modern NLP.

Features I Implemented
Core Transformer Components: I built the fundamental Encoder and Decoder stacks. The Encoder processes the input sequence, and the Decoder generates the output sequence, attending to both the encoder's output and its own previous outputs.

Attention Mechanisms:

Scaled Dot-Product Attention: This is the basic building block, calculating how much focus each word in a sequence should place on other words.

Multi-Head Attention: I implemented this to allow the model to jointly attend to information from different representation subspaces at different positions. It's like having multiple "attention lenses" to capture diverse relationships.

Positional Encoding: Since attention itself doesn't inherently understand word order, I added Positional Encoding to inject information about the relative or absolute position of tokens in the sequence.

Feed-Forward Networks: Position-wise fully connected feed-forward networks were integrated into both the Encoder and Decoder, applied independently to each position.

Training Utilities: I incorporated crucial elements like residual connections (to help with training deep networks by allowing gradients to flow more easily) and layer normalization (to stabilize activations). A main.py script was developed for data loading, model training, and evaluation.
