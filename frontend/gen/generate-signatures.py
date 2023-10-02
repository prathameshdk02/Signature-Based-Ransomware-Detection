from pathlib import Path
import hashlib

samplePath = './liveSamples/'

samples = [file for file in Path(samplePath).iterdir() if file.is_file()]
sampleCount = len(samples)
hashGenerations = 0

print(f"\nFile Hashes from \"{samplePath}\":")

for sample in samples:
    try:
        hash = hashlib.sha256(Path(sample).read_bytes()).hexdigest()
        hashGenerations += 1
        print(hash)
    except Exception as e:
        print(e)

print(f"\nGenerated over {hashGenerations} hashes from {sampleCount} samples.\nEncountered Errors were {sampleCount - hashGenerations}")