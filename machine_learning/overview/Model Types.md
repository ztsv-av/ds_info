# Model types

Predicting a spectrogram from text is a sequence-to-sequence problem because the input and output are different lengths. The length of the output is itself ambiguous, and something the model needs to predict.

Most successful approaches to this problem use an encoder-decoder system. The typical pattern looks like:

1. The model has a character embedding for each character in its vocabulary. This is usually learned from scratch during training, but can also be pre-trained or augmented with generic language embeddings like BERT.
2. The encoder analyzes the input sentence and applies various transformations to each character embedding in the output sequence. The encoder outputs are character embeddings that represent how each character should be pronounced, given the sentence. Encoders will also usually encode the approximate length, or duration, of each character.
3. The decoder predicts the spectrogram using the sequence of character pronunciation embeddings provided by the encoder.

Most model architectures rely on RNNs or Transformers to do sentence-level processing (like how to pronounce or emphasize certain words based on the meaning of the sentence), and CNNs to process features based on their adjacent characters or audio frames (like how to start and end a word to make it flow naturally with the previous and next words).

Today there are two main categories of these encoder-decoder systems: auto-regressive models and parallel models. Within these categories, parallel models typically use duration prediction, while auto-regressive models can use duration prediction or attention.

## Auto Regressive Models

### Tacotron 2

The first good neural TTS models were auto-regressive models such as Tacotron 2.

For these models, the encoder encodes the input sentence, and then the decoder predicts the spectrogram one audio frame at a time. This lets the model condition each spectrogram frame on the frames before it, producing high quality audio.

Let's take a quick look at the Tacotron 2 architecture.

