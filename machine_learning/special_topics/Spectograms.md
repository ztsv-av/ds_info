# Spectrograms

To train audio model, we convert audio to spectograms.

While raw audio shows amplitude versus time and is useful for easily recording and listening, it is not optimal when it comes to processing.

For processing, it is usually preferable to represent the audio as a spectrogram which shows frequency versus time. Specifically, we:

- Group together audio samples into a much smaller set of time buckets, called audio frames. An audio frame will usually bucket around 50ms of audio.
- For each audio frame, use the Fast Fourier transform (FFT) to calculate the magnitude (ie. energy, amplitude or "loudness") and phase (which we don't use) of each frequency band (ie. pitch).
- Translate the original frequency bands, measured in units of hertz (Hz), into units of mel frequency. The output is called a **mel spectrogram**.

We then use the mel spectrogram as our final audio representation. The only thing we lose during this process is the phase information, the implications of which we will discuss more later on.

The reason for converting from hertz to mel frequency is that hertz are a physical measurement, while mel frequency better captures how humans perceive sound. Human ears are more sensitive to low frequencies than high frequencies. So low frequency bands would have large impact on the perceived sound while high frequency bands might have little to no effect. On the mel scale, the impact of different frequency bands are more evenly distributed.

## Why use a spectrogram?

In addition to the mel spectrogram providing handcrafted features that are closer to human perception and easier to predict, there are a few other advantages to using it over audio samples.

1. Computational Efficiency

One reason to use a spectrogram is that it is a lot more computationally efficient than processing raw audio.

Take for example a 10 second piece of audio sampled at 44.1 kHz.

This audio has 10 * 44,100 = 441,000 audio samples.

For TTS we will represent this same audio with audio frames that are overlapping such that there is about 1 audio frame per 10ms (0.01s). For each audio frame we have 80 frequency bands.

Our final spectrogram has 80 bands * 10s * / (0.01s) = 80,000

So we made our data about 5 times smaller.

Even in other fields that deal with audio, such as digital signal processing (DSP), it is common practice to reduce computation time by computing the FFT, running mathematical calculations and manipulations in the frequency domain, and then converting the final spectrogram back to audio with the inverse FFT.

2. Shorter 2D sequence length

In the example above, the dimension of our input goes from being (441,000, 1) to (1000, 80). Instead of having a very long 1-dimensional time series, we instead have a much shorter sequence of multi-dimensional features.

This dimensionality works better with most modern deep learning models.

Most models work better representing large chunks/sequences of information as higher dimension vectors (eg. embeddings).

RNN/LSTM architectures have latency proportional to the length of the sequence, can struggle to remember information for sequences over a few hundred tokens long, and are more prone to vanishing/exploding gradients as the sequence gets longer.

With 2 dimensions we can effectively use CNNs by running temporal convolutions over the time dimension. Or by applying 2d convolutions to the spectrogram exactly as if it were an image in computer vision.

Transformers require computation/memory that is proportional to the length of the sequence squared. This means we can easily use large transformers for relatively short sequences like in NLP, smaller transformers for longer sequences like spectrogram data, and are impractical to use on very long sequences like audio samples.

## Fast Fourier transform (FFT)

The "Fast Fourier Transform" (FFT) converts a signal into individual spectral components and thereby provides frequency information about the signal. Strictly speaking, the FFT is an optimized algorithm for the implementation of the "Discrete Fourier Transformation" (DFT). A signal is sampled over a period of time and divided into its frequency components. These components are single sinusoidal oscillations at distinct frequencies each with their own amplitude and phase.

![image](https://user-images.githubusercontent.com/73081144/226219857-e4cf1c39-5d28-4e62-8d6a-1eee7108c7aa.png)

In the first step, a section of the signal is scanned and stored in the memory for further processing. Two parameters are relevant:

1. The sampling rate or sampling frequency fs of the measuring system (e.g. 48 kHz). This is the average number of samples obtained in one second (samples per second).
2. The selected number of samples; the blocklength BL. This is always an integer power to the base 2 in the FFT (e.g., 2^10 = 1024 samples).

From the two basic parameters fs and BL, further parameters of the measurement can be determined.

- Bandwidth fn (= Nyquist frequency). This value indicates the theoretical maximum frequency that can be determined by the FFT.

fn = fs / 2
 
For example at a sampling rate of 48 kHz, frequency components up to 24 kHz can be theoretically determined. In the case of an analog system, the practically achievable value is usually somewhat below this, due to analog filters - e.g. at 20 kHz.

- Measurement duration D. The measurement duration is given by the sampling rate fs and the blocklength BL.

D = BL / fs.

At fs = 48 kHz and BL = 1024, this yields 1024/48000 Hz = 21.33 ms

- Frequency resolution df. The frequency resolution indicates the frequency spacing between two measurement results.

df = fs / BL

At fs = 48 kHz and BL = 1024, this gives a df of 48000 Hz / 1024 = 46.88 Hz.

In practice, the sampling frequency fs is usually a variable given by the system. However, by selecting the blocklength BL, the measurement duration and frequency resolution can be defined. The following applies:

- A small blocklength results in fast measurement repetitions with a coarse frequency resolution.
- A large blocklength results in slower measuring repetitions with fine frequency resolution.

![image](https://user-images.githubusercontent.com/73081144/226220525-a9f4e005-d4da-4d5d-ba2a-244f468a08fa.png)

**more here: https://www.nti-audio.com/en/support/know-how/fast-fourier-transform-fft#:~:text=The%20%22Fast%20Fourier%20Transform%22%20(,frequency%20information%20about%20the%20signal.**
