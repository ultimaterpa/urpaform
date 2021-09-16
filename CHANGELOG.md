# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Changelog
- FormError
- typehints for all methods
- new assigned value to `send_method` and it's named `set_value`
- new optional argument `clear_method` for EditElement and PasswordElement, possible values are
  - `clear_keys`
  - `empty_string`
  - `no_clearing`

### Changed

- outdated format methods for f-strings
- argument `walk_type` in ComboElement to `set_method` argument
- assigned value to ComboElement argument `set_method` from `text` to `send_text`
- naming of assigned values for `send_method` in EditElement and PasswordElement
  - `writing` to `send_text`
  - `pasting` to `paste`

### Fixed

- Code is formatted with [black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort)
