default:
	python -m game.play

frontend:
	python -m gui.gui

stratego:
	python -m game.play

test:
	python -m pytest

trainStartState:
	python -m train.train_start

trainReachable:
	python -m train.trainerTestReachable

trainModifiedReachable:
	python -m train.trainerTestModifiedReachable

trainPieceBased:
	python -m train.trainerTestPieceBased

tournement:
	python -m train.run_tournement

clean:
	find . -name '*.pyc' -delete
