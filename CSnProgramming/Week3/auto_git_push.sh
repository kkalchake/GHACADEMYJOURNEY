#!/bin/bash

# =============================================================================
# Script: Push New Folders to GitHub
# Purpose: Adds only new directories to git and pushes them to GitHub
# Usage: ./auto_git_push.sh
# =============================================================================

# Stop the script if any command fails
set -e

# -----------------------------------------------------------------------------
# Step 1: Check if we're inside a git repository
# -----------------------------------------------------------------------------
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: You're not in a git repository"
    echo "Please run this script from inside your project folder"
    exit 1
fi

# -----------------------------------------------------------------------------
# Step 2: Find all new (untracked) directories
# -----------------------------------------------------------------------------
echo "Looking for new folders..."

# Get list of untracked files and filter only directories
# - 'git ls-files --others --exclude-standard' lists untracked files
# - We extract the directory path and remove duplicates with 'sort -u'
NEW_FOLDERS=$(git ls-files --others --exclude-standard | 
              grep -E '.+/.+' | 
              sed 's|/[^/]*$||' | 
              sort -u)

# -----------------------------------------------------------------------------
# Step 3: Check if there are any new folders
# -----------------------------------------------------------------------------
if [ -z "$NEW_FOLDERS" ]; then
    echo "✓ No new folders found"
    echo "All folders are already tracked by git"
    exit 0
fi

# -----------------------------------------------------------------------------
# Step 4: Show the user which folders will be added
# -----------------------------------------------------------------------------
echo "Found these new folders:"
echo "$NEW_FOLDERS" | while read folder; do
    echo "  - $folder"
done
echo ""

# -----------------------------------------------------------------------------
# Step 5: Ask for confirmation before proceeding
# -----------------------------------------------------------------------------
read -p "Do you want to add these folders? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "Cancelled by user"
    exit 0
fi

# -----------------------------------------------------------------------------
# Step 6: Add each new folder to git
# -----------------------------------------------------------------------------
echo ""
echo "Adding folders to git..."

echo "$NEW_FOLDERS" | while read folder; do
    # Add the folder and all its contents
    git add "$folder/"
    echo "  ✓ Added: $folder"
done

# -----------------------------------------------------------------------------
# Step 7: Check if there's anything to commit
# -----------------------------------------------------------------------------
if git diff --staged --quiet; then
    echo "No changes to commit (folders might be empty)"
    exit 0
fi

# -----------------------------------------------------------------------------
# Step 8: Commit the changes with default message
# -----------------------------------------------------------------------------
COMMIT_MESSAGE="add new directory"

echo ""
echo "Committing changes..."
git commit -m "$COMMIT_MESSAGE"

# -----------------------------------------------------------------------------
# Step 9: Push to GitHub
# -----------------------------------------------------------------------------
echo ""
echo "Pushing to GitHub..."

# Get the current branch name
CURRENT_BRANCH=$(git branch --show-current)

# Push to the remote repository
git push origin "$CURRENT_BRANCH"

# -----------------------------------------------------------------------------
# Success!
# -----------------------------------------------------------------------------
echo ""
echo "Success! New folders have been pushed to GitHub"
echo "Branch: $CURRENT_BRANCH"
echo "Commit message: $COMMIT_MESSAGE"