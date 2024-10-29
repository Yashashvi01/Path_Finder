import streamlit as st
from algorithms.pathfinding_algorithms import bfs_shortest_path, dijkstra_shortest_path, dfs_search, a_star_search, manhattan_distance
from utils.visualization import plot_graph
from utils.graph_utils import create_grid_graph, add_obstacles
from algorithms.rl_pathfinding import QLearningAgent

# Title for the application
st.title("Pathfinding Algorithm Visualizer")

# User-defined grid dimensions and obstacles
rows = st.slider("Grid Rows", 5, 20, 10)
cols = st.slider("Grid Columns", 5, 20, 10)
num_obstacles = st.slider("Number of Obstacles", 0, (rows * cols) // 4, (rows * cols) // 10)

# Define start and end points
start_row = st.slider("Start Node Row", 0, rows - 1, 0)
start_col = st.slider("Start Node Column", 0, cols - 1, 0)
end_row = st.slider("End Node Row", 0, rows - 1, rows - 1)
end_col = st.slider("End Node Column", 0, cols - 1, cols - 1)

start_node = (start_row, start_col)
end_node = (end_row, end_col)

# Create the graph and add obstacles
graph, node_positions = create_grid_graph(rows, cols)
graph = add_obstacles(graph, node_positions, num_obstacles, start_node, end_node)

# Algorithm selection
algorithm = st.selectbox("Choose an algorithm", ("BFS", "Dijkstra", "DFS", "A*", "Q-Learning AI"))
episodes = 0
save_interval = 0
if algorithm == "Q-Learning AI":
    episodes = st.slider("Training Episodes", min_value=100, max_value=1000, step=100)
    save_interval = st.slider("Save Interval", min_value=10, max_value=100, step=10)

if st.button("Run Algorithm"):
    path, explore_order = None, []

    if algorithm == "Q-Learning AI":
        with st.spinner("Training AI..."):
            st.subheader("The AI model is trying to improve the path's distance after each iteration...")
            agent = QLearningAgent(graph, start_node, end_node)
            all_paths, final_path = agent.train(episodes=episodes, save_interval=save_interval)
            
            # Display progress by visualizing saved paths
            for idx, path in enumerate(all_paths):
                st.write(f"Episode {idx * save_interval} Path:", " -> ".join(str(node) for node in path))
                plot_graph(graph, node_positions, path, start_node, end_node, explore_order=path)
            
            # Capture the entire explore order for final animation
            explore_order = final_path
            st.subheader("Final AI-optimized Path:")
            st.write("Final AI-optimized Path:", " -> ".join(str(node) for node in final_path))
            with st.spinner("Generating Plot ..."):
                plot_graph(graph, node_positions, final_path, start_node, end_node, explore_order=final_path, animate=True, save_path="exploration_ai.gif")
                st.image("exploration_ai.gif", caption="Final AI Pathfinding Animation")
    elif algorithm == "BFS":
        path, explore_order = bfs_shortest_path(graph, start_node, end_node)
    elif algorithm == "Dijkstra":
        path, explore_order = dijkstra_shortest_path(graph, start_node, end_node)
    elif algorithm == "DFS":
        path, explore_order = dfs_search(graph, start_node, end_node)
    elif algorithm == "A*":
        path, explore_order = a_star_search(graph, start_node, end_node, heuristic=manhattan_distance)

    # Save and display animated exploration GIF for other algorithms
    if algorithm != "Q-Learning AI":
        # Display path results
        if path:
            st.subheader("Path Found")
            st.write("Path found:", " -> ".join(str(node) for node in path))
        else:
            st.write("No path found!")
        with st.spinner("Generating Plot ..."):
            gif_path = "exploration.gif"
            plot_graph(graph, node_positions, path, start_node, end_node, explore_order, animate=True, save_path=gif_path)
            st.image(gif_path, caption="Algorithm Exploration and Shortest Path")