# SGU - 841408 - Software Testing

Coursework and testing projects for the Software Testing course at Saigon University, including manual reports, Selenium automation, unit tests, and OpenCart and Classic Groove applications.

## Repository contents

| Directory | Materials |
| --- | --- |
| [assignments/](assignments/README.md) | Final Assignment 1 and 2 reports, team spreadsheets, and one consolidated Assignment 2 source suite |
| [projects/](projects/README.md) | OpenCart black-box/white-box tests and browser prototypes; Classic Groove application, Selenium and Jest suites |
| [practice/](practice/README.md) | Weekly Python/Java exercises and Selenium examples organized by website |
| [references/](references/README.md) | Independent OpenCart examples and documents, plus reference work from other groups |
| [tools/](tools/README.md) | One archived ChromeDriver distribution, Selenium Java 4.27.0, and shared HTML-report styling |
| [recovery/](recovery/private-backup/README.md) | Complete encrypted backup of the original Git histories and pre-publication private files |

```text
assignments/
  assignment-01-manual-testing/{reports,team-members}/
  assignment-02-selenium/{reports,source}/
projects/
  opencart/{black-box,white-box,selenium-prototype,documents,presentation-drafts}/
  classic-groove/{application,black-box,white-box}/
practice/
  weekly/{week-03,week-04}/
  selenium/{learning,saucedemo,tree-shop,tic-tac-toe}/
references/
tools/
```

## Finding the coursework

[Assignment 1](assignments/assignment-01-manual-testing/README.md) contains the final manual OpenCart report in editable Word and submitted PDF formats, plus Nguyen Long Vu's distinct bug and test-execution spreadsheets.

[Assignment 2](assignments/assignment-02-selenium/README.md) contains the final Word/PDF report, one combined Selenium/HTTP test suite, and three distinct historical HTML results. The combined source retains the product-options checkout scenario from the older copy and the expanded guest-checkout cases.

The [OpenCart black-box suite](projects/opencart/black-box/README.md) combines shared cases with wishlist, guest checkout, navigation, product-review and contact-validation checks. The [Classic Groove project](projects/classic-groove/README.md) separates the PHP application, Selenium black-box tests and one Jest white-box suite.

## Running and interpreting results

Read each suite's README and dependency manifests before execution. The personal Selenium suites require Python 3.12 or newer; many expect OpenCart at `http://localhost/demo/` or Classic Groove installed in XAMPP. Historical account data, fixed delays and some machine-specific paths remain in the coursework source and require local setup.

The [environment template](.env.example) names the variables used by the SGU login exercise and OpenCart public-demo scripts. Export these variables in your shell; the template is not loaded automatically. Local test accounts inside reports and localhost test cases are historical test data.

Saved HTML reports, screenshots and document results describe their original runs. They are retained when they represent different runs. Browser, payment, account and database workflows are not exercised as part of repository cleanup.

## Consolidation and naming

Accidental source copies and superseded drafts have been removed. Python modules use `snake_case`; descriptive document and directory names use `kebab-case`. Final Word/PDF pairs remain because they serve editing and layout-preserving use. Independent examples, dependency manifests, licenses and application images used in separate editable storage locations remain in their own context.

The [cleanup record](.organization/cleanup-manifest.json) records the consolidations and renames from the initial import. The [source provenance index](.organization/source-provenance.json) records upstream repositories and current locations. The [initial organization record](.organization/move-manifest.json) is a historical checkpoint; its paths precede this cleanup.

Installed dependencies, environments, browser profiles, caches, IDE state, private configuration and OS metadata are excluded. The original Git metadata and pre-publication private files are preserved in the [encrypted recovery archive](recovery/private-backup/README.md). At the owner's request, its recovery key is included in the repository; anyone with repository access can restore the complete archive, including original saved passwords and account data. Local environment residues remain in excluded `.local-backups/`. Previous published source copies can also be recovered from Git history.

## Material provenance

Original authorship, copyright notices and licenses for third-party code, fonts, media and reference materials remain with their owners. This collection does not grant a separate license for those materials. Submitted documents retain their original author and group information.

Maintainer: **La Hieu Phong** (`lahieuphong`).
