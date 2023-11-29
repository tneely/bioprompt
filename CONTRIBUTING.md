# Contributing to bioprompt

Here's what you'll need to contribute.

### Tooling

something about rtx / toolversions

### Testing

Tests can be run via

```bash
pdm run test
```

### Code style

This repository uses [pre-commit](https://github.com/pre-commit/pre-commit) for linting. 
Install `pre-commit` first, for example with pip or [pipx](https://github.com/pypa/pipx):

```bash
python -m pip install pre-commit
```

```bash
pipx install pre-commit
```

Then initialize `pre-commit`:

```bash
pre-commit install
```

You can now lint the code with:

```bash
pdm run lint
```

Failure to properly fix linting errors will cause the CI will fail and 
your Pull Request will not be merged.