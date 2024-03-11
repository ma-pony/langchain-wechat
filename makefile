
export_requirements:
	@echo "Exporting requirements..."
	poetry export --without-hashes -f requirements.txt --output requirements.txt


pre-commit:
	@echo "Setting up pre-commit..."
	poetry run pre-commit install
	# poetry run pre-commit autoupdate

install_packages:
	@echo "Installing dependencies..."
	poetry lock --no-update && poetry install

cp_env:
	@echo "Setting up env config..."
	cp -n config/.env.sample config/.env

install: install_packages pre-commit cp_env
