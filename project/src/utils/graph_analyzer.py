import networkx as nx
import pandas as pd
import numpy as np


class GraphAnalyzer:
    def __init__(self):
        """Initialize graph analyzer."""
        pass
    
    def analyze_relationships(self, data_df):
        """
        Analyze relationships in data using graph theory.
        
        Args:
            data_df: pandas DataFrame with features
            
        Returns:
            Dictionary with graph analysis results
        """
        # Create graph from correlation matrix
        corr_matrix = data_df.corr().abs()
        G = nx.from_pandas_adjacency(corr_matrix)
        
        # Calculate centrality measures
        centrality = nx.degree_centrality(G)
        clustering = nx.clustering(G)
        
        # Find most central nodes
        most_central = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'centrality': dict(list(centrality.items())[:10]),  # First 10 for brevity
            'clustering': dict(list(clustering.items())[:10]),
            'connected_components': nx.number_connected_components(G),
            'density': nx.density(G),
            'most_central_nodes': most_central,
            'average_clustering': nx.average_clustering(G)
        }
    
    def build_feature_graph(self, data_df, threshold=0.7):
        """
        Build graph based on feature correlations.
        
        Args:
            data_df: pandas DataFrame
            threshold: Correlation threshold for edge creation
            
        Returns:
            NetworkX Graph
        """
        corr_matrix = data_df.corr().abs()
        G = nx.Graph()
        
        # Add nodes (features)
        for col in corr_matrix.columns:
            G.add_node(col)
        
        # Add edges for high correlations
        for i, col1 in enumerate(corr_matrix.columns):
            for j, col2 in enumerate(corr_matrix.columns):
                if i < j and corr_matrix.loc[col1, col2] > threshold:
                    G.add_edge(col1, col2, weight=corr_matrix.loc[col1, col2])
        
        return G
    
    def find_communities(self, graph):
        """Find communities in the graph using greedy modularity."""
        try:
            communities = nx.community.greedy_modularity_communities(graph)
            return {
                'num_communities': len(communities),
                'communities': [list(comm) for comm in communities]
            }
        except:
            return {'error': 'Could not compute communities'}

