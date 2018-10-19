default:
		python game/play.py	

stratego:
		python game/play.py	

test:
		python -m pytest

clean:
		find . -name '*.pyc' -delete 
