# Multimodal LLM Comparison Report
This repository contains my report comparing two prominent multimodal Large Language Models (LLMs): CLIP (Contrastive Language-Image Pre-training) and BLIP (Bootstrapping Language-Image Pre-training). This assignment explores their architectures, the types of inputs they process, their primary applications, and how they handle the complex task of understanding information across different modalities.

# Project Overview
The objective of this project was to delve into the fascinating world of multimodal LLMs, which are designed to understand and process information from more than one modality (e.g., text and images). By comparing CLIP and BLIP, I aimed to:

# BLIP (Bootstrapping Language-Image Pre-training)
Architecture: BLIP is a more complex architecture that combines a Vision Transformer (ViT) for image encoding, a Text Encoder, and a Text Decoder. It integrates these components within a unified framework, often using a multimodal mixture of encoders and decoders.

Input Types: Primarily uses Image and Text inputs.

Cross-Modal Handling: BLIP employs a multitask learning objective during pre-training, which includes:

Image-Text Contrastive (ITC) Loss: Similar to CLIP, aligning image and text embeddings.

Image-Text Matching (ITM) Loss: Predicting whether an image and text pair are a positive match or not, at a finer-grained level than just contrastive learning.

Language Modeling (LM) Loss: Generating text captions for images.
It also uses a "bootstrapping" strategy to generate synthetic captions and noisy captions to improve learning from web data.

# CLIP (Contrastive Language-Image Pre-training)
Architecture: CLIP consists of two separate encoders: an Image Encoder (a ResNet or Vision Transformer) and a Text Encoder (a Transformer). These encoders are trained independently but simultaneously to learn representations that are aligned in a shared embedding space.

Input Types: Primarily uses Image and Text inputs.

Cross-Modal Handling: CLIP learns by contrastive pre-training. It takes a batch of (image, text) pairs and aims to maximize the cosine similarity between the correct image-text pairs' embeddings while minimizing the similarity for incorrect pairs. This forces the model to learn a joint embedding space where semantically related images and text are close together.

Main Applications:

Zero-shot image classification: Classifying images into categories without explicit training on those categories, by comparing image embeddings to text embeddings of category names.

Image search: Finding images based on text descriptions.

Image captioning (with additional components): Generating descriptions for images.

Multimodal retrieval.

