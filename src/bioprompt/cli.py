import typer

from bioprompt.ai import bp


def main(prompt: str) -> None:
    print(bp(prompt))


if __name__ == "__main__":
    typer.run(main)