![image](https://user-images.githubusercontent.com/73081144/226222588-df560af5-acfe-488d-bed7-6e97eac700f8.png)

The model is fairly complex. At a high level, it contains:

1. A CNN-RNN encoder which uses a bidirectional LSTM to analyze the entire sentence forward and backwards to figure out the pronunciation of every character.
1. A unidirectional LSTM decoder which predicts the spectrogram one frame at a time.
1. An attention mechanism that the decoder uses to determine which character(s) to look at when generating specific audio frames.
1. A stop token layer which predicts a single number [0, 1] to determine the probability that the decoder has reached the end of the sentence.
1. A pre-net that feeds the previous predicted frame into the decoder before predicting the next frame. This is used primarily for **teacher forcing** so that the model can learn effectively.
1. A post-net which post-processes the entire spectrogram produced by the decoder to fix inconsistencies and smooth it out.

The attention and teacher forcing mechanisms are the main characteristics that define the auto-regressive model and differentiate it from non-auto-regressive systems. These will be discussed in more detail below.

The post-net is an optional optimization.

The specifics of the encoder and decoder are not too important, and can be replaced with any equivalent combination of RNN, CNN, and/or Transformer blocks.

### Attention and Alignment

An auto-regressive model predicts the spectrogram based primarily on the encoder output features. For the output to make sense, each audio frame produced needs to be based on a subset of the characters in the input. Which character(s) the decoder is using when it predicts an audio frame is called its attention.

In order to get good quality output, we need our model's attention to follow these constraints:

- The decoder should pay attention to one character at a time (sometimes it also places weight on the one character immediately before and/or after it).
- The attention should be **monotonically increasing**, meaning it never go backwards in the text sequence. So the attention should only ever stay on the current character, or move forward to the next character.
- The model should start on the first character in the sequence and end on the last character.
These constraints result in the decoder effectively "reading" the text character by character or word by word, similar to how humans read aloud.

A model may need to be trained for a while before its attention learns to follow these constraints. Before that, the attention may look non-sensical, and the model output will sound unintelligible.

Once the models learns the above constraints and starts producing well-behaved attention maps, it is said that the model has **aligned**.

#### Attention Mechanisms

A large number of different systems have been developed over time to model TTS attention. Historically a lot of these mechanisms would use various inputs (decoder state, previous prediction, previous attention weights, etc) during each decoder step to predict a softmax across all characters in the sentence.

This works decently, but is not very good at enforcing the constraints listed above. A better alternative is to model the attention similar to a Hidden Markov Model; a state machine in which each character in the text is a state and the only valid state transitions are to stay on the current character or move forward 1 character.

### Training Features and Teacher Forcing

Another very important aspect of TTS modeling is teacher forcing, which means that during **training** we provide various **pieces of ground truth information** to the model and at **inference** provide **equivalent predicted values**.

Another very important aspect of TTS modeling is teacher forcing, which means that during training we provide various pieces of ground truth information to the model and at inference provide equivalent predicted values.

Training a model to directly predict a spectrogram from text by itself does not work, for a few reasons:

- Spectrogram Synthesis is a difficult enough problem that most models will not converge to anything meaningful if its only input is text.
- The prediction target is extremely ambiguous. There are several correct ways to read any sentence. For training to be smooth, the input features need to be enough to figure out the speaking pattern for most training utterances.

The most standard form of teacher forcing in auto-regressive systems is for each decoder step to receive the ground truth prediction from the previous step. In other words, each decoder step predicts an audio frame. During training, the ground truth audio frame is passed to the next decoder step. During inference, the predicted audio frame is passed to the next decoder step. In Tacotron 2, the pre-net applies a large amount of dropout to this input to avoid overfitting.

Some other common forms of ground truth information that have been found to be useful are:

- Pitch: By providing the pitch, aka. the fundamental frequency (F0), for each character, a model is able to better learn and mimic a variety of natural speaking patterns.
- Speaking Rate: By providing the length of the ground truth spectrogram as an input feature, the model is able to easily disambiguate how long the final audio should be. At inference time a user can then manually change the input value to make the model speak as slow or as fast as they want.
- Style Embeddings: By training an auto-encoder on the TTS training data, it is possible to represent very complex speaking styles with utterance-level embeddings. Taking a style embedding from one utterance to make a speaker say a different sentence with the same speaking characteristics is referred to as style transfer.

### Ground Truth Aligned (GTA) Inference

Let's take an utterance and compare the output of Tacotron2 when teacher forcing is used versus when it is not. The teacher forcing ensures that the predicted spectrogram is the same length as the ground truth spectrogram, so this type of inference is often referred to as being ground truth aligned (GTA).

We see that with teacher forcing, the model output sounds almost exactly like the original audio. This is how the model learns how to generate audio that sounds realistic and high-quality.

However, at inference time we see that the pitch of the speaker is very different. Without teacher forcing, and without receiving the pitch as an input feature, the model has no way of knowing what pitch to use. So most likely, all predicted utterances will end up using the average pitch observed at training time.

## Duration Prediction

A large weakness of the original Tacotron 2 model is its attention mechanism, which does not enforce the required monotonicity constraint (ie. the decoder must pay attention to each character once in sequential increasing order). As a result, the attention is not robust. It often skips words, repeats words, or encounters catastrophic failures where the output becomes unintelligible.

There are some attention mechanisms such as forward attention which try to address this.

The most standard approach today is to do explicit duration prediction. This means that the model encoder predicts the duration (ie. number of spectrogram frames) of each character directly, instead of relying on the attention to determine it implicitly.

Replacing the attention mechanism in Tacotron 2 with duration prediction, eg. Non-Attentive Tacotron, has historically been a common and necessary optimization to make it robust enough for use in enterprise applications. Though it gained visibility in academic literature primarily due to its use in modern transformer based model architectures such as FastSpeech and FastPitch.

The biggest drawback of this approach is that you need to get the ground truth character duration information. Some methods for doing this are:

- The preferred method in NeMo is to Jointly train an alignment model that measures the similarity between characters and spectrogram frames.
- Run forced alignment, such as with the Montreal Forced Aligner.
- Infer the duration information from the attention map of a teacher model, such as Tacotron 2.

## Parallel Models

There are some significant weaknesses to auto-regressive systems. Most notably:

- Spectrograms are long (100s-1000s of frames), so generating them one frame at a time makes inference slow.
- They are typically implemented using RNN based architectures, which are slow to train.
- The user has little control over how the sentence is spoken.

Using duration prediction enables us to remove the auto-regressive inference and predict every spectrogram frame in parallel. This makes the inference speed up to 100x faster, making it highly preferable for deploying and serving to users.

### FastPitch

FastPitch is a parallel transformer-based model with pitch and duration control and prediction.

![image](https://user-images.githubusercontent.com/73081144/226225280-d3f7ed30-8c7b-412e-bf04-7b953615fff5.png)

At a high level it contains:

1. An encoder consisting of a feed-forward transformer block (FFTr), which transforms the input character embeddings into character pronunciation embeddings.
1. A temporal CNN which takes the encoder output and predicts the duration and pitch of each character. At training time, the ground truth pitch and duration information are fed to the model (similar to teacher forcing).
1. Each encoder output is repeated a number of times equal to the predicted duration. The repeated encoder output is the same length as the final spectrogram. For example, for characters 'abc' and predicted durations (2, 3, 1) we get the encoder output repeated 'aabbbc'.
1. A decoder consisting of a FFTr that transforms this encoder output into the predicted spectrogram.

Some advantages to this approach are:

- The duration prediction makes the output consistent and robust.
- The model inference is fast, able to synthesize up to 1000 seconds of audio every second on an A100 GPU.
- You can customize the prosody by manually selecting the pitch and duration of each character or word.

### Drawbacks

One weakness of parallel models is that without auto-regressive teacher forcing, the model is unable to reliably predict/reconstruct the original utterance. Primarily due to the inputs not fully capturing the unpredictable variability/ambiguity in the possible outputs. The result is that the model learns an average over possible outputs, creating spectrograms that look unrealistically "smooth", degrading the audio quality (https://arxiv.org/abs/2202.13066). The predicted spectrogram looks very smooth and well-behaved compared to the ground truth which has a more variation and detail.

This problem can be partially alleviated by fine-tuning the spectrogram inversion model (described in the next section) directly on the predicted spectrograms.

## Research

There is ongoing research into improving the audio quality and expressiveness of models like FastPitch, with a few methods that have shown promising results being:

- Train a variational auto-encoder (VAE) that can compress all utterance-level variation/prosody into an embedding and provide it as a feature it to the decoder (https://arxiv.org/abs/1812.04342).
- Use normalizing flows (sometimes called glow models) to directly learn the variability in the training data (eg. RAD-TTS).
- Use generative adversarial networks (GAN) based training to make the predicted spectrograms harder to tell apart from real spectrograms.
- Avoid the spectrogram entirely by training an end-to-end model that can go directly from text to audio (eg. VITS).

## Audio Synthesis (Spectrogram Inversion) | Vocoder

Reconstructing audio from a spectrogram can theoretically be done using the inverse FFT (iFFT). However there are a few complications in doing this with our model.

1. The mel spectrogram does not contain the phase information output by the original FFT.
1. The predicted spectrogram is imperfect. It is likely smoother than the ground truth and may contain noise or other unnatural characteristics/artifacts.

We could approximate the phase information using the Griffin-Lim algorithm. However its just an approximation, and does not help with issue (2).

So instead we train a separate model called a **vocoder** to generate the audio. This model can learn to do the audio reconstruction more accurately. If necessary we can train it directly on the ground-truth aligned spectrograms produced by our model to teach it to denoise the output automatically, often called **GTA fine-tuning**.


### Modeling approach

Spectrogram inversion is a sequence-to-sequence problem.

The input sequence is the mel spectrogram with 80 mel bands for each audio frame, and the output is a sequence of audio samples. For example, the input sequence may have 100 audio frames making it dimension [100, 80] and have a corresponding audio output sequence of dimension [25,600, 1]

The audio samples being discrete 16-bit integers can be predicted using a softmax layer size 216. Or we can divide them by 216 to scale them to the range [-1, 1] and then predict them as a continuous value using an appropriate activation like tanh.

Most sequence-to-sequence problems rely on attention or other upsampling methods, but in this case it is unnecessary because the ratio of input to output elements is fixed. So given any input, we already know the final output length and which output samples correspond to which input frames.

The ratio is dependent on length of each audio frame.

In NeMo, for 22.05 kHz audio, we use a audio window stride of 256 meaning there are exactly 256 audio samples for each audio spectrogram frame. For 44.1 kHz we double the stride to 512.

This means each audio frame represents approximately (256 / 22.05) = 11.61 ms of audio.

The first step for most approaches is to upsample our input sequence to match the final output length. This can be done by duplicating each audio frame a number of times equal to your audio stride/ratio.

Or if your stride is a power of 2 (like the ones we selected) then you can upsample the sequence more effectively using transposed convolutions (aka. deconvolutional layers).

Once the input and output sequences are the same length, you can use any number of models to predict the output.

### WaveNet

The first mainstream vocoder was WaveNet, a very large auto-regressive dilated causal CNN. For each predicted audio sample, the CNN predicts a softmax probability across all possible 216 sample values.

Here auto-regressive means every audio sample is predicted by looking at the entire history of previously predicted audio samples. Dilated means it samples a few past audio samples spread over a wide range, instead of processing every past sample or only recent samples. Causal means the CNN only uses information from past predictions; it does not condition on audio samples after it.

![image](https://user-images.githubusercontent.com/73081144/226228044-9b19ebfd-7050-44ed-a207-993119c5bfe3.png)

This system is very accurate, but also very slow. Largely because of the auto-regressive system predicting 1 sample at a time for an output that is 10,000s to 100,000s of samples long. Its real-time factor (RTF) is on the order of 100, meaning it takes up to 100 seconds to reconstruct 1 second of audio. This makes it impractical to use in most applications.

### HiFi-GAN

The most common vocoder used in NeMo is HiFi-GAN. The architecture is similar to WaveNet. The main difference is that it is smaller, and not auto-regressive. This allows it to reach a speed of around 0.01 RTF; 10,000x faster than WaveNet.

The main way that HiFi-GAN achieves this speed with minimal sacrifice to perceived audio quality is through adversarial training, treating the vocoder like a generative adversarial network (GAN).

To do this, we jointly train the vocoder with a set of discriminators that try to predict whether the synthesized/reconstructed audio is real or not. The goal being to trick the discriminators so they cannot systematically tell the difference between the synthesized audio and the original audio. Doing this allows us to get realistic audio with a significantly smaller model.

Notably it uses multiple scale discriminators, which are temporal CNNs that try to classify the audio as real or fake after average pooling sets of adjacent audio samples, and period discriminators which try to classify using audio sampled over different periods.

In addition to penalizing the model if the discriminator can classify the synthesized audio as fake, it also uses feature matching loss to penalize the model if the distribution of intermediate layer outputs in the discriminator networks differ between the real and synthesized audio.

![image](https://user-images.githubusercontent.com/73081144/226228413-5833505a-3a3b-4fb7-b7d2-656a33514a52.png)

HiFi-Gan scale (a) and period (b) discriminators.

### WaveRNN

Many people tend to avoid RNNs because of how slowly they train compared to CNNs and Transformers.

However, they are one of the most used architectures in real-world applications and industry due to their small compute requirements and memory footprint at inference time. This makes them ideal for low-latency and low-power situations like on-device TTS.

WaveRNN is a popular vocoder for those who want to do spectrogram inversion on-device.

The model itself manages to minimize compute requirements in several different ways that are too complex to summarize adequately here. But a few highlights would be:

1. Instead of using a 216 sized softmax, it uses two 28 sized softmaxes to predict the first and last 8-bits of the 16-bit audio sample separately.
1. Uses a subscaling system to have the RNN predict 16 audio samples at a time instead of 1 sample at a time.
1. Uses sparse RNN training during which the smallest model weights in the RNN are periodically set to zero. Inference is then done efficiently using sparse vectors.

## Model Evaluation

There are no well-established objective metrics for evaluating how good a TTS model is. Rather, quality is usually based on human opinion or perception, commonly measured through surveys.

The most common type of survey for evaluating TTS quality is mean opinion score (MOS), in which listeners rate the quality of TTS samples on a 1 to 5 scale.

Another common alternative is MUSHRA in which users are provided a reference (the ground truth audio) and asked to rate several TTS samples relative to the reference.

There are some metrics which are occasionally used to try and measure audio quality such as MCD-DTW, PESQ, and STOI. But these have very limited accuracy and usefulness.

The lack of objective numerical metrics that can be trained on is a large reason as to why many state of the art models rely on GAN based training to get good quality.
