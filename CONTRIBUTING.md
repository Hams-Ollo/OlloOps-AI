# Contributing to hams_ollo & AI

## 🌟 Welcome

Thank you for considering contributing to hams_ollo AI! This guide will help you understand our development process and how to contribute effectively.

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Branch Structure](#branch-structure)
3. [Development Workflow](#development-workflow)
4. [Getting Started](#getting-started)
5. [Making Changes](#making-changes)
6. [Pull Request Process](#pull-request-process)
7. [Coding Standards](#coding-standards)

## 📜 Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## 🌳 Branch Structure

```curl
main
  └── develop
       ├── feature/your-feature
       ├── bugfix/issue-description
       └── enhancement/feature-improvement
```

- `main`: Production-ready code
- `develop`: Main development branch
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `enhancement/*`: Improvements to existing features

## 🔄 Development Workflow

1. **Fork & Clone**

```bash
# Fork via GitHub UI, then:
git clone https://github.com/YOUR_USERNAME/hams_ollo-AI.git
cd hams_ollo-AI
```

2. **Set Up Remote**

```bash
git remote add upstream https://github.com/Hams-Ollo/hams_ollo_ai.git
```

3. **Create Feature Branch**

```bash
# First, ensure you're on develop
git checkout develop
git pull upstream develop

# Create your feature branch
git checkout -b feature/your-feature-name
```

4. **Work on Your Feature**

```bash
# Make changes, then commit
git add .
git commit -m "feat: description of your changes"
```

5. **Keep Your Branch Updated**

```bash
git checkout develop
git pull upstream develop
git checkout feature/your-feature-name
git rebase develop
```

6. **Push Changes**

```bash
git push origin feature/your-feature-name
```

## 🚀 Getting Started

1. **Environment Setup**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Unix/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

2. **Configure Environment**

- Add required API keys to `.env`
- Set up development tools

## ✏️ Making Changes

1. **Create a New Branch**

```bash
# For new features
git checkout -b feature/your-feature-name develop

# For bug fixes
git checkout -b bugfix/issue-description develop

# For enhancements
git checkout -b enhancement/feature-improvement develop
```

2. **Commit Guidelines**

```curl
type: subject

body

footer
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Example:

```bash
git commit -m "feat: add voice synthesis capability

Implemented ElevenLabs API integration for natural voice synthesis.
Includes voice profile management and streaming support.

Closes #123"
```

## 🔍 Pull Request Process

1. **Before Submitting**
   - Update your branch with latest develop
   - Run all tests
   - Update documentation
   - Check coding standards

2. **Submitting PR**
   - Create PR to `develop` branch
   - Fill out PR template
   - Request reviews
   - Address feedback

3. **PR Template**

```markdown
## Description
[Describe your changes]

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Enhancement
- [ ] Documentation

## Testing
- [ ] Tests added
- [ ] Existing tests pass

## Screenshots
[If applicable]

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Branch up-to-date with develop
```

## 📝 Coding Standards

1. **Python Style**
   - Follow PEP 8
   - Use type hints
   - Document functions/classes

2. **Documentation**
   - Update README.md if needed
   - Add docstrings
   - Update ROADMAP.md for features

3. **Testing**
   - Write unit tests
   - Ensure all tests pass
   - Add integration tests for new features

## 🔄 Regular Workflow Example

```bash
# Start new feature
git checkout develop
git pull upstream develop
git checkout -b feature/new-capability

# Make changes
# ... work on code ...

# Commit changes
git add .
git commit -m "feat: add new capability

Detailed description of changes"

# Update with develop
git checkout develop
git pull upstream develop
git checkout feature/new-capability
git rebase develop

# Push and create PR
git push origin feature/new-capability
# Create PR via GitHub UI
```

## 🤝 Getting Help

- Create an issue for bugs
- Join discussions in existing issues
- Check project documentation
- Contact maintainers

## 📅 Release Process

1. **Prepare Release**
   - Merge feature branches to develop
   - Update version numbers
   - Update CHANGELOG.md

2. **Create Release PR**
   - develop → main
   - Include release notes
   - Get approvals

3. **After Release**
   - Tag release
   - Update documentation
   - Clean up branches

Remember: All changes must go through develop first, then to main via pull request.
