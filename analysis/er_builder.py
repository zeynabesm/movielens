import pandas as pd
import networkx as nx
from pathlib import Path
DATA_PATH = Path("../Data")
movies = pd.read_csv(DATA_PATH / "movies.csv")
ratings = pd.read_csv(DATA_PATH / "ratings.csv")
tags = pd.read_csv(DATA_PATH / "tags.csv")
links = pd.read_csv(DATA_PATH / "links.csv")
