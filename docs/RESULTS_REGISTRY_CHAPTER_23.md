# سجل نتائج الفصل الثالث والعشرين

```text
CHAPTER                = 23
VERSION                = 0.27.0-dev
REGISTRY               = AUTHORED-DRAFT
RESULTS                = 10 AUTHORED-DRAFT / NON-CITABLE
PASS-FOR-AUTHORING     = YES
AUTHORING               = COMPLETED
LOCAL-BUILD             = PENDING
POST-AUTHORING-REVIEW   = PENDING
OWNER-ADOPTION          = NOT REQUESTED
MERGE                  = NOT AUTHORIZED
```

| المعرّف | الوصف | التصنيف المجمد | الحالة |
|---|---|---|---|
| ANT-DEF-23-01 | دالة عد الأصفار والتطبيع المحلي، مع إحالة إلى `ANT-THM-06-06` | DEFINITION / INTERNAL-CROSS-REFERENCE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-DEF-23-02 | إحصاء الارتباط الثنائي ودالة Montgomery الموزونة | DEFINITION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-23-01 | مبرهنة Montgomery ضمن دعم \((-1,1)\) | CITED-CORE / CONDITIONAL-ON-RH | AUTHORED-DRAFT / NON-CITABLE |
| ANT-CONJ-23-01 | حدسية الارتباط الثنائي الكاملة | CONJECTURAL-GUE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-23-02 | حد GUE ونواة الجيب في النموذج المصفوفي | RANDOM-MATRIX-THEOREM / CITED-CORE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-EVID-23-01 | دليل Odlyzko العددي | NUMERICAL-EVIDENCE / FINITE-VERIFIED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-DEF-23-03 | إحصاء الفواصل والتباين العددي | DEFINITION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PRIN-23-01 | مبدأ أنواع التناظر لعائلات دوال L | CITED-CORE / INTERPRETATION-GUARDED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-OPEN-23-01 | حدسية GUE الكاملة وإحصاءات n-level | OPEN / FRONTIER | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PRIN-23-02 | حدود الاستدلال بين RH وpair correlation والإحصاءات الأعلى | METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED | AUTHORED-DRAFT / NON-CITABLE |

## حكم بوابة التأليف

```text
PRIMARY-INDEPENDENT-REVIEW = CHANGES-REQUIRED / 0 BLOCKERS
FIRST-NARROW-RE-REVIEW     = CHANGES-REQUIRED / 0 BLOCKERS
SECOND-NARROW-RE-REVIEW    = PASS / 0 BLOCKERS
REVIEWED-HEAD              = f1c39285af56b0677864454c84adf0f9fe22b73c
REVIEW-COMMIT              = 66927de635532a0ef4e82087e4a528abc57b5ebe
PASS-FOR-AUTHORING         = YES
```

## حراس ما بعد التأليف

- لا يصبح أي معرّف `ACTIVE / CITABLE` قبل البناء الكامل والمراجعة المستقلة بعد التأليف واعتماد المالك.
- صيغة ريمان--فون مانغولت لا تحصل على معرّف فصل 23 جديد؛ مصدرها الداخلي `ANT-THM-06-06`.
- `ANT-THM-23-01` يحمل RH في نصه ويقيد دعم \(\widehat f\) داخل \((-1,1)\).
- `ANT-THM-23-02` مبرهنة في نموذج المصفوفات العشوائية لا في دالة زيتا.
- `ANT-EVID-23-01` لا يرقى إلى مبرهنة.
- `ANT-CONJ-23-01` و`ANT-OPEN-23-01` لا يوصفان بأنهما مثبتان.
- `ANT-PRIN-23-02` مبدأ منهجي ولا يحمل تصنيف `PROVED-HERE`.
- يوضع الفصل 23 قبل خريطة الجبهات، وتبقى الخريطة آخر فصل.
- `MERGE = NOT AUTHORIZED` حتى اعتماد المالك الصريح.