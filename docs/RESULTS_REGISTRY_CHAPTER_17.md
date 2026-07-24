# سجل نتائج الفصل السابع عشر

آخر تحديث: 2026-07-25

```text
CHAPTER               = 17
VERSION               = 0.21.0-dev
STATUS                = PRE-AUTHORING / NON-CITABLE
PRE-AUTHORING-GATE    = OPEN
PASS-FOR-AUTHORING    = NO
RESULTS               = 7 / PROVISIONALLY RESERVED
RELEASE-READY         = NO
```

| المعرّف | النوع | الوصف | التصنيف | الحالة |
|---|---|---|---|---|
| `ANT-ID-17-01` | هوية | تعامد الدوال الأسية على الدائرة | `IDENTITY / PROVED-HERE` | `RESERVED / NON-CITABLE` |
| `ANT-ID-17-02` | هوية | تمثيل عدد الحلول الموزون بتكامل فورييه | `IDENTITY / PROVED-HERE` | `RESERVED / NON-CITABLE` |
| `ANT-DEF-17-01` | تعريف | الأقواس الكبرى والأقواس الصغرى | `PROVED-HERE` | `RESERVED / NON-CITABLE` |
| `ANT-PROP-17-01` | قضية | بنية مساهمة الأقواس الكبرى عبر السلسلة والتكامل المفردين في النموذج المختار | `PROVED-HERE / CITED INPUTS` | `RESERVED / NON-CITABLE` |
| `ANT-THM-17-01` | مبرهنة | نتيجة كلاسيكية مختارة في مسألة وارينغ | `CITED` أو `MIXED` بعد تثبيت النطاق | `RESERVED / NON-CITABLE` |
| `ANT-THM-17-02` | مبرهنة | مبرهنة فينوغرادوف للثلاثة أوليات | `CITED` | `RESERVED / NON-CITABLE` |
| `ANT-CONJ-17-01` | حدس | صيغة هاردي–ليتلوود لمسألة غولدباخ الثنائية | `HYPOTHESIS / OPEN` | `RESERVED / NON-CITABLE` |

## قواعد الحجز

- الحجز يمنع تعارض المعرّفات فقط، ولا يمنح أي نتيجة حالة علمية فعالة.
- لا تنتقل نتيجة إلى `DRAFT` قبل إغلاق بوابة ما قبل التأليف.
- لا تتحول نتيجة مقتبسة إلى `PROVED-HERE` إلا ببرهان كامل مدقق داخل الفصل.
- أي فحص عددي لاحق يصنف `FINITE-VERIFIED` ولا يرقى إلى برهان.
- `ANT-CONJ-17-01` يبقى `OPEN` ولا يجوز عرضه بوصفه نتيجة مثبتة.

## العوائق قبل التفعيل

1. تجميد مبرهنة وارينغ المستهدفة.
2. تثبيت تقديرات الأقواس الصغرى ومصادرها.
3. حسم نطاق مبرهنة فينوغرادوف مقابل نتيجة هلفغوت.
4. توحيد التطبيع والرموز.

```text
RESULT-ID-COLLISION   = NONE DETECTED
ACTIVATION            = BLOCKED
AUTHORING             = BLOCKED
```