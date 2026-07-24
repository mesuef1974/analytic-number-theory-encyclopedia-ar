# Chapter 17 post-integration build receipt

Date: 2026-07-25

Branch:

`agent/chapter-17-circle-method-goldbach-waring-v0.21.0`

Verified after integrating the former audit-03 and audit-04 material into the main chapter text and removing the standalone audit files.

```text
PDF-BUILD            = PASS
PAGES                = 237
PDF-SHA256           = 1D0EA5E9E98526E6330961AB52D3D83E538D57716F9B0DE811C0A1712020A520
UNDEFINED-CITATIONS  = 0
UNDEFINED-REFERENCES = 0
LATEX-FATAL-ERRORS   = 0
```

Generated outputs:

- `build/main.pdf`
- `releases/preview.pdf`

The following stale chapter-text markers were absent from the integrated chapter:

- `ANT-PROP-01-17`
- the standalone section title `تدقيق عامل القياس والكثافات المحلية`
- the standalone section title `تدقيق الاصطلاحات وحدود الادعاء`

The global macro `\draftresult` remains defined in `manuscript/preamble.tex` for use elsewhere in the encyclopedia; its presence is not evidence that Chapter 17 still uses the draft badge.

Remaining gate:

```text
VISUAL-RECHECK    = PENDING
OWNER-ADOPTION    = NOT YET
MERGE             = NOT AUTHORIZED
RELEASE-READY     = NO
```