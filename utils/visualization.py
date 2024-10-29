import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def plot_graph(graph, node_positions, path=None, start=None, end=None, explore_order=None, animate=False, save_path="exploration.gif"):
    G = nx.Graph(graph)
    fig, ax = plt.subplots(figsize=(8, 8))
    
    pos = node_positions
    nx.draw(G, pos, node_color="lightblue", with_labels=True, node_size=300, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color="green", label="Start", ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=[end], node_color="red", label="End", ax=ax)

    # Default to empty lists if None
    path = path or []
    explore_order = explore_order or []

    if animate:
        def update(num):
            ax.clear()
            nx.draw(G, pos, node_color="lightblue", node_size=300, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color="green", label="Start", ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=[end], node_color="red", label="End", ax=ax)

            if num < len(explore_order):
                current_explored = explore_order[:num + 1]
                nx.draw_networkx_nodes(G, pos, nodelist=current_explored, node_color="blue", ax=ax)

            if path and num >= len(explore_order):
                edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
                nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="orange", width=6, ax=ax)
            return ax

        total_frames = len(explore_order) + len(path)
        ani = FuncAnimation(fig, update, frames=total_frames, repeat=False)
        ani.save(save_path, writer=PillowWriter(fps=5))
    else:
        if path:
            edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="orange", width=6, ax=ax)
        else:
            ax.set_title("No path found!")

    plt.close(fig)
