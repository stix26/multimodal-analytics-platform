# 🔌 API Reference

Complete REST API documentation for the Advanced Multi-Modal Computational Analytics Platform.

---

## Base URL

```
http://127.0.0.1:5000
```

---

## Authentication

Currently, no authentication is required for API endpoints. All endpoints are publicly accessible when the server is running.

---

## Endpoints

### 1. Dashboard

**GET** `/`

Main dashboard page serving the web interface.

**Response:** HTML page with the interactive dashboard

**Example:**
```bash
curl http://127.0.0.1:5000/
```

---

### 2. Multi-Modal Analysis

**POST** `/api/analyze`

Analyze multi-modal data combining image, audio, and metadata processing.

**Content-Type:** `multipart/form-data`

**Parameters:**
- `image` (file, optional): Image file (JPEG, PNG)
- `audio` (file, optional): Audio file (WAV, MP3)  
- `metadata` (string, optional): JSON metadata

**Response:**
```json
{
  "status": "success|error",
  "image_features": {
    "shape": [1, 1000],
    "sample": [0.1, 0.2, ...]
  },
  "audio_features": {
    "shape": [1, 512], 
    "sample": [0.3, 0.4, ...]
  },
  "integrated_data": {
    "combined_features": [...],
    "total_dimensions": 1512,
    "metadata_included": true
  },
  "errors": []
}
```

**Example:**
```bash
curl -X POST \
  -F "image=@sample_image.jpg" \
  -F "audio=@sample_audio.wav" \
  -F 'metadata={"source": "api", "quality": "high"}' \
  http://127.0.0.1:5000/api/analyze
```

**Features:**
- **Image Processing**: ResNet50 model extracts 1000-dimensional features
- **Audio Processing**: Wav2Vec2 model extracts 512-dimensional features  
- **Data Integration**: Combines features using StandardScaler normalization
- **Metadata Support**: Integrates additional JSON metadata into feature vectors

---

### 3. Mathematical Analysis

**POST** `/api/math`

Perform symbolic mathematical computations using SymPy.

**Content-Type:** `application/json`

**Parameters:**
```json
{
  "expression": "x**3 + 2*x**2 - x + 1"
}
```

**Response:**
```json
{
  "status": "success|error", 
  "original": "x**3 + 2*x**2 - x + 1",
  "derivative": "3*x**2 + 4*x - 1",
  "integral": "x**4/4 + 2*x**3/3 - x**2/2 + x",
  "simplified": "x**3 + 2*x**2 - x + 1",
  "error": null
}
```

**Example:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"expression": "sin(x)*cos(x)"}' \
  http://127.0.0.1:5000/api/math
```

**Supported Operations:**
- **Symbolic Differentiation**: Computes derivatives using SymPy
- **Symbolic Integration**: Computes integrals when possible
- **Expression Simplification**: Reduces expressions to canonical form
- **Expression Parsing**: Supports standard mathematical notation

---

### 4. Graph Analysis

**POST** `/api/graph`

Analyze graph data and relationships using NetworkX.

**Content-Type:** `application/json`

**Parameters:**
```json
{
  "nodes": [1, 2, 3, 4],
  "edges": [[1, 2], [2, 3], [3, 4], [4, 1]]
}
```

**Response:**
```json
{
  "status": "success|error",
  "analysis": {
    "node_count": 4,
    "edge_count": 4, 
    "density": 0.67,
    "is_connected": true,
    "clustering_coefficient": 0.33,
    "average_path_length": 1.5
  },
  "error": null
}
```

**Example:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nodes": [1,2,3], "edges": [[1,2],[2,3]]}' \
  http://127.0.0.1:5000/api/graph
```

**Graph Metrics:**
- **Basic Properties**: Node/edge counts, density
- **Connectivity**: Connected components analysis  
- **Clustering**: Local and global clustering coefficients
- **Path Analysis**: Average shortest path lengths

---

### 5. Health Check

**GET** `/health`

Simple health check endpoint for monitoring server status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-04T16:15:30Z"
}
```

**Example:**
```bash
curl http://127.0.0.1:5000/health
```

---

## Error Handling

All endpoints return structured error responses:

```json
{
  "status": "error",
  "message": "Detailed error description",
  "code": "ERROR_CODE",
  "timestamp": "2025-11-04T16:15:30Z"
}
```

**Common Error Codes:**
- `400`: Bad Request - Invalid input data
- `415`: Unsupported Media Type - Invalid file format
- `500`: Internal Server Error - Processing failure

---

## File Upload Limits

- **Maximum file size**: 16MB per file
- **Supported image formats**: JPEG, PNG, GIF
- **Supported audio formats**: WAV, MP3, FLAC
- **Metadata format**: Valid JSON strings

---

## Sample Requests

### Complete Multi-Modal Analysis
```bash
# Upload image + audio + metadata
curl -X POST \
  -F "image=@project/samples/images/gradient_sample.jpg" \
  -F "audio=@project/samples/audio/sine_wave_440hz.wav" \
  -F 'metadata=@project/samples/metadata/basic_metadata.json' \
  http://127.0.0.1:5000/api/analyze
```

### Mathematical Expression Analysis  
```bash
# Analyze complex mathematical expression
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"expression": "integrate(x*sin(x), x)"}' \
  http://127.0.0.1:5000/api/math
```

### Graph Network Analysis
```bash
# Analyze social network structure
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nodes": [1,2,3,4,5], "edges": [[1,2],[2,3],[3,4],[4,5],[5,1],[1,3]]}' \
  http://127.0.0.1:5000/api/graph
```

---

## Integration Examples

### Python Integration
```python
import requests

# Multi-modal analysis
files = {
    'image': open('image.jpg', 'rb'),
    'audio': open('audio.wav', 'rb')
}
data = {'metadata': '{"source": "python_client"}'}

response = requests.post('http://127.0.0.1:5000/api/analyze', 
                        files=files, data=data)
result = response.json()

# Mathematical analysis  
math_data = {"expression": "diff(x**2 + 2*x + 1, x)"}
response = requests.post('http://127.0.0.1:5000/api/math',
                        json=math_data)
result = response.json()
```

### JavaScript Integration
```javascript
// Multi-modal analysis with fetch API
const formData = new FormData();
formData.append('image', imageFile);
formData.append('audio', audioFile);
formData.append('metadata', JSON.stringify({source: 'web_client'}));

fetch('http://127.0.0.1:5000/api/analyze', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));

// Mathematical analysis
fetch('http://127.0.0.1:5000/api/math', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({expression: 'sin(x) + cos(x)'})
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider implementing:
- Request rate limits per IP
- File upload frequency limits  
- Concurrent processing limits

---

## Development & Testing

### Running the API Server
```bash
cd project/config
python app.py
```

### API Testing with Sample Data
The platform includes sample files for testing:
- **Images**: `project/samples/images/`
- **Audio**: `project/samples/audio/`  
- **Metadata**: `project/samples/metadata/`

### Enable Debug Mode
Set `debug=True` in `app.py` for detailed error messages during development.

---

*Last updated: November 2025*
