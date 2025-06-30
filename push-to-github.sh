#!/bin/bash
set -e

echo "Initializing git repository..."
git init

echo "Setting remote origin..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/af1nzr/Java-CICD-Full-Stack-Pipeline-Azure.git

echo "Adding all files..."
git add .

echo "Committing changes..."
git commit -m "Initial commit: Full stack Java CI/CD pipeline with Docker and Azure"

echo "Setting main branch..."
git branch -M main

echo "Pushing to GitHub..."
git push -u origin main

echo "Push complete!" 