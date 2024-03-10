
export_requirements:
	@echo "Exporting requirements..."
	poetry export --without-hashes -f requirements.txt --output requirements.txt
