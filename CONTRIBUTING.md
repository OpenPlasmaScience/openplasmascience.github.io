[`Node.js`](https://nodejs.org/en/download)

# Contributing to the Guide

> [!NOTE]
> This page is in the process of being written, and will largely be 
> adapted from [PlasmaPy's Contributor Guide]. 

## Submitting a pull request

A contribution to this guide can be made via a pull request to the
repository's `main` branch.

## Building the site locally

> [!NOTE]
> It may be necessary to install a recent version of [`Node.js`].

After cloning the repository, go to the top-level directory and run

```bash
python noxfile.py -s build
```

The build will be located at `_build/html/index.html`.

[PlasmaPy's Contributor Guide]: https://docs.plasmapy.org/en/latest/contributing