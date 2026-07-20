# تقدم المشروع

## الحالة العامة

- **الإصدار التطويري الحالي:** `0.17.0-dev`
- **المرحلة:** الفصل الثالث عشر — مبرهنة Bombieri--Vinogradov والتوزيع المتوسطي للأعداد الأولية.
- **حالة الفصل:** `PRE-AUTHORING`
- **الفرع المستقر:** `main`
- **رأس `main` عند بدء المرحلة:** `607c6f8ad76f8085828f49ce6b566c846950ab2a`
- **فرع العمل:** `agent/chapter-13-bombieri-vinogradov-v0.17.0`
- **منهج العمل:** `EVIDENCE-FIRST / AUTHORING-BLOCKED`
- **بوابة ما قبل التأليف:** `OPEN`
- **المسار المرشح:** `VAUGHAN IDENTITY + LARGE SIEVE`
- **الهدف المركزي:** `TARGET / NOT YET ADOPTED`
- **مستوى التوزيع المستهدف:** `1/2 WITH LOGARITHMIC LOSS`
- **تدقيق الاعتمادات:** `OPEN`
- **تدقيق الخسائر اللوغاريتمية:** `OPEN`
- **تدقيق الفعالية:** `OPEN`
- **آخر تحديث:** 2026-07-21

```text
CHAPTER-13                = PRE-AUTHORING
VERSION                   = 0.17.0-dev
BASE-MAIN                 = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                    = agent/chapter-13-bombieri-vinogradov-v0.17.0
MODE                      = EVIDENCE-FIRST
PRE-AUTHORING-GATE        = OPEN
AUTHORING                 = BLOCKED
CENTRAL-TARGET            = BOMBIERI--VINOGRADOV / NOT YET ADOPTED
PROOF-ROUTE               = VAUGHAN-IDENTITY + LARGE-SIEVE / CANDIDATE
LEVEL-OF-DISTRIBUTION     = 1/2 WITH LOGARITHMIC LOSS / TARGET
DEPENDENCY-AUDIT          = OPEN
LOG-LOSS-AUDIT            = OPEN
EFFECTIVITY-AUDIT         = OPEN
RELEASE-READY             = NO
```

## إغلاق المرحلة السابقة

```text
CHAPTER-12          = REVIEWED / MERGED
PR-20               = MERGED
GOVERNANCE-PR-21    = MERGED
GOVERNANCE-MERGE    = 607c6f8ad76f8085828f49ce6b566c846950ab2a
LOCAL-SOURCE-BUILD  = PASS / 184 PAGES
RELEASE-READY       = NO
```

## لوحة التقدم

| المكوّن | الحالة | التقدم التقريبي |
|---|---:|---:|
| هيكل المستودع | مكتمل مبدئيًا | 100% |
| أهداف المشروع | مكتملة للإصدار الأول | 100% |
| نظام التوثيق والمتابعة | مكتمل مبدئيًا | 100% |
| بناء PDF المحلي والآلي | مسار محلي وآلي عامل | 100% |
| الفصل الأول: التاريخ والمنهج | مدقق داخليًا؛ الإحالات التفصيلية باقية | 85% |
| الفصل الثاني: اللغة التقاربية والجمع الجزئي | `VERIFIED` | 85% |
| الفصل الثالث: التحليل المركب الموجّه | `VERIFIED`؛ التوسعات مؤجلة | 80% |
| الفصل الرابع: الدوال الحسابية والالتفاف | `VERIFIED` | 92% |
| الفصل الخامس: سلاسل ديريشليه والمنتجات الأويلرية | `REVIEWED` | 78% |
| الفصل السادس: دالة زيتا لريمان | `REVIEWED` | 85% |
| الفصل السابع: دوال ديريشليه \(L\) | `REVIEWED` | 95% |
| الفصل الثامن: مبرهنة ديريشليه | `REVIEWED` | 90% |
| الفصل التاسع: مبرهنة الأعداد الأولية | `REVIEWED` | 92% |
| الفصل العاشر: PNT في المتتاليات الحسابية | `REVIEWED` | 94% |
| الفصل الحادي عشر: المناطق الخالية والأصفار الاستثنائية | `REVIEWED / MERGED` | 95% |
| الفصل الثاني عشر: Siegel--Walfisz | `REVIEWED / MERGED` | 95% |
| الفصل الثالث عشر: Bombieri--Vinogradov | `PRE-AUTHORING` | 12% |
| فصل الجبهات الحديثة | نواة أولية | 10% |
| الملحق الحاسوبي | أول تجربة مسجلة وقابلة للتشغيل | 15% |

