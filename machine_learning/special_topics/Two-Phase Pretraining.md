# Two-phase Pretraining Strategy for LLMs

https://arxiv.org/pdf/2412.15285

`Fine-tuning the pretraining for better foundation model quality.`

The paper introduces a two-phase pretraining strategy for large language models (LLMs) that improves performance by strategically selecting, blending, and ordering data during training, rather than using the common approach of randomly ordering data or following its natural distribution.

## Why

LLMs are trained on huge corpora from diverse sources (web crawl, books, code, math, etc.), but little is known about how best to mix and schedule this data to maximize downstream accuracy. The authors tackle this gap by formalizing and empirically validating a two-phase approach.

## Two-phase Strategy

1. Phase 1 (Diversity Focus): Train on a broad mix of data with emphasis on diversity, especially high-quality web crawl plus some high-quality sources.
2. Phase 2 (Quality Focus): Shift to a blend that heavily emphasizes high-quality datasets such as math, code, Wikipedia, and other structured domains. The idea is to first establish a broad linguistic foundation, then refine the model on higher-quality, task-relevant data.

## Guidance

The authors also provide guidance on how to quantify data quality and choose appropriate ratios for blending and ordering, including using downsampled runs to inform larger-scale pretraining decisions.

## Conclusion

A structured, phased training regimen that first prioritizes data diversity and then shifts toward quality leads to stronger and more robust LLM performance than unstructured data training.
