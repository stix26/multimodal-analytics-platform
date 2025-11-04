# 🎯 Sample Files for AI-Powered Multi-Modal Analytics Platform

This directory contains sample files to test and demonstrate all features of the AI platform.

## 📁 Directory Structure

```
samples/
├── audio/           # Audio samples for testing
├── images/          # Image samples for testing  
├── metadata/        # JSON metadata examples
├── combined/        # Multi-modal test scenarios
└── README.md        # This file
```

## 🎵 Audio Samples

### `audio/sine_wave_440hz.wav`
- **Type**: Pure sine wave
- **Frequency**: 440 Hz (A note)
- **Duration**: 3 seconds
- **Use**: Basic audio processing test

### `audio/a_major_chord.wav`
- **Type**: Musical chord
- **Notes**: A (440 Hz) + C# (554.37 Hz) + E (659.25 Hz)
- **Duration**: 3 seconds
- **Use**: Complex harmonic analysis

### `audio/frequency_sweep.wav`
- **Type**: Frequency sweep
- **Range**: 200 Hz to 2000 Hz
- **Duration**: 3 seconds
- **Use**: Dynamic frequency analysis

## 🖼️ Image Samples

### `images/gradient_sample.jpg`
- **Type**: Color gradient
- **Size**: 400×300 pixels
- **Content**: Red-green-blue gradient
- **Use**: Color transition analysis

### `images/red_sample.jpg`
- **Type**: Solid color
- **Color**: Pure red (255,0,0)
- **Size**: 300×300 pixels
- **Use**: Single color analysis

### `images/green_sample.jpg`, `blue_sample.jpg`, `purple_sample.jpg`
- **Type**: Solid colors
- **Use**: Color-specific feature extraction

## 📋 Metadata Examples

### `metadata/basic_metadata.json`
**Simple metadata for quick testing**
```json
{
  "source": "sample_upload",
  "category": "test", 
  "quality": "high",
  "confidence": 0.95
}
```

### `metadata/advanced_metadata.json`
**Comprehensive metadata with nested objects**
- Analysis configuration
- Technical specifications
- ML parameters
- Session data

### `metadata/audio_metadata.json`
**Audio-specific metadata**
- Audio properties (sample rate, duration, channels)
- Content analysis parameters
- Quality metrics
- Expected features

### `metadata/multimodal_metadata.json`
**Multi-modal analysis metadata**
- Experiment information
- Image and audio context
- Integration goals
- Validation criteria

### `metadata/production_metadata.json`
**Enterprise/production metadata**
- Deployment information
- Business context
- Performance requirements
- Security settings

## 🔗 Combined Test Scenarios

### `combined/test_batch_1.json`
**Batch testing configuration**
- Multiple sample combinations
- Validation criteria
- Expected outcomes

## 🧪 How to Use These Samples

### 1. **Quick Test** (Basic)
1. Go to http://127.0.0.1:5000
2. Upload: `images/gradient_sample.jpg`
3. Metadata: Copy from `metadata/basic_metadata.json`
4. Click "Start Analysis"

### 2. **Audio Test** (Single Modal)
1. Upload: `audio/sine_wave_440hz.wav`
2. Metadata: Copy from `metadata/audio_metadata.json`
3. See audio-only analysis

### 3. **Multi-Modal Test** (Full Platform)
1. Upload: `images/red_sample.jpg`
2. Upload: `audio/a_major_chord.wav`
3. Metadata: Copy from `metadata/multimodal_metadata.json`
4. See combined 1522-dimensional analysis!

### 4. **Mathematical Test**
1. Go to "Symbolic Mathematics" section
2. Try: `sin(x**2) + exp(cos(x)) + log(sqrt(x))`
3. See calculus results

### 5. **API Testing**
```bash
# Image + Audio + Metadata
curl -X POST \
  -F "image=@samples/images/gradient_sample.jpg" \
  -F "audio=@samples/audio/a_major_chord.wav" \
  -F "metadata=$(cat samples/metadata/multimodal_metadata.json)" \
  http://127.0.0.1:5000/api/analyze

# Mathematical Analysis
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"expression": "x**3 + 2*x**2 - x + 1"}' \
  http://127.0.0.1:5000/api/math
```

## 🎯 Expected Results

### Image Analysis (ResNet50)
- **Dimensions**: 1 × 1000 features
- **Sample values**: Float array with semantic features
- **Processing time**: 1-2 seconds

### Audio Analysis (Wav2Vec2)
- **Dimensions**: 1 × 512 features  
- **Sample values**: Float array with audio features
- **Processing time**: 0.5 seconds

### Multi-Modal Integration
- **Combined dimensions**: 1 × 1522 total features
- **Integration method**: StandardScaler normalization
- **Requires**: Both image AND audio files

## 🚀 Pro Tips

1. **Start Simple**: Use `basic_metadata.json` for first tests
2. **Test Audio**: Try different audio samples to see feature variations
3. **Compare Results**: Upload different images to see feature differences
4. **Multi-Modal**: Always upload both image AND audio for integration
5. **JSON Validation**: Ensure metadata is valid JSON format

## 🔧 Troubleshooting

- **No audio features**: Upload a `.wav` file (MP3 may not work)
- **No integration**: Need both image AND audio files
- **JSON error**: Validate JSON syntax in metadata
- **File size**: Keep files under 16MB limit

**These samples ensure you can immediately test and demonstrate all platform capabilities!** 🎉
