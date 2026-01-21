from pathlib import Path

from practice.labyrinth.repository.text_file import TextFileRepo
from practice.train.domain.train import Route


def main():
    pass

if __name__ == "__main__":
    path = Path(__file__).with_name("routes.txt")
    repo = TextFileRepo(str(path))
    route = Route(repo)

    print(route)