#!/usr/bin/env python
import wandb

# Initialize W&B
api = wandb.Api()

# Get the artifact
artifact = api.artifact('jtibb15-western-governors-university/nyc_airbnb/clean_sample.csv:latest')

# Add the reference alias
artifact.aliases.append('reference')
artifact.save()

print("Successfully added 'reference' alias to clean_sample.csv:latest")
