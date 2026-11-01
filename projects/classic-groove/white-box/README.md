# Classic Groove white-box tests

One Jest suite for the JavaScript application controllers, using jsdom, jQuery and Sinon. The formerly identical application-side and separate copies are consolidated here.

```bash
npm ci
npm test -- --runInBand
```

Run these commands from this directory. Test imports resolve through `../../application/controllers/` from `tests/`, so the suite does not require the old absolute XAMPP controller location. Some tests contain their own historical mocks and function implementations.

[Classic Groove project](../README.md)

## Known historical fixture failures

The original and consolidated suites both produce 58 passed and 3 failed tests out of 61. The failures concern the empty-song-name fixture selector and two registration cases with a missing required name. The same failures were reproduced from the original tests and controllers with only the machine-specific import path adapted. They remain visible for later test-fixture work.
