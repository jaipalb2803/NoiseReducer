import noisereduce as nr
import librosa
import soundfile as sf

def process_audio(input_path, output_path):
    # Load the noisy audio file
    data, rate = librosa.load(input_path, sr=None, mono=False)  # Load stereo if needed

    # Reduce noise
    reduced_noise = nr.reduce_noise(y=data, sr=rate)

    # Save the noise-reduced audio file
    sf.write(output_path, reduced_noise.T, rate)  # Transpose if stereo
