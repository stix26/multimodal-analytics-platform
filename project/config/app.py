from flask import Flask, request, render_template, jsonify, send_from_directory
import torch
import pandas as pd
import os
from werkzeug.utils import secure_filename
import json

import sys
import os
# Add parent directory to path to enable imports
sys.path.append('..')
sys.path.append('../..')

from src.processors.image_processor import ImageProcessor
from src.processors.audio_processor import AudioProcessor
from src.processors.data_integrator import DataIntegrator
from src.utils.math_analyzer import MathAnalyzer
from src.utils.graph_analyzer import GraphAnalyzer

app = Flask(__name__, template_folder='../src/templates', static_folder='../src/static')
app.config['UPLOAD_FOLDER'] = '../src/static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize processors
image_processor = ImageProcessor()
audio_processor = AudioProcessor()
data_integrator = DataIntegrator()
math_analyzer = MathAnalyzer()
graph_analyzer = GraphAnalyzer()


@app.route('/')
def dashboard():
    """Main dashboard page."""
    return render_template('dashboard.html')


@app.route('/api/analyze', methods=['POST'])
def analyze_multimodal():
    """Analyze multi-modal data (image + audio + metadata)."""
    try:
        print(f"DEBUG: Request content type: {request.content_type}")
        print(f"DEBUG: Request files: {list(request.files.keys())}")
        print(f"DEBUG: Request form: {list(request.form.keys())}")
        results = {
            'status': 'processing',
            'image_features': None,
            'audio_features': None,
            'integrated_data': None,
            'errors': []
        }
        
        # Handle image file upload
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file.filename:
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
                
                try:
                    image_features = image_processor.process_image(image_path)
                    results['image_features'] = {
                        'shape': list(image_features.shape),
                        'sample': image_features.flatten()[:10].tolist()
                    }
                except Exception as e:
                    results['errors'].append(f"Image processing error: {str(e)}")
        
        # Handle audio file upload
        if 'audio' in request.files:
            audio_file = request.files['audio']
            if audio_file.filename:
                filename = secure_filename(audio_file.filename)
                audio_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                audio_file.save(audio_path)
                
                try:
                    audio_features = audio_processor.extract_features(audio_path)
                    results['audio_features'] = {
                        'shape': list(audio_features.shape) if hasattr(audio_features, 'shape') else len(audio_features),
                        'sample': audio_features.flatten()[:10].tolist() if hasattr(audio_features, 'flatten') else str(audio_features)[:100]
                    }
                except Exception as e:
                    results['errors'].append(f"Audio processing error: {str(e)}")
        
        # Handle metadata
        metadata = {}
        if request.form.get('metadata'):
            try:
                metadata = json.loads(request.form.get('metadata'))
            except:
                metadata = {'metadata': request.form.get('metadata')}
        # Remove the request.json check that was causing the 415 error
        
        # Combine modalities if we have data
        if results['image_features'] or results['audio_features']:
            try:
                # Create sample data for integration
                img_features = image_features if results['image_features'] else None
                aud_features = audio_features if results['audio_features'] else None
                
                if img_features is not None and aud_features is not None:
                    metadata_df = pd.DataFrame([metadata])
                    integrated = data_integrator.combine_modalities(
                        img_features, aud_features, metadata_df
                    )
                    results['integrated_data'] = {
                        'shape': list(integrated.shape),
                        'feature_count': integrated.shape[1]
                    }
            except Exception as e:
                results['errors'].append(f"Integration error: {str(e)}")
        
        results['status'] = 'completed'
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/math', methods=['POST'])
def analyze_math():
    """Perform symbolic mathematical analysis."""
    try:
        # Handle both JSON and form data
        if request.is_json:
            data = request.json
        else:
            # Handle form data
            data = request.form.to_dict()
        expression = data.get('expression', '')
        
        if not expression:
            return jsonify({'error': 'No expression provided'}), 400
        
        result = math_analyzer.symbolic_analysis(expression)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/graph', methods=['POST'])
def analyze_graph():
    """Perform graph analysis on data."""
    try:
        # Handle both JSON and form data
        if request.is_json:
            data = request.json
        else:
            data = request.form.to_dict()
        # Expect CSV-like data or JSON array
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            result = graph_analyzer.analyze_relationships(df)
            return jsonify(result)
        else:
            return jsonify({'error': 'No data provided'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'processors': {
            'image': 'ready',
            'audio': 'ready',
            'data_integrator': 'ready'
        }
    })


if __name__ == '__main__':
    print("="*70)
    print("AI-Powered Multi-Modal Analytics Platform")
    print("="*70)
    print("Starting server...")
    print("Access the dashboard at: http://127.0.0.1:5000")
    print("="*70)
    app.run(debug=True, host='0.0.0.0', port=5000)

