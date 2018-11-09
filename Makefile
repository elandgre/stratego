default:
	python -m game.play

frontend:
	python -m gui.gui

stratego:
	python -m game.play

test:
	python -m pytest

trainStart:
	python -m ai.train_start

clean:
	find . -name '*.pyc' -delete