## لقطة بوابات الفصول

| الفصل | البوابة الحالية | ما يمنع البوابة التالية |
|---|---|---|
| 1 | `DRAFT` | الإحالات التاريخية والحلول والمراجعة المستقلة |
| 2 | `VERIFIED` | مراجعة ثانية مستقلة |
| 3 | `VERIFIED` | مراجعة ثانية مستقلة والتوسعات المعلنة |
| 4 | `VERIFIED` | مراجعة ثانية مستقلة |
| 5 | `REVIEWED` | الديون التحريرية قبل `RELEASE-READY` |
| 6 | `REVIEWED` | براهين بيرون وتحويل المسار قبل `RELEASE-READY` |
| 7 | `REVIEWED` | حلول وتوسعات قبل `RELEASE-READY` |
| 8 | `REVIEWED` | أمثلة وتمارين وتدقيق إصدار |
| 9 | `REVIEWED` | الديون الفعالة والتحريرية |
| 10 | `REVIEWED` | أربعة تحسينات اختيارية وتدقيق إصدار |
| 11 | `REVIEWED / MERGED` | ديون الإصدار قبل `RELEASE-READY` |
| 12 | `REVIEWED / MERGED` | ديون المجلد والتنضيد قبل `RELEASE-READY` |
| 13 | `PRE-AUTHORING` | إغلاق الاعتمادات وType I/II والفعالية وعدم الدور |

التدقيق الداخلي والمراجعة المستقلة والدمج لا تجعل أي فصل `RELEASE-READY` تلقائيًا.

## الفصل الثالث عشر — المنجز

- دُمج PR #21 وأغلق الفصل الثاني عشر حوكميًا.
- أُنشئ الفرع من رأس الدمج `607c6f8ad76f8085828f49ce6b566c846950ab2a`.
- رُفع الإصدار إلى `0.17.0-dev`.
- قُرئت ملفات README وROADMAP وPROGRESS وTODO وRESULTS_REGISTRY وCHANGELOG قبل التعديل.
- بدأ المسح عبر Consensus.
- تحققت بيانات أوراق Bombieri (1965)، وA. I. Vinogradov (1965)، وتصحيح Vinogradov (1966)، وGallagher (1968)، وVaughan (1975).
- صيغ الهدف المركزي بصيغة \(\psi\) مع `max_{y\le x}` ومستوى \(1/2\) حتى خسارة لوغاريتمية.
- فُصلت النتيجة عن Siegel--Walfisz وعن Elliott--Halberstam وعن النتائج الموزونة بعد حاجز \(1/2\).
- أُنشئ سجل الأدلة وخريطة البرهان وتدقيق ما قبل التأليف.
- ثُبت حكم `PASS-FOR-RESEARCH-INTAKE / FAIL-FOR-AUTHORING`.

## الهدف المركزي المرشح

لكل \(A>0\) يوجد \(B=B(A)>0\) بحيث، إذا

\[
Q\le \frac{x^{1/2}}{(\log x)^B},
\]

فإن

\[
\sum_{q\le Q}\max_{(a,q)=1}\max_{2\le y\le x}
\left|\psi(y;q,a)-\frac{y}{\varphi(q)}\right|
\ll_A \frac{x}{(\log x)^A}.
\]

هذه الصيغة ليست نتيجة معتمدة بعد.

## العوائق الحالية

1. تثبيت صيغة الغربال الكبير وتطبيعها بالصفحات.
2. إثبات هوية Vaughan وتدقيق حدود \(U,V\).
3. إغلاق تقدير Type I.
4. إغلاق تقدير Type II.
5. تثبيت آلية `max_{y\le x}`.
6. تدقيق الموصلات والشخصيات المستحثة.
7. تدقيق الشخصية الرئيسية والعوامل المحلية.
8. حساب الخسائر اللوغاريتمية وشرط \(B(A)\).
9. الحكم على فعالية الثوابت.
10. فحص عدم الدور وحجز معرفات النتائج.

## الخطوة التالية

إغلاق عقدة الغربال الكبير أولًا، ثم كتابة هوية Vaughan في سجل تدقيق مستقل قبل أي إنشاء لملف الفصل.
