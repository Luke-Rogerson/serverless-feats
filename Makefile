deploy:
	@rm lambda.zip || true
	@pip install -r ./app/lambda/requirements.txt -t ./app/lambda/deps
	@cd ./app/lambda/deps && zip -r ../../../lambda.zip .
	@cd ./app/lambda && zip -g ../../lambda.zip main.py lib
	@cd terraform && terraform apply -var-file=vars.tfvars -auto-approve
	@tput setaf 2; echo "Deployed successfully!"
