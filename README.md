# Pathfinding Algorithm Visualizer

A web-based application to visualize and understand popular pathfinding algorithms and a Q-learning AI agent in a grid environment. Built with Streamlit and Python, this app allows users to choose grid size, obstacles, and starting and ending points, making it an interactive tool to learn about pathfinding.

## Features
- **Algorithms Supported**: Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra’s Shortest Path, A* Search with Manhattan distance heuristic, and Q-Learning AI.
- **Customizable Grid**: Choose grid size, starting and ending nodes, and obstacle placement.
- **Animated Visualization**: Watch as each algorithm explores nodes and finds the shortest path to the goal.
- **AI Training**: The Q-learning agent is trained over episodes to improve its pathfinding strategy iteratively, displaying intermediate and final paths.
- **Free Hosting**: Deployed via Streamlit and GitHub Pages.

## [Live Link](https://pathfinder-fyd49a2akrgrw6dq7nygod.streamlit.app/)

## Install Requirements:
`` bash
pip install -r requirements.txt
## Usage
Run the Streamlit app:
`` bash
streamlit run app.py
Open the local URL provided by Streamlit in your web browser.
Use the controls to:
Select the algorithm
Define grid size, start and end points, and obstacles
Choose episodes and save interval for AI training (Q-learning).
Project Structure
app.py: Main application file for Streamlit.
algorithms/: Contains individual implementations for each algorithm.
pathfinding_algorithms.py: BFS, DFS, Dijkstra, and A*.
rl_pathfinding.py: Q-Learning agent implementation.
utils/:
graph_utils.py: Functions to create grid graphs and add obstacles.
visualization.py: Visualization utilities to animate and display exploration and path.
