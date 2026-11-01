# SGU - 841408 - Software Testing

Coursework and testing-project materials for the Software Testing course at Saigon University, including manual test reports, Selenium automation, unit tests, and OpenCart and Classic Groove projects.

## Repository contents

| Directory | Materials |
| --- | --- |
| [assignments/](assignments/README.md) | Assignment 1 manual testing and Assignment 2 Selenium automation: reports, drafts, team spreadsheets, and three source versions |
| [projects/](projects/README.md) | OpenCart BlackBox/WhiteBox tests, an early Selenium prototype, project documents, and Classic Groove application and test snapshots |
| [practice/](practice/README.md) | Weekly Python/Java exercises and Selenium practice for SauceDemo, Tree Shop, Tic Tac Toe, SGU, YouTube, and VnExpress |
| [references/](references/README.md) | OpenCart examples and documentation, a Classic Groove reference report, and coursework examples from other groups |
| [tools/](tools/README.md) | Selenium Java 4.27.0 JAR distribution and its accompanying dependencies and license files |

```text
sgu-841408-software-testing/
├── assignments/
│   ├── assignment-01-manual-testing/
│   └── assignment-02-selenium/
├── projects/
│   ├── opencart/
│   └── classic-groove/
├── practice/
│   ├── weekly/
│   └── selenium/
├── references/
└── tools/
```

## Assignments

[Assignment 1](assignments/assignment-01-manual-testing/README.md) contains La Hieu Phong's Word/PDF manual OpenCart report, a Vietnamese draft, and Nguyen Long Vu's test-execution and bug-report spreadsheets.

[Assignment 2](assignments/assignment-02-selenium/README.md) contains the automated-testing report and the `N9`, `N9_LaHieuPhong_Assignment2`, and `N9_LaHieuPhong_Assignment2-main` source versions. `co_Hanh_ne.docx` is Phong's editable Assignment 2 report. The source versions differ and remain separate.

## Testing projects

[OpenCart](projects/opencart/README.md) contains Selenium/Pytest BlackBox suites, PHPUnit and Selenium PHP tests, the public-demo Selenium prototype, the project scope, and a draft group presentation. `La_Hieu_Phong` adds wishlist, guest-checkout, navigation, and review tests beyond the other BlackBox snapshot.

[Classic Groove](projects/classic-groove/README.md) contains a standalone Selenium/Pytest suite and the original combined package with a PHP application, SQL data, BlackBox tests, and Jest WhiteBox tests. The source folders retain their original structure and versions.

## Working with the materials

Read the README and dependency manifests in the relevant project before running it. Many OpenCart tests expect a local installation at `http://localhost/demo/`. Classic Groove scripts and Jest tests include historical XAMPP paths. Some older scripts use fixed delays, saved session-token URLs, or absolute paths that need local configuration. The `opencart-4.0.2.3` reference folder contains documentation and database schemas; it is not a complete application installation.

Reports, HTML results, and screenshots are historical coursework evidence. Publishing this collection does not rerun the browser, database, payment, or external-account workflows. Week 6 currently contains no coursework files.

The SGU login exercise and two public-demo OpenCart scripts read account details from environment variables. See [.env.example](.env.example) for the variable names; export them in your shell before running the matching script. The example file is not loaded automatically.

## Publication and source provenance

The repository includes the organized coursework files, original source versions, documents, reports, application assets, browser-driver binaries, and Selenium Java distribution. Installed dependencies, virtual environments, browser profiles, caches, IDE state, private environment files, and operating-system metadata are excluded.

The seven original nested Git directories are preserved locally under `.local-backups/publication-2026-11-01/`, outside version control. Their working-tree contents are imported as ordinary files rather than Git submodules. The [source provenance index](.organization/source-provenance.json) records the original repository URLs and commits. Local backups also retain the original files changed to remove embedded account passwords.

The [organization map](.organization/move-manifest.json) records the original and organized paths. Its verification describes the organization checkpoint before the publication changes.

## Material provenance

The materials are collected for course study and reference. Original authorship, copyright notices, and licenses for third-party code, fonts, media, and reference materials remain with their respective owners. This repository does not grant a separate license for those materials. Coursework submissions retain their original author and group information.

Maintainer: **La Hieu Phong** (`lahieuphong`).
