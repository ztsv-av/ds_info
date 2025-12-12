# Audio

Audio is typically represented by a long sequence of numbers representing the audio amplitude at each point in time.

How often the audio samples are recorded is the sampling rate. Common sampling rates are 16 kHz, 22.05 kHz, and 44.1 kHz, with higher sampling rates producing more accurate, higher quality audio.

A sampling rate of 44.1 kHz means that we store 44,100 audio sample per second of audio. Each audio sample is typically stored as a 16-bit integer (a whole number ranging from -32,768 to +32,767). For machine learning, it is sometimes more convenient to rescale it and represent it as a continuous value between -1.0 and 1.0 using 32-bit floats.

![image](https://user-images.githubusercontent.com/73081144/226218935-8000de93-26b2-4378-88cb-3a05a1b1f56c.png)
