import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import networkx as nx
import torch


class DataIntegrator:
    def __init__(self):
        """Initialize data integrator with scaler."""
        self.scaler = StandardScaler()
        self.is_fitted = False
    
    def combine_modalities(self, image_features, audio_features, metadata):
        """
        Combine features from different modalities.
        
        Args:
            image_features: numpy array of image features
            audio_features: torch tensor or numpy array of audio features
            metadata: pandas DataFrame with metadata
            
        Returns:
            numpy array of combined and scaled features
        """
        # Convert image features to DataFrame with consistent column names
        if isinstance(image_features, np.ndarray):
            if len(image_features.shape) == 1:
                image_features = image_features.reshape(1, -1)
            img_df = pd.DataFrame(image_features, columns=[f'img_feat_{i}' for i in range(image_features.shape[1])])
        else:
            img_df = pd.DataFrame([image_features], columns=[f'img_feat_{i}' for i in range(len(image_features))])
        
        # Convert audio features to DataFrame with consistent column names
        if isinstance(audio_features, torch.Tensor):
            audio_np = audio_features.cpu().numpy()
            if len(audio_np.shape) == 1:
                audio_np = audio_np.reshape(1, -1)
            audio_df = pd.DataFrame(audio_np, columns=[f'audio_feat_{i}' for i in range(audio_np.shape[1])])
        else:
            if isinstance(audio_features, np.ndarray):
                if len(audio_features.shape) == 1:
                    audio_features = audio_features.reshape(1, -1)
                audio_df = pd.DataFrame(audio_features, columns=[f'audio_feat_{i}' for i in range(audio_features.shape[1])])
            else:
                audio_df = pd.DataFrame([audio_features], columns=[f'audio_feat_{i}' for i in range(len(audio_features))])
        
        # Convert metadata to DataFrame with string column names
        if not isinstance(metadata, pd.DataFrame):
            metadata = pd.DataFrame([metadata])
        
        # Ensure all metadata columns are strings and values are numeric
        metadata_processed = pd.DataFrame()
        for col, val in metadata.items():
            col_name = f'meta_{str(col)}'
            # Convert values to numeric if possible, otherwise use ordinal encoding
            if isinstance(val.iloc[0] if hasattr(val, 'iloc') else val, (int, float)):
                metadata_processed[col_name] = pd.to_numeric(val, errors='coerce').fillna(0)
            else:
                # Simple ordinal encoding for strings
                metadata_processed[col_name] = [hash(str(v)) % 1000 for v in (val if hasattr(val, '__iter__') and not isinstance(val, str) else [val])]
        
        # Reset indices for concatenation
        img_df.reset_index(drop=True, inplace=True)
        audio_df.reset_index(drop=True, inplace=True)
        metadata_processed.reset_index(drop=True, inplace=True)
        
        # Combine all features - only numeric columns
        combined = pd.concat([metadata_processed, img_df, audio_df], axis=1)
        
        # Ensure all data is numeric
        combined = combined.select_dtypes(include=[np.number])
        
        # Scale features
        if not self.is_fitted:
            scaled = self.scaler.fit_transform(combined)
            self.is_fitted = True
        else:
            scaled = self.scaler.transform(combined)
        
        return scaled
    
    def build_relationship_graph(self, data):
        """
        Build a NetworkX graph from data relationships.
        
        Args:
            data: pandas DataFrame with features
            
        Returns:
            NetworkX Graph object
        """
        G = nx.Graph()
        
        # Add nodes with features
        for i, row in data.iterrows():
            G.add_node(f"item_{i}", features=row.to_dict())
        
        # Add edges based on similarity (cosine similarity threshold)
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                # Calculate similarity (simplified - could use cosine similarity)
                similarity = np.dot(data.iloc[i].values, data.iloc[j].values)
                if similarity > 0.5:  # Threshold for edge creation
                    G.add_edge(f"item_{i}", f"item_{j}", weight=similarity)
        
        return G
    
    def analyze_graph(self, graph):
        """Analyze graph properties."""
        return {
            'nodes': graph.number_of_nodes(),
            'edges': graph.number_of_edges(),
            'density': nx.density(graph),
            'connected_components': nx.number_connected_components(graph)
        }

