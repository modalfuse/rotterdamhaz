# Releasing RotterdamHaz (maintainer notes)

This directory is the GitHub repository for RotterdamHaz 1.0.0: https://github.com/modalfuse/rotterdamhaz

The data files are the 1.0.0 package. `SHA256SUMS` lists those files. `LICENSE`, `CITATION.cff`, `.zenodo.json`, `.gitignore`, `.gitattributes` and this note are repository metadata and are not in `SHA256SUMS`. `README.md` is in `SHA256SUMS`; its repository URL line is included in that checksum.

## Still assigned at publication
- Dataset DOI: Zenodo mints it when the record is published. `CITATION.cff` has no `doi` yet. README citation says `DOI: TBD`. `.zenodo.json` `publication_date` stays `TBD`.
- arXiv identifier: not assigned. The arXiv package is not in this repository.
- Do not add either value until the corresponding service has issued it.

## Check
`shasum -a 256 -c SHA256SUMS` (macOS) or `sha256sum -c SHA256SUMS`.

## Zenodo
Enable the repository in Zenodo's GitHub integration, then publish a GitHub release with tag `v1.0.0`. Zenodo reads `.zenodo.json`. After the DOI exists, fill `CITATION.cff`, the README citation line, and `.zenodo.json`, and update the `README.md` line in `SHA256SUMS`.
