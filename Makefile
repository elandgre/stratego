default:
		python -m game.play

stratego:
		python -m game.play

test:
		python -m pytest

clean:
		find . -name '*.pyc' -delete
