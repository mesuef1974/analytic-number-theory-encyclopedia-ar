# طلب مراجعة مستقلة بعد تأليف الفصل الثالث والعشرين

```text
CHAPTER                = 23
VERSION                = 0.27.0-dev
BRANCH                 = agent/chapter-23-zero-statistics-random-matrices-v0.27.0
TARGET-HEAD            = 5ccd956258c6f790d0e3a6190de504beab9849bf
REVIEW-STAGE           = POST-AUTHORING
LOCAL-BUILD            = PASS / 302 PAGES
RESULTS                = 10 AUTHORED-DRAFT / NON-CITABLE
OWNER-ADOPTION         = NOT REQUESTED
MERGE                  = NOT AUTHORIZED
```

## الملفات الواجب قراءتها كاملة

1. `volumes/volume-15-modern-frontiers/chapters/chapter-23-zero-statistics-random-matrices.tex`
2. `manuscript/chapter-23-bibliography.bib`
3. `docs/CHAPTER_23_SCOPE_2026-07-26.md`
4. `docs/CHAPTER_23_EVIDENCE_LEDGER_2026-07-26.md`
5. `docs/CHAPTER_23_NORMALIZATION_TABLE_2026-07-26.md`
6. `docs/CHAPTER_23_PROOF_MAP_2026-07-26.md`
7. `docs/RESULTS_REGISTRY_CHAPTER_23.md`
8. `docs/CHAPTER_23_LOCAL_BUILD_RECEIPT_2026-07-26.md`
9. المراجعات المستقلة السابقة الخاصة ببوابة ما قبل التأليف.
10. `manuscript/main.tex` و`manuscript/preamble.tex` للتحقق من الربط والترتيب وعدم كسر أوامر الحوكمة.

## نطاق المراجعة العلمية

تحقق مستقلًا من:

- أن `ANT-DEF-23-01` لا يعيد ادعاء صيغة ريمان--فون مانغولت كمبرهنة جديدة، وأن الإحالة إلى `ANT-THM-06-06` واضحة.
- صحة اشتقاق الكثافة المتوسطة ومتوسط التباعد والتطبيع المحلي.
- تعريف دالة Montgomery الموزونة: الوزن، التطبيع، الأزواج المرتبة، القطر، وشرط RH.
- دقة صيغة مبرهنة Montgomery ومجال `0 <= alpha < 1` وقيد دعم فورييه `(-1,1)`.
- الفصل الصريح بين الجزء المثبت وحدسية الارتباط الثنائي الكاملة.
- اتفاقية فورييه وهوية تحويل مربع نواة الجيب.
- أن مبرهنة GUE مصنفة مبرهنة مصفوفية لا نتيجة عن أصفار زيتا.
- دقة أرقام Odlyzko وتصنيفها `NUMERICAL-EVIDENCE / FINITE-VERIFIED`.
- التمييز بين pair correlation وnearest-neighbor spacing وnumber variance وn-level statistics.
- حارس Katz--Sarnak وبيانات Rudnick--Sarnak.
- أن `ANT-PRIN-23-02` مبدأ منهجي لا `PROVED-HERE`.
- بقاء RH وGUE الكاملة وإحصاءات المستويات الأعلى خارج ادعاءات الإثبات.

## نطاق المراجعة التحريرية والبنائية

- تحقق من وجود المعرفات العشرة مرة واحدة واتساقها مع السجل.
- تحقق من الاستشهادات السبعة الخاصة بالفصل ومطابقتها للمراجع.
- أعد البناء من الصفر بدورة `xelatex -> biber -> xelatex -> xelatex`.
- تحقق من أن الفصل 23 هو الفصل 23 وأن خريطة الجبهات هي الفصل 24 وآخر فصل.
- ميّز بين التحذيرات القديمة العامة والتحذيرات الجديدة الخاصة بالفصل 23.
- راجع مواضع `Overfull hbox` في الفصل 23 بصريًا، خصوصًا نص التصنيفات الطويلة.
- لا تعدل المتن أثناء المراجعة. اكتب تقريرًا مستقلًا فقط.

## المخرج المطلوب

أنشئ:

`docs/CHAPTER_23_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-26.md`

ويجب أن يحتوي على:

```text
REVIEWED-HEAD    = 5ccd956258c6f790d0e3a6190de504beab9849bf
REVIEWER         = INDEPENDENT LOCAL CLIENT
REVIEW-STAGE     = POST-AUTHORING
VERDICT          = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS         = <integer>
RESULTS-CITABLE  = YES | NO
MERGE            = NOT AUTHORIZED
PDF-PAGES        = <integer>
```

لا يصدر `RESULTS-CITABLE = YES` إلا مع `VERDICT = PASS` و`BLOCKERS = 0`. حتى عند النجاح يبقى التفعيل والدمج رهن اعتماد المالك الصريح.
