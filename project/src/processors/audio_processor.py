import torch
import pandas as pd
import numpy as np
try:
    import torchaudio
    TORCHAUDIO_AVAILABLE = True
except ImportError:
    TORCHAUDIO_AVAILABLE = False
    print("Warning: torchaudio not available, using basic audio processing")


class AudioProcessor:
    def __init__(self):
        """Initialize audio processor with fallback for missing dependencies."""
        self.sample_rate = 16000
        self.torchaudio_available = TORCHAUDIO_AVAILABLE
        
        if TORCHAUDIO_AVAILABLE:
            try:
                self.bundle = torchaudio.pipelines.WAV2VEC2_BASE
                self.model = self.bundle.get_model()
                self.model.eval()
                self.sample_rate = self.bundle.sample_rate
                print("✅ Wav2Vec2 model loaded successfully")
            except Exception as e:
                print(f"Warning: Could not load Wav2Vec2, using fallback: {e}")
                self.bundle = None
                self.model = None
        else:
            self.bundle = None
            self.model = None
    
    def extract_features(self, audio_path):
        """
        Extract features from audio file.
        
        Args:
            audio_path: Path to audio file or file-like object
            
        Returns:
            torch tensor of extracted features
        """
        if not self.torchaudio_available:
            # Return mock features when torchaudio is not available
            print("⚠️ Using mock audio features (torchaudio not available)")
            return torch.randn(1, 512)  # Mock 512-dimensional features
        
        try:
            waveform, sample_rate = torchaudio.load(audio_path)
            
            if self.model is None:
                # Fallback: return basic statistical features as tensor
                features = torch.tensor([
                    waveform.mean().item(),
                    waveform.std().item(),
                    waveform.max().item(),
                    waveform.min().item(),
                    float(waveform.shape[1] / sample_rate)  # duration
                ])
                return features.unsqueeze(0)  # Add batch dimension
            
            # Resample if necessary
            if sample_rate != self.sample_rate:
                waveform = torchaudio.functional.resample(
                    waveform, sample_rate, self.sample_rate
                )
            
            with torch.no_grad():
                features, _ = self.model.extract_features(waveform)
                # Average over time dimension
                features = features[0].mean(dim=1)
            
            return features
            
        except Exception as e:
            print(f"⚠️ Audio processing error: {e}, using mock features")
            return torch.randn(1, 512)  # Mock features as fallback
    
    def extract_statistical_features(self, audio_path):
        """Extract statistical features from audio."""
        if not self.torchaudio_available:
            # Return mock statistical features
            features = {
                'mean': 0.1,
                'std': 0.3,
                'max': 1.0,
                'min': -1.0,
                'duration': 2.5
            }
            return pd.Series(features)
            
        try:
            waveform, sample_rate = torchaudio.load(audio_path)
            waveform = waveform.numpy()
            
            features = {
                'mean': np.mean(waveform),
                'std': np.std(waveform),
                'max': np.max(waveform),
                'min': np.min(waveform),
                'duration': waveform.shape[1] / sample_rate
            }
            
            return pd.Series(features)
        except Exception as e:
            print(f"⚠️ Statistical audio processing error: {e}")
            # Return mock features as fallback
            features = {
                'mean': 0.0,
                'std': 0.1,
                'max': 0.5,
                'min': -0.5,
                'duration': 1.0
            }
            return pd.Series(features)

