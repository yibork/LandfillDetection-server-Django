#!/bin/bash
echo "Building latest changes"
cd LandfillDetection
docker compose up -d --build

echo "Deployment complete"