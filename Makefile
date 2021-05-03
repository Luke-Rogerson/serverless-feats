deploy:
	@cd terraform && terraform apply -var-file=vars.tfvars -auto-approve
	@tput setaf 2; echo "Deployed successfully!"

plan:
	@cd terraform && terraform plan -var-file=vars.tfvars