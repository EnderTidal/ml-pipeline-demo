#!/usr/bin/env python
import wandb

# Initialize W&B
api = wandb.Api()

# Get the random_forest_export artifact
artifact = api.artifact('jtibb15-western-governors-university/nyc_airbnb/random_forest_export:latest')

# Add the prod alias
artifact.aliases.append('prod')
artifact.save()

print(f"Successfully tagged {artifact.name} as 'prod'")
print(f"Aliases: {artifact.aliases}")
