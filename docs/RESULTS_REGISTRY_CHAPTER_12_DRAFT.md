# سجل نتائج الفصل الثاني عشر المحجوزة

## حالة السجل

```text
CHAPTER          = 12 — مبرهنة Siegel--Walfisz
VERSION          = 0.16.0-dev
BRANCH           = agent/chapter-12-siegel-walfisz-v0.16.0
PRE-AUTHORING    = CLOSED / PASS
AUTHORING        = NOT YET STARTED
REGISTRY-STATUS  = DRAFT / NON-CITABLE
```

هذا سجل حجز مؤقت للمعرفات قبل كتابة المتن. لا تسمح أي حالة هنا بالاستشهاد الخارجي، ولا تعني أن البرهان كتب أو دقق أو بني داخل PDF.

| المعرّف | النتيجة المخططة | الملف المخطط | الحالة | المنشأ المتوقع |
|---|---|---|---|---|
| `ANT-LEM-12-01` | رد \(\psi(x,\chi)\) للشخصية المستحثة إلى جدها البدائي مع خطأ العوامل المحلية | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-PROVED-HERE` |
| `ANT-THM-12-01` | مبرهنة الأعداد الأولية بحد de la Vallée Poussin الفعال للشخصية الرئيسية | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-CITED` |
| `ANT-THM-12-02` | صيغة صريحة مقطوعة موحدة لـ\(\psi(x,\chi)\) للشخصيات البدائية | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-CITED` |
| `ANT-LEM-12-02` | ضبط مساهمة الأصفار غير الاستثنائية باختيار \(T=e^{\kappa\sqrt{\log x}}\) | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-PROVED-HERE` |
| `ANT-LEM-12-03` | امتصاص حد الصفر الاستثنائي باستعمال مبرهنة Siegel في المجال اللوغاريتمي | الفصل 12 | `DRAFT / NON-CITABLE / INEFFECTIVE` | `EXPECTED-PROVED-HERE` |
| `ANT-THM-12-03` | مبرهنة Siegel--Walfisz بصيغة \(\psi(x;q,a)\) | الفصل 12 | `DRAFT / NON-CITABLE / INEFFECTIVE-CONSTANT` | `EXPECTED-PROVED-HERE` |
| `ANT-COR-12-01` | صيغة الادخار اللوغاريتمي الاعتباطي | الفصل 12 | `DRAFT / NON-CITABLE / INEFFECTIVE-CONSTANT` | `EXPECTED-PROVED-HERE` |
| `ANT-COR-12-02` | الصيغة الموحدة لـ\(\vartheta(x;q,a)\) | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-PROVED-HERE` |
| `ANT-COR-12-03` | الصيغة الموحدة لـ\(\pi(x;q,a)\) | الفصل 12 | `DRAFT / NON-CITABLE` | `EXPECTED-PROVED-HERE` |

## قواعد الترقية

لا ينقل أي معرف إلى `docs/RESULTS_REGISTRY.md` بحالة قابلة للاستشهاد إلا بعد:

1. إنشاء متن الفصل وربط النتيجة بمعرفها داخله.
2. تثبيت النص النهائي للنتيجة وفروضها ومدى انتظامها.
3. إظهار منشأ كل مدخل مقتبس.
4. نجاح التدقيق المنطقي بعد التأليف.
5. نجاح فحوص الجودة وبناء PDF.
6. اجتياز تدقيق ما بعد التأليف.

## القيود الحاكمة

```text
FIXED-Q-RESULT         = SEPARATE
EXPLICIT-FORMULA       = CITED-INPUT
EXCEPTIONAL-ZERO       = MUST-BE-ISOLATED
SIEGEL-CONSTANT        = INEFFECTIVE
BOMBIERI-VINOGRADOV    = DEFERRED
GRH                    = NOT USED
```
