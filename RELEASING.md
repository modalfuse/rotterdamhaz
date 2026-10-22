# Releasing RotterdamHaz (maintainer notes)

This directory is the GitHub repository for RotterdamHaz 1.0.1: https://github.com/modalfuse/rotterdamhaz

The data files are the 1.0.1 package. `SHA256SUMS` lists those files. `LICENSE`, `CITATION.cff`, `.zenodo.json`, `.gitignore`, `.gitattributes` and this note are repository metadata and are not in `SHA256SUMS`. `README.md` is in `SHA256SUMS`.

## Version DOIs

- RotterdamHaz 1.0.0: https://doi.org/10.5281/zenodo.23568109. Tag `v1.0.0` is unchanged. The file on that Zenodo record stays the 1.0.0 archive, and the code archive inside it keeps its original filename.
- RotterdamHaz 1.0.1: the version DOI is written here after the Zenodo draft returns. Tag `v1.0.1` is created on the commit that records that DOI.

## Check

`shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS`.

## Zenodo

1.0.1 is a new version of Zenodo record 23568109. It does not replace the 1.0.0 file. After the version DOI exists, fill `CITATION.cff`, the README citation line and this note, and update the `README.md` line in `SHA256SUMS`.
