# Classic Groove testing project

| Directory | Purpose |
| --- | --- |
| [application/](application/README.md) | Original PHP vinyl-store application, SQL data, controllers and assets |
| [black-box/](black-box/README.md) | One combined Selenium/Pytest suite, including admin order search |
| [white-box/](white-box/README.md) | One Jest suite targeting the application controllers with relative paths |

The duplicate application-side Jest copy and repeated black-box tree have been removed. The application keeps independent album-image and slideshow storage directories because administration operations write them separately.

A [2023 report from another group](../../references/classic-groove/group-03-testing-report-2023.pdf) is retained as reference material.

[Projects](../README.md)
