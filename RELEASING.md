# Releasing RotterdamHaz (maintainer notes)

This directory is the GitHub repository for RotterdamHaz 1.1.0: https://github.com/modalfuse/rotterdamhaz

The data files are the 1.1.0 package. `SHA256SUMS` lists those files. `LICENSE`, `CITATION.cff`, `.zenodo.json`, `.gitignore`, `.gitattributes` and this note are repository metadata and are not in `SHA256SUMS`. `README.md` is in `SHA256SUMS`.

## Version DOIs

- RotterdamHaz 1.0.0: https://doi.org/10.5281/zenodo.23568109. Tag `v1.0.0` is unchanged. The file on that Zenodo record stays the 1.0.0 archive, and the code archive inside it keeps its original filename.
- RotterdamHaz 1.0.1: https://doi.org/10.5281/zenodo.23579821. Tag `v1.0.1` is unchanged. The file on that Zenodo record stays the 1.0.1 archive.
- RotterdamHaz 1.1.0: https://doi.org/10.5281/zenodo.23582773. Tag `v1.1.0` is the commit that records this DOI. The draft is record 23582773 and is not published.

## Check

`shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS`.

## Zenodo

1.1.0 is a new version of Zenodo record 23579821. It does not replace the 1.0.1 file. The version DOI is https://doi.org/10.5281/zenodo.23582773. The draft is not published.
