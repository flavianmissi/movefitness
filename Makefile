test: clean
	./manage.py test --settings=move_fitness.settings_test

clean:
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@echo "Done!"
