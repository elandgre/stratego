default:
	python -m game.play

frontend:
	python -m gui.gui

stratego:
	python -m game.play

test:
	python -m pytest

clean:
	find . -name '*.pyc' -delete
